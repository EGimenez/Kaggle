
from Tweets.Tweets_lib import *
# ==============================

import gc
import re
import string
import operator
from collections import defaultdict

import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

import matplotlib.pyplot as plt
import seaborn as sns

import tokenization
from wordcloud import STOPWORDS

from sklearn.model_selection import StratifiedKFold, StratifiedShuffleSplit
from sklearn.metrics import precision_score, recall_score, f1_score

import tensorflow as tf
import tensorflow_hub as hub
from tensorflow import keras
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.keras.layers import Dense, Input, Dropout, GlobalAveragePooling1D
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, Callback

SEED = 1337

from spellchecker import SpellChecker
import pandas as pd
import os
import numpy
from tensorflow.keras.models import Model, Sequential
# from tensorflow.keras.layers import CuDNNLSTM as LSTM
from tensorflow.keras.layers import LSTM as LSTM
from tensorflow.keras.layers import SpatialDropout1D, Input, GlobalMaxPooling1D, GlobalAveragePooling1D, Dense, Bidirectional, Embedding, TimeDistributed, add, concatenate
from tensorflow.keras.optimizers import Adam
import spacy
import en_vectors_web_lg
import en_core_web_sm
import re
import random

spell = SpellChecker()
print("Loading spaCy")
nlp_ents = en_core_web_sm.load()
nlp_vects = en_vectors_web_lg.load()
nlp_vects.add_pipe(nlp_vects.create_pipe("sentencizer"))

if os.name == 'nt':
    df_train = pd.read_csv('C:\\Users\\EGimenez\\Programming\\PyCharmProjects\\Kaggle\\data\\Tweets\\train.csv', dtype={'id': np.int16, 'target': np.int8})
    df_test = pd.read_csv('C:\\Users\\EGimenez\\Programming\\PyCharmProjects\\Kaggle\\data\\Tweets\\test.csv', dtype={'id': np.int16})

else:
    df_train = pd.read_csv('../input/nlp-getting-started/train.csv', dtype={'id': np.int16, 'target': np.int8})
    df_test = pd.read_csv('../input/nlp-getting-started/test.csv', dtype={'id': np.int16})


for df in [df_train, df_test]:
    for col in ['keyword', 'location']:
        df[col] = df[col].fillna(f'no_{col}')


print("Parsing texts...")
print("url characters...")
df_train['text_cleaned'] = df_train.apply(lambda tweet: manage_url_tweet_characters(tweet), axis=1)
df_test['text_cleaned'] = df_test.apply(lambda tweet: manage_url_tweet_characters(tweet), axis=1)
print('contractions')
df_train['text_cleaned'] = df_train.apply(lambda tweet: manage_contractions(tweet), axis=1)
df_test['text_cleaned'] = df_test.apply(lambda tweet: manage_contractions(tweet), axis=1)
print('manage_tricks')
df_train['text_cleaned'] = df_train.apply(lambda tweet: manage_tricks(tweet), axis=1)
df_test['text_cleaned'] = df_test.apply(lambda tweet: manage_tricks(tweet), axis=1)
print('ner')
df_train['text_cleaned'] = df_train.apply(lambda tweet: manage_ner(tweet, nlp_ents), axis=1)
df_test['text_cleaned'] = df_test.apply(lambda tweet: manage_ner(tweet, nlp_ents), axis=1)
print('multi_word')
df_train['text_cleaned'] = df_train.apply(lambda tweet: manage_no_dictionable(tweet, nlp_vects, spell), axis=1)
df_test['text_cleaned'] = df_test.apply(lambda tweet: manage_no_dictionable(tweet, nlp_vects, spell), axis=1)
print('done')