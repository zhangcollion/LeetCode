from lyk_config import k, conf_th, DEBUG, load_data
import sys
sys.path.append('../input/timm045/')
import timm

from itertools import zip_longest
import json
import math
import gc
import os
from pathlib import Path

import faiss
import numpy as np
import cupy as cp
import pandas as pd

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, Dataset

from tqdm import tqdm
from PIL import Image
import joblib
import lightgbm as lgb
from scipy.sparse import hstack, vstack, csc_matrix, csr_matrix
import editdistance
import networkx as nx

import string
import nltk
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.tokenize import TweetTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer

NUM_CLASSES = 11014
NUM_WORKERS = 2
SEED = 0

class GraphDataset(Dataset):
    def __init__(self, feats=None, labels=None, weights=None, pair_tuples=None, k=50, top_neighbors=None):
        self.feats = feats
        self.labels = labels
        self.weights = weights
        self.pair_tuples = pair_tuples
        self.k = k
        self.top_neighbors = top_neighbors

    def __getitem__(self, index):
        i, j = self.pair_tuples[index]
        feat = torch.FloatTensor(self.feats[i][j])

        padding_i = [[0] * feat.shape[0]]*(self.k - len(self.top_neighbors[i]))
        neighbor_feats_i = torch.FloatTensor([self.feats[i][neighbor] for neighbor in self.top_neighbors]+padding_i)
        padding_j = [[0] * feat.shape[0]]*(self.k - len(self.top_neighbors[j]))
        neighbor_feats_j = torch.FloatTensor([self.feats[j][neighbor] for neighbor in self.top_neighbors]+padding_j)
        neighbor_feats = torch.cat([feat.unsqueeze(0), neighbor_feats_i, neighbor_feats_j], dim=0)

        outputs = (feat, neighbor_feats)

        if self.labels is not None:
            outputs += (self.labels[i]==self.labels[j], )

        if self.weights is not None:
            outputs += (self.weights[i],)

        return outputs

    def __len__(self):
        return len(self.pair_tuples)


        


