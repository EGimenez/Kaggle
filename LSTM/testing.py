import numpy as np
import pandas as pd
from tqdm import tqdm
import os

tqdm.pandas()
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Embedding, SpatialDropout1D, Dropout, add, concatenate
#from tensorflow.rs import CuDNNLSTM, Bidirectional, GlobalMaxPooling1D, GlobalAveragePooling1D
from tensorflow.keras.layers import CuDNNLSTM, Bidirectional, GlobalMaxPooling1D, GlobalAveragePooling1D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import text, sequence
from tensorflow.keras.callbacks import LearningRateScheduler

EMBEDDING_FILES = [
    '../input/gensim-embeddings-dataset/crawl-300d-2M.gensim',
    '../input/gensim-embeddings-dataset/glove.840B.300d.gensim'
]

EMBEDDING_FILES = [
    'data\\crawl-300d-2M.vec',
    'data\\glove.840B.300d.txt'
]

for path in EMBEDDING_FILES:
    with open(path, "r") as f:
        try:
            for i in range(100):
                line = f.readLine()
                print(line)
        except:
            pass


for path in EMBEDDING_FILES:
    with open(os.path.join(os.getcwd(), path)) as f:
        # return dict(get_coefs(*line.strip().split(' ')) for line in f)
        # return dict(get_coefs(*o.strip().split(" ")) for o in tqdm(f))
        my_dict = {}

        try:
            for o in tqdm(f):
                o.strip().split(" ")
        except:
            pass