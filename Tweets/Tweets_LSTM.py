from Tweets.Tweets_lib import manage_contractions, manage_url_tweet_characters, manage_tricks, manage_ner, manage_no_dictionable


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

BATCH_SIZE = 256
LSTM_UNITS = 128
DENSE_HIDDEN_UNITS = 4 * LSTM_UNITS
EPOCHS = 15
MAX_LEN = 40
LEARN_RATE = 0.001
BY_SENTENCE = True
CHARS_TO_REMOVE = '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n“”’\'∞θ÷α•à−β∅³π‘₹´°£€\×™√²—'

if os.name == 'nt':
    path = 'C:\\Users\\EGimenez\\Programming\\PyCharmProjects\\Kaggle\\data\\Tweets\\'
else:
    path = '/content/'

spell = SpellChecker()
print("Loading spaCy")
nlp_ents = en_core_web_sm.load()
nlp_vects = en_vectors_web_lg.load()
nlp_vects.add_pipe(nlp_vects.create_pipe("sentencizer"))

train_df = pd.read_csv(os.path.join(path, 'train.csv'))
test_df = pd.read_csv(os.path.join(path, 'test.csv'))


def manage_spelling(tweets):
    for i, tweet in enumerate(tweets):

        if i % 25 == 0:
            print(i)

        line = str(tweet)
        for word in tweet:
            if not word.has_vector:
                word = str(word)
                corr = spell.correction(str(word))
                print('{0} : {1}'.format(word, corr))
                line = line.replace(word, corr)
        tweets[i] = line
    tweets =list(nlp_vects.pipe(tweets))
    return tweets


def get_labelled_sentences(docs, doc_labels):
    labels = []
    sentences = []
    for doc, y in zip(docs, doc_labels):
        for sent in doc.sents:
            sentences.append(sent)
            labels.append(y)
    return sentences, numpy.asarray(labels, dtype="int32")


def get_features(docs, max_length):
    docs = list(docs)
    Xs = numpy.zeros((len(docs), max_length), dtype="int32")
    for i, doc in enumerate(docs):
        j = 0
        for token in doc:
            vector_id = token.vocab.vectors.find(key=token.orth)
            if vector_id >= 0:
                Xs[i, j] = vector_id
            else:
                Xs[i, j] = 0
            j += 1
            if j >= max_length:
                break
    return Xs


def compile_lstm(embeddings):
    words = Input(shape=(MAX_LEN,))
    x_1 = Embedding(
        embeddings.shape[0],
        embeddings.shape[1],
        input_length=MAX_LEN,
        trainable=False,
        weights=[embeddings],
        mask_zero=True,
    )(words)
    x_2 = SpatialDropout1D(0.2)(x_1)
    x_3 = Bidirectional(LSTM(LSTM_UNITS, return_sequences=True))(x_2)

    if True:
        x_3 = Bidirectional(LSTM(LSTM_UNITS, return_sequences=True))(x_3)

        y_1 = GlobalMaxPooling1D()(x_3)
        y_2 = GlobalAveragePooling1D()(x_3)
        hidden = concatenate([
            y_1,
            y_2,
        ])
    else:
        x_3 = Bidirectional(LSTM(LSTM_UNITS))(x_3)

        hidden = x_3
    #hidden = add([hidden, Dense(DENSE_HIDDEN_UNITS, activation='relu')(hidden)])
    #hidden = add([hidden, Dense(DENSE_HIDDEN_UNITS, activation='relu')(hidden)])

    hidden = Dense(DENSE_HIDDEN_UNITS, activation='relu')(hidden)
    hidden = Dense(DENSE_HIDDEN_UNITS, activation='relu')(hidden)
    hidden = Dense(DENSE_HIDDEN_UNITS, activation='relu')(hidden)

    result = Dense(1, activation='sigmoid')(hidden)

    model = Model(inputs=words, outputs=result)
    model.compile(
        optimizer=Adam(lr=LEARN_RATE),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    return model


def train():
    model = compile_lstm(nlp_vects.vocab.vectors.data)

    print("Parsing texts...")
    print("url characters...")
    train_df['text'] = train_df.apply(lambda tweet: manage_url_tweet_characters(tweet), axis=1)
    test_df['text'] = test_df.apply(lambda tweet: manage_url_tweet_characters(tweet), axis=1)
    print('contractions')
    train_df['text'] = train_df.apply(lambda tweet: manage_contractions(tweet), axis=1)
    test_df['text'] = test_df.apply(lambda tweet: manage_contractions(tweet), axis=1)
    print('manage_tricks')
    train_df['text'] = train_df.apply(lambda tweet: manage_tricks(tweet), axis=1)
    test_df['text'] = test_df.apply(lambda tweet: manage_tricks(tweet), axis=1)
    print('ner')
    train_df['text'] = train_df.apply(lambda tweet: manage_ner(tweet, nlp_ents), axis=1)
    test_df['text'] = test_df.apply(lambda tweet: manage_ner(tweet, nlp_ents), axis=1)
    print('multi_word')
    train_df['text'] = train_df.apply(lambda tweet: manage_no_dictionable(tweet, nlp_vects, spell), axis=1)
    test_df['text'] = test_df.apply(lambda tweet: manage_no_dictionable(tweet, nlp_vects, spell), axis=1)

    train_texts = train_df['text']
    train_labels =train_df['target']

    train_index = set(random.sample(range(train_texts.size), k=round(train_texts.size*.7)))
    dev_index = set(range(train_texts.size))-train_index

    dev_texts = train_texts.loc[dev_index]
    dev_labels = train_labels.loc[dev_index]

    train_texts = train_texts.loc[train_index]
    train_labels = train_labels.loc[train_index]

    train_docs = list(nlp_vects.pipe(train_texts))
    dev_docs = list(nlp_vects.pipe(dev_texts))

    #train_docs = manage_spelling(train_docs)
    #dev_docs =manage_spelling(dev_docs)

    if BY_SENTENCE:
        train_docs, train_labels = get_labelled_sentences(train_docs, train_labels)
        dev_docs, dev_labels = get_labelled_sentences(dev_docs, dev_labels)

    train_x = get_features(train_docs, MAX_LEN)
    dev_x = get_features(dev_docs, MAX_LEN)
    model.fit(
        train_x,
        train_labels,
        validation_data=(dev_x, dev_labels),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
    )
    return model


train()
