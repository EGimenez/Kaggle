from spellchecker import SpellChecker
import pandas as pd
import os
import re
import spacy
import matplotlib.pyplot as plt
import seaborn as sns
import spacy
import en_vectors_web_lg
import en_core_web_sm
from Tweets.Tweets_lib import manage_contractions, manage_url_tweet_characters, find_non_vector, manage_tricks, manage_ner, manage_no_dictionable

path = 'C:\\Users\\EGimenez\\Programming\\PyCharmProjects\\Kaggle\\data\\Tweets\\'

spell = SpellChecker()
nlp_ents = spacy.load('en_core_web_sm')
nlp_vects = spacy.load('en_vectors_web_lg')
nlp_vects.add_pipe(nlp_vects.create_pipe("sentencizer"))

train_df = pd.read_csv(os.path.join(path, 'train.csv'))

print("Parsing texts...")

print("url characters...")
#train_df['text'] = train_df.apply(lambda tweet: manage_url_tweet_characters(tweet), axis=1)
print('contractions')
#train_df['text'] = train_df.apply(lambda tweet: manage_contractions(tweet), axis=1)
print('manage_tricks')
#train_df['text'] = train_df.apply(lambda tweet: manage_tricks(tweet), axis=1)
print('ner')
#train_df['text'] = train_df.apply(lambda tweet: manage_ner(tweet, nlp_ents), axis=1)
print('multi_word')
train_df['text'] = train_df.apply(lambda tweet: manage_no_dictionable(tweet, nlp_vects, spell), axis=1)

train_texts = train_df['text']
train_labels = train_df['target']

train_docs = list(nlp_vects.pipe(train_texts))

find_non_vector(train_docs, nlp_vects, spell)


#
#
# # Number of sentences
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
# tweet_len = train_df[train_df['target'] == 1]['text'].str.split().map(lambda x: len(x))
# ax1.hist(tweet_len, color='red')
# ax1.set_title('disaster tweets')
# tweet_len = train_df[train_df['target'] == 0]['text'].str.split().map(lambda x: len(x))
# ax2.hist(tweet_len, color='green')
# ax2.set_title('Not disaster tweets')
# fig.suptitle('Words in a tweet')
# plt.show()
#
# # Number of sentences





    # for ent in doc.ents:
    #     print('\t' + str(ent) + ' ' + str(ent.label_))



    # for sent in doc.sents:
    #     line = str(sent)
    #     misspelled = spell.unknown(line.split(' '))
    #
    #     for w in misspelled:
    #         line = line.replace(w, spell.correction(w))
    #
    #     sent = nlp(line)
    #
    #     for word in sent:
    #         w_t += 1
    #         if word.has_vector:
    #             w_v += 1
    #         else:
    #             print(word)
    #
    # print(str(i)+': ' + str(w_v) + '/' + str(w_t))



# # find those words that may be misspelled
# misspelled = spell.unknown(['something', 'is', 'hapenning', 'here', 'helo'])
#
# for word in misspelled:
#     # Get the one `most likely` answer
#     print(spell.correction(word))
#
#     # Get a list of `likely` options
#     print(spell.candidates(word))
#
# pass