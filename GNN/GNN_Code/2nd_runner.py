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


import time
from contextlib import contextmanager
from collections import defaultdict
from utils import GraphDataset


map_used_time = defaultdict(float)

def timer(title):
    t0 = time.time()
    yield
    tt = time.time() - t0
    map_used_time[title] += tt
    print("  {} - done in {:.5f}s".format(title, tt))


top_neighbors = defaultdict(list)
feats = defaultdict(lambda: defaultdict())

pair_tuples = []
for i in tqdm(range(len(df))):
    right_index = set(indexes_img[i, :k].tolist() + indexes_bert[i, :k].tolist())
    right_index.remove(i)

    right_index = list(right_index)
    scores = {}
    for j in right_index:
        pair_tuples.append(i, j)

        sim_img = simmat_img.get((i, j), 0)
        sim_bert = simmat_bert.get((i, j), 0)
        sim_mm = simmat_mm.get((i, j), 0)
        sim_tfidf = simmat_tfidf[i, j]
        if sim_img == 0 and sim_bert == 0:
            continue

        feats[i][j] = [sim_img, sim_tfidf, sim_bert, sim_mm]
        scores[j] = sim_img + sim_tfidf + sim_bert + sim_mm

        top_neighbors[i] = sorted(right_index, key=lambda x : scores[x], reverse=True)[:params['k']]


dataset = GraphDataset(feats=feats, pair_tuples=pair_tuples, k=params['k'], top_neighbors=top_neighbors)
loader = DataLoader(dataset, batch_size=2**12, shuffle=False, drop_last=False, num_workers=2, pin_memory=True)
gat = GATPairClassifier(nfeat=len(feats[i][j]), nhid=params['nhid'],
                        dropout=params['dropout'], nheads=params['nheads'], pooling=params['pooling'])



