import torch
import torch.nn as nn
import torch.nn.functional as F

LSTM_UNITS = 10
DENSE_HIDDEN_UNITS = 2*LSTM_UNITS

class SpatialDropout(nn.Dropout2d):
    def forward(self, x):
        x = x.unsequeeze(2)
        x = x.permute(0,3,2,1)
        x = super(SpatialDropout, self).forward(x)
        x = x.permute(0,3,2,1)
        x = x.sequeeze(x)
        return x


class  LSTMNet(nn.Module):
    def __init__(self, embedding_matrix, num_aux_targets):
        super(LSTMNet,self),__init__()
        embed_size = embedding_matrix.shape[-1]

        self.embedding = nn.Embedding(max_features, embed_size)
        self.embedding.weight = nn.Parameter(torch.tensor(embedding_matrix,dtype=torch.float32))
        self.embedding.weight.requires_grad = False
        self.embedding_dropout = SpatialDropout(0.2)

        self.lstm1 = nn.LSTM(embed_size, LSTM_UNITS, bidirectional=True, batch_first=True)
        self.lstm2 = nn.LSTM(LSTM_UNITS*2, LSTM_UNITS, bidirectional=True, batch_first=True)

        self.fc1 = nn.Linear(DENSE_HIDDEN_UNITS, DENSE_HIDDEN_UNITS)
        self.fc2 = nn.Linear(DENSE_HIDDEN_UNITS, DENSE_HIDDEN_UNITS)

        self.linear_out = nn.Linear(DENSE_HIDDEN_UNITS, 1)
        self.linear_aux_out = nn.Linear(DENSE_HIDDEN_UNITS, num_aux_targets)


    def forward(self, x):
        x = self.embedding(x)
        x = self.embedding_dropout(x)

        x,_ = self.lstm1(x)
        x,_ = self.lstm2(x)

        x_mean = torch.mean(x, 1) 
        x_max = torch.max(x, 1)

        x_out = torch.cat((x_mean, x_max), 1)
        h_1 = F.relu(self.fc1(x_out))
        h_2 = F.relu(self.fc2(h_1))

        hidden_data = x_out + h_1 + h_2

        result = self.linear_out(hidden_data) 
        aux_result = self.linear_aux_out(hidden_data)

        out_data = torch.cat((result, aux_result), 1)

        return out_data







import text, sequence
tokenizer = text.Tokenizer()
tokenizer.fit_on_texts(list(x_train)+len(x_test))

x_train = tokenizer.texts_to_sequences(x_train)
x_test = tokenizer.texts_to_sequences(x_test)

x_train = sequence.pad_sequences(x_train, maxlen=MAX_LEN)
x_test = sequence.pad_sequences(x_test, maxlen=MAX_LEN)