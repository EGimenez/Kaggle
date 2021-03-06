import re
import glob
import spacy
import nltk
from wordcloud import WordCloud
import pandas as pd

docs = list()
nlp = spacy.load("en_core_web_sm")


def clean_html(line):
    return re.sub('<.*>', '', line)


def token_filter(token):
    if token.pos_ in ['NUM', 'SYM', 'ADP', 'AUX', 'DET', 'INTJ', 'PRON', 'SCONJ', 'PART']:
        return ''
    elif token.pos_ == 'PROPN':
        return ''
    else:
        if token.lemma_ == 'PRON':
            print('eo')
        return token.lemma_.lower()


def get_docs(article):
    # Eliminamos Q&A
    article = article.split('Transcript of the questions asked')[0]
    article = article.split('* * *')[0]

    res = re.findall('<p>(.*)</p>', article)

    docs = ''

    for line in res:
        doc = nlp(clean_html(line))
        for token in doc:
            docs = docs + ' ' + token_filter(token)

    return [docs]

# Read data into papers
path = "../tutorial/ecb_data/*.html"
for filename in glob.glob(path):
    with open(filename, 'r', encoding="utf-8") as f:
        try:
            article = f.read()
            docs = docs + get_docs(article)
        except Exception as ex:
            print('eo')

# Join the different processed titles together.
long_string = ','.join(docs)

# N-Grams
words = re.findall(r"[\w']+", long_string)
words = [word for word in long_string.split(' ')]

bigrams = nltk.collocations.BigramAssocMeasures()
trigrams = nltk.collocations.TrigramAssocMeasures()

bigramFinder = nltk.collocations.BigramCollocationFinder.from_words(words)
trigramFinder = nltk.collocations.TrigramCollocationFinder.from_words(words)

bigramFinder.apply_freq_filter(50)
the_bigrams = list(bigramFinder.score_ngrams(bigrams.pmi))
# bigramPMITable = pd.DataFrame(list(bigramFinder.score_ngrams(bigrams.pmi)), columns=['bigram', 'PMI']).sort_values(by='PMI', ascending=False)
# bigramPMITable[:10]
# for i in range(1, 200):
#     print(bigramPMITable[i - 1:i])

trigramFinder.apply_freq_filter(50)
the_trigrams = list(trigramFinder.score_ngrams(trigrams.pmi))
# trigramPMITable = pd.DataFrame(list(trigramFinder.score_ngrams(trigrams.pmi)), columns=['trigram','PMI']).sort_values(by='PMI', ascending=False)
# trigramPMITable[:10]
# for i in range(1, 200):
#     print(trigramPMITable[i - 1:i])

# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')

# Generate a word cloud
wordcloud.generate(long_string)

# Visualize the word cloud
wordcloud.to_image().show()

# Load the library with the CountVectorizer method
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')


# Helper function
def plot_10_most_common_words(count_data, count_vectorizer):
    import matplotlib.pyplot as plt
    words = count_vectorizer.get_feature_names()
    total_counts = np.zeros(len(words))
    for t in count_data:
        total_counts += t.toarray()[0]

    count_dict = (zip(words, total_counts))
    count_dict = sorted(count_dict, key=lambda x: x[1], reverse=True)[0:10]
    words = [w[0] for w in count_dict]
    counts = [w[1] for w in count_dict]
    x_pos = np.arange(len(words))

    plt.figure(2, figsize=(15, 15 / 1.6180))
    plt.subplot(title='10 most common words')
    sns.set_context("notebook", font_scale=1.25, rc={"lines.linewidth": 2.5})
    sns.barplot(x_pos, counts, palette='husl')
    plt.xticks(x_pos, words, rotation=90)
    plt.xlabel('words')
    plt.ylabel('counts')
    plt.show()


# Initialise the count vectorizer with the English stop words
count_vectorizer = CountVectorizer(stop_words='english')

# Fit and transform the processed titles
count_data = count_vectorizer.fit_transform(docs)

# Visualise the 10 most common words
plot_10_most_common_words(count_data, count_vectorizer)

import warnings

warnings.simplefilter("ignore", DeprecationWarning)

# Load the LDA model from sk-learn
from sklearn.decomposition import LatentDirichletAllocation as LDA


# Helper function
def print_topics(model, count_vectorizer, n_top_words):
    words = count_vectorizer.get_feature_names()
    for topic_idx, topic in enumerate(model.components_):
        print("\nTopic #%d:" % topic_idx)
        print(" ".join([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))


# Tweak the two parameters below (use int values below 15)
number_topics = 5
number_words = 10

# Create and fit the LDA model
lda = LDA(n_components=number_topics)
lda.fit(count_data)

# Print the topics found by the LDA model
print("Topics found via LDA:")
print_topics(lda, count_vectorizer, number_words)
