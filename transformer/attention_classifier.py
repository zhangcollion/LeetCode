import numpy as np 
import json
import os
import torch
import random 
from pathlib import Path
from torch.utils.data import Dataset
from torch.nn.utils.rnn import pad_sequence

class SpeakerDataset(Dataset):
    def __init__(self, data_dir, segment_len=128):
        self.data_dir = data_dir
        self.segment_len = segment_len

        mapping_data = Path(data_dir)/"mapping.json"
        mapping = json.load(mapping_path.open())
        self.speaker2id = mapping["speaker2id"]

        metadata_path = Path(data_dir)/'metadata.json'
        metadata = json.load(metadata_path.open())["speakers"]
        self.speaker_num = len(metadata.keys())
        self.data = []
        for speaker in metadata.keys():
            for utterances in metadata[speaker]:
                self.data.append([utterances["feature_path"], self.speaker2id[speaker]])


    def __len__(self):
        return len(self.data)


    def __getitem__(self, index):
        feat_path, speaker = self.data[index]
        mel = torch.load(os.path.json(self.data_dir, feat_path))
        if len(mel) > self.segment_len:
            start = random.randint(0, len(mel) - self.segment_len)
            # Get a segment with "segment_len" frames.
            mel = torch.FloatTensor(mel[start:start+self.segment_len])
        else:
            mel = torch.FloatTensor(mel)

        speaker = torch.FloatTensor([speaker]).long()
        return mel, speaker

    def get_speaker_num(self):
        return self.speaker_num


import torch
from torch.utils.data import DataLoader, random_split
from torch.nn.utils.rnn import pad_sequence

def collate_batch(batch):
    mel, speaker = zip(*batch)
    mel = pad_sequence(mel, batch_first=True, padding_value=-20)
    return mel, torch.FloatTensor(speaker).long()

def get_dataloader(data_dir, batch_size, n_worker):
    dataset = SpeakerDataset(data_dir)
    speaker_num = dataset.get_speaker_num()
    train_len = int(0.9*len(dataset))
    lengths = [trainlen, len(dataset) - trainlen]
    trainset, validset = random_split(dataset, lengths)

    ## 因为每个speaker的segment 不同，需要padding对齐
    train_loader = DataLoader(
        trainset,
        batch_size=batch_size,
        shuffle=True,
        drop_last=True,
        num_workers=n_worker,
        pin_memory=True,
        collate_fn=collate_batch
        )
    valid_loader = DataLoader(
        validset,
        batch_size=batch_size,
        num_workers=n_workers,
        drop_last=True,
        pin_memory=True,
        collate_fn=collate_batch,
        )
    return train_loader, valid_loader, speaker_num



import torch
import torch.nn as nn
import torch.nn.functional as F


class attention_classifier(nn.Module):
    def self.__init__(self, d_model=80, n_spks=600, dropout=0.1):
        super(attention_classifier, self).__init__()
        self.embedding = nn.Linear(40, d_model)
        self.attn = nn.TransformerEncoderLayer(d_model=d_model, dim_feedforward=1024,nhead=8)

        self.pred_layer = nn.Sequential(nn.Linear(d_model, d_model),
            nn.Sigmoid(),
            nn.Linear(d_model, n_spks))

    def forward(self, mels):
        out = self.embedding(mels)
        out = out.permute(1,0,2)
        out = self.attn(out)
        out = out.transpose(0,1)
        stats = out.mean(dim=1)
        out = self.pred_layer(stats)
        return out
