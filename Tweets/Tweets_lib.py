import re
import os
#import spacy
#nlp_vects = spacy.load('en_vectors_web_lg')
from spellchecker import SpellChecker

def manage_contractions(tweet):
    tweet = tweet.text
    tweet_ = tweet

    # Contractions
    tweet = re.sub(r"\bain'?t\b", "am not", tweet, flags=re.I)
    tweet = re.sub(r"\baren'?t\b", "are not", tweet, flags=re.I)
    tweet = re.sub(r"\bcan'?t\b", "cannot", tweet, flags=re.I)
    tweet = re.sub(r"\bcouldn'?t\b", "could not", tweet, flags=re.I)
    tweet = re.sub(r"\bcould'?ve\b", "could have", tweet, flags=re.I)
    tweet = re.sub(r"\bdidn'?t\b", "did not", tweet, flags=re.I)
    tweet = re.sub(r"\bdoesn'?t\b", "does not", tweet, flags=re.I)
    tweet = re.sub(r"\bdon'?t\b", "do not", tweet, flags=re.I)
    tweet = re.sub(r"\bhasn'?t\b", "has not", tweet, flags=re.I)
    tweet = re.sub(r"\bhaven'?t\b", "have not", tweet, flags=re.I)
    tweet = re.sub(r"\bhe'?ll\b", "he will", tweet, flags=re.I)
    tweet = re.sub(r"\bhere'?s\b", "here is", tweet, flags=re.I)
    tweet = re.sub(r"\bhe'?s\b", "he is", tweet, flags=re.I)
    tweet = re.sub(r"\bi'?d\b", "i would", tweet, flags=re.I)
    tweet = re.sub(r"\bi'?ll\b", "i will", tweet, flags=re.I)
    tweet = re.sub(r"\bi'?m\b", "i am", tweet, flags=re.I)
    tweet = re.sub(r"\bisn'?t\b", "is not", tweet, flags=re.I)
    tweet = re.sub(r"\bit'?ll\b", "it will", tweet, flags=re.I)
    tweet = re.sub(r"\bit'?s\b", "it is", tweet, flags=re.I)
    tweet = re.sub(r"\bit'?s\b", "it is", tweet, flags=re.I)
    tweet = re.sub(r"\bi'?ve\b", "i have", tweet, flags=re.I)
    tweet = re.sub(r"\blet'?s\b", "let us", tweet, flags=re.I)
    tweet = re.sub(r"\bshouldn'?t\b", "should not", tweet, flags=re.I)
    tweet = re.sub(r"\bshould'?ve\b", "should have", tweet, flags=re.I)
    tweet = re.sub(r"\bthat'?s\b", "that is", tweet, flags=re.I)
    tweet = re.sub(r"\bthere'?s\b", "there is", tweet, flags=re.I)
    tweet = re.sub(r"\bthey'?d\b", "they would", tweet, flags=re.I)
    tweet = re.sub(r"\bthey'?ll\b", "they will", tweet, flags=re.I)
    tweet = re.sub(r"\bthey'?re\b", "they are", tweet, flags=re.I)
    tweet = re.sub(r"\bthey'?ve\b", "they have", tweet, flags=re.I)
    tweet = re.sub(r"\bwasn'?t\b", "was not", tweet, flags=re.I)
    tweet = re.sub(r"\bwe'?d\b", "we would", tweet, flags=re.I)
    tweet = re.sub(r"\bwe'?ll\b", "we will", tweet, flags=re.I)
    tweet = re.sub(r"\bwe'?re\b", "we are", tweet, flags=re.I)
    tweet = re.sub(r"\bweren'?t\b", "were not", tweet, flags=re.I)
    tweet = re.sub(r"\bwe'?ve\b", "we have", tweet, flags=re.I)
    tweet = re.sub(r"\bwhat'?s\b", "what is", tweet, flags=re.I)
    tweet = re.sub(r"\bwhere'?s\b", "where is", tweet, flags=re.I)
    tweet = re.sub(r"\bwho'?s\b", "who is", tweet, flags=re.I)
    tweet = re.sub(r"\bwon'?t\b", "will not", tweet, flags=re.I)
    tweet = re.sub(r"\bwouldn'?t\b", "would not", tweet, flags=re.I)
    tweet = re.sub(r"\bwould'?ve\b", "would have", tweet, flags=re.I)
    tweet = re.sub(r"\by'?all\b", "you all", tweet, flags=re.I)
    tweet = re.sub(r"\byou'?d\b", "you would", tweet, flags=re.I)
    tweet = re.sub(r"\byou'?ll\b", "you will", tweet, flags=re.I)
    tweet = re.sub(r"\byou'?re\b", "you are", tweet, flags=re.I)
    tweet = re.sub(r"\byou'?ve\b", "you have", tweet, flags=re.I)

    if tweet.find('woulded') != -1:
        print('oe')

    return tweet


def manage_contractions_old(tweet):
    tweet = tweet.text
    # Contractions
    tweet = re.sub(r"he's", "he is", tweet, flags=re.I)
    tweet = re.sub(r"there's", "there is", tweet, flags=re.I)
    tweet = re.sub(r"We're", "We are", tweet, flags=re.I)
    tweet = re.sub(r"That's", "That is", tweet, flags=re.I)
    tweet = re.sub(r"won't", "will not", tweet, flags=re.I)
    tweet = re.sub(r"they're", "they are", tweet, flags=re.I)
    tweet = re.sub(r"Can't", "Cannot", tweet, flags=re.I)
    tweet = re.sub(r"wasn't", "was not", tweet, flags=re.I)
    tweet = re.sub(r"don\x89Ûªt", "do not", tweet, flags=re.I)
    tweet = re.sub(r"aren't", "are not", tweet, flags=re.I)
    tweet = re.sub(r"isn't", "is not", tweet, flags=re.I)
    tweet = re.sub(r"What's", "What is", tweet, flags=re.I)
    tweet = re.sub(r"haven't", "have not", tweet, flags=re.I)
    tweet = re.sub(r"hasn't", "has not", tweet, flags=re.I)
    tweet = re.sub(r"There's", "There is", tweet, flags=re.I)
    tweet = re.sub(r"He's", "He is", tweet, flags=re.I)
    tweet = re.sub(r"It's", "It is", tweet, flags=re.I)
    tweet = re.sub(r"You're", "You are", tweet, flags=re.I)
    tweet = re.sub(r"I'M", "I am", tweet, flags=re.I)
    tweet = re.sub(r"shouldn't", "should not", tweet, flags=re.I)
    tweet = re.sub(r"wouldn't", "would not", tweet, flags=re.I)
    tweet = re.sub(r"i'm", "I am", tweet, flags=re.I)
    tweet = re.sub(r"I\x89Ûªm", "I am", tweet, flags=re.I)
    tweet = re.sub(r"I'm", "I am", tweet, flags=re.I)
    tweet = re.sub(r"Isn't", "is not", tweet, flags=re.I)
    tweet = re.sub(r"Here's", "Here is", tweet, flags=re.I)
    tweet = re.sub(r"you've", "you have", tweet, flags=re.I)
    tweet = re.sub(r"you\x89Ûªve", "you have", tweet, flags=re.I)
    tweet = re.sub(r"we're", "we are", tweet, flags=re.I)
    tweet = re.sub(r"what's", "what is", tweet, flags=re.I)
    tweet = re.sub(r"couldn't", "could not", tweet, flags=re.I)
    tweet = re.sub(r"we've", "we have", tweet, flags=re.I)
    tweet = re.sub(r"it\x89Ûªs", "it is", tweet, flags=re.I)
    tweet = re.sub(r"doesn\x89Ûªt", "does not", tweet, flags=re.I)
    tweet = re.sub(r"It\x89Ûªs", "It is", tweet, flags=re.I)
    tweet = re.sub(r"Here\x89Ûªs", "Here is", tweet, flags=re.I)
    tweet = re.sub(r"who's", "who is", tweet, flags=re.I)
    tweet = re.sub(r"I\x89Ûªve", "I have", tweet, flags=re.I)
    tweet = re.sub(r"y'all", "you all", tweet, flags=re.I)
    tweet = re.sub(r"can\x89Ûªt", "cannot", tweet, flags=re.I)
    tweet = re.sub(r"would've", "would have", tweet, flags=re.I)
    tweet = re.sub(r"it'll", "it will", tweet, flags=re.I)
    tweet = re.sub(r"we'll", "we will", tweet, flags=re.I)
    tweet = re.sub(r"wouldn\x89Ûªt", "would not", tweet, flags=re.I)
    tweet = re.sub(r"We've", "We have", tweet, flags=re.I)
    tweet = re.sub(r"he'll", "he will", tweet, flags=re.I)
    tweet = re.sub(r"Y'all", "You all", tweet, flags=re.I)
    tweet = re.sub(r"Weren't", "Were not", tweet, flags=re.I)
    tweet = re.sub(r"Didn't", "Did not", tweet, flags=re.I)
    tweet = re.sub(r"they'll", "they will", tweet, flags=re.I)
    tweet = re.sub(r"they'd", "they would", tweet, flags=re.I)
    tweet = re.sub(r"DON'T", "DO NOT", tweet, flags=re.I)
    tweet = re.sub(r"That\x89Ûªs", "That is", tweet, flags=re.I)
    tweet = re.sub(r"they've", "they have", tweet, flags=re.I)
    tweet = re.sub(r"i'd", "I would", tweet, flags=re.I)
    tweet = re.sub(r"should've", "should have", tweet, flags=re.I)
    tweet = re.sub(r"You\x89Ûªre", "You are", tweet, flags=re.I)
    tweet = re.sub(r"where's", "where is", tweet, flags=re.I)
    tweet = re.sub(r"Don\x89Ûªt", "Do not", tweet, flags=re.I)
    tweet = re.sub(r"we'd", "we would", tweet, flags=re.I)
    tweet = re.sub(r"i'll", "I will", tweet, flags=re.I)
    tweet = re.sub(r"weren't", "were not", tweet, flags=re.I)
    tweet = re.sub(r"They're", "They are", tweet, flags=re.I)
    tweet = re.sub(r"Can\x89Ûªt", "Cannot", tweet, flags=re.I)
    tweet = re.sub(r"you\x89Ûªll", "you will", tweet, flags=re.I)
    tweet = re.sub(r"I\x89Ûªd", "I would", tweet, flags=re.I)
    tweet = re.sub(r"let's", "let us", tweet, flags=re.I)
    tweet = re.sub(r"it's", "it is", tweet, flags=re.I)
    tweet = re.sub(r"can't", "cannot", tweet, flags=re.I)
    tweet = re.sub(r"don't", "do not", tweet, flags=re.I)
    tweet = re.sub(r"you're", "you are", tweet, flags=re.I)
    tweet = re.sub(r"i've", "I have", tweet, flags=re.I)
    tweet = re.sub(r"that's", "that is", tweet, flags=re.I)
    tweet = re.sub(r"i'll", "I will", tweet, flags=re.I)
    tweet = re.sub(r"doesn't", "does not", tweet, flags=re.I)
    tweet = re.sub(r"i'd", "I would", tweet, flags=re.I)
    tweet = re.sub(r"didn't", "did not", tweet, flags=re.I)
    tweet = re.sub(r"ain't", "am not", tweet, flags=re.I)
    tweet = re.sub(r"you'll", "you will", tweet, flags=re.I)
    tweet = re.sub(r"I've", "I have", tweet, flags=re.I)
    tweet = re.sub(r"Don't", "do not", tweet, flags=re.I)
    tweet = re.sub(r"I'll", "I will", tweet, flags=re.I)
    tweet = re.sub(r"I'd", "I would", tweet, flags=re.I)
    tweet = re.sub(r"Let's", "Let us", tweet, flags=re.I)
    tweet = re.sub(r"you'd", "You would", tweet, flags=re.I)
    tweet = re.sub(r"It's", "It is", tweet, flags=re.I)
    tweet = re.sub(r"Ain't", "am not", tweet, flags=re.I)
    tweet = re.sub(r"Haven't", "Have not", tweet, flags=re.I)
    tweet = re.sub(r"Could've", "Could have", tweet, flags=re.I)
    tweet = re.sub(r"youve", "you have", tweet, flags=re.I)
    tweet = re.sub(r"donå«t", "do not", tweet, flags=re.I)


    return tweet


def manage_url_tweet_characters(tweet):
    tweet = tweet.text
    tweet_ = tweet

    tweet = re.sub(r"https?:\/\/t.co\/[A-Za-z0-9]+", "", tweet)
    tweet = re.sub('#', '', tweet)
    tweet = re.sub('@.*', 'author', tweet)
    tweet = re.sub('\n', ' ', tweet)

    tweet = re.sub('_', ' ', tweet)

    # Character entity references
    tweet = re.sub(r"&gt;", " ", tweet)
    tweet = re.sub(r"&lt;", " ", tweet)
    tweet = re.sub(r"&amp;", " ", tweet)

    # Extended Characters
    tweet = tweet.encode('iso-8859-1').decode('ascii', 'ignore')

    return tweet


def manage_tricks(tweet):
    tweet = tweet.text
    tweet_ = tweet

    # Three letters
    tweet = re.sub(r'([a-z])\1\1+', r'\1\1', tweet)
    tweet = re.sub(r'([A-Z])\1\1+', r'\1\1', tweet)

    # LetterNumber -> Letter -> Number
    tweet = re.sub("([a-zA-Z])(\d)", r"\1 \2", tweet)
    tweet = re.sub("(\d)([a-zA-Z])", r"\1 \2", tweet)

    # HowAreYou -> How Are You
    tweet = re.sub('([a-z])([A-Z])', r'\1 \2', tweet)

    # numbers & percentage
    re.sub(r'\s[\+~\-]?\d+[\.,\']?\d*\%', ' percentage ', tweet)
    tweet = re.sub(r'\s[\+~\-]?\d+[\.,\']?\d*\s', ' number ', tweet)

    # Dates and times
    tweet = re.sub('\d\d:\d\d:\d\d', 'time', tweet)
    tweet = re.sub('\d\d/\d\d/\d\d', 'date', tweet)
    tweet = re.sub('\d\d/\d\d/\d\d\d\d', 'date', tweet)

    # letter weird letter
    tweet = re.sub('(\d),(\d)', r'\1\2', tweet)
    tweet = re.sub(r'(\d)\.(\d)', r'\1\2', tweet)
    tweet = re.sub('([a-zA-Z0-9])[^a-zA-Z0-9]([a-zA-Z0-9])', r'\1 \2', tweet)

    # dot letter
    tweet = re.sub(r'\b\.([a-zA-Z])', r'\1', tweet)

    # remove more than two spaces
    tweet = re.sub(r' +', r' ', tweet)

    if tweet.find('Rescuers recover') != -1:
        print('eo')

    if tweet.find(r'\.author') != -1:
        print('eo')

    return tweet


def manage_ner(tweet, nlp):
    tweet = tweet.text
    # PERSON    People, including    fictional.
    # NORP    Nationalities or religious or political    groups.
    # FAC    Buildings, airports, highways, bridges, etc.
    # ORG    Companies, agencies, institutions, etc.
    # GPE    Countries, cities, states.
    # LOC     	Non-GPE locations, mountain ranges, bodies of water.
    # MONEY    Monetary    values, including    unit.
    labels = ['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'MONEY']
    tweet_ = tweet
    tweet = re.sub('[\|\(\)]', '', tweet)
    tweet = re.sub("'", '', tweet)
    doc = nlp(tweet)


    for ent in doc.ents:
        if ent.label_ in labels:
            try:
                if os.name == 'nt':
                    tweet = re.sub('('+ent.text+')', ent.label_, tweet)
                else:
                    tweet = re.sub('('+ent.text+')', ent.label_+' \\1', tweet)
            except:
                pass

    if tweet.find('ORGDemolition') != -1:
        print('person')

    if tweet.find('PERSONDetonate') != -1:
        print('person')


    return tweet


def manage_no_dictionable(tweet, nlp, spell):
    id = tweet.id

    tweet = tweet.text
    doc = nlp(tweet)
    for word in doc:
        if word.has_vector:
            pass
        else:
            if id % 100000000 == 0:
                print(id)
                print(str(word))
            new_words = split_multi_word(str(word), spell, 4)
            if id % 100000000 == 0:
                print(new_words)
            try:
                tweet_ = tweet
                tweet = re.sub(str(word), new_words, tweet)
                manage_no_dictionable.dic[tweet_] = tweet
            except:
                pass
    return tweet


def is_vectorable(word, spell):
    if len(word) < 3:
        return False
    if spell.known([word]):
        return word
    else:
        for i in range(3, len(word)):
            w1 = word[0:i]
            w2 = word[i:]

            w1_r = is_vectorable(w1, spell)
            w2_r = is_vectorable(w2, spell)

            if w1_r and w2_r:
                return w1_r + ' ' + w2_r

        return False


def split_multi_word(word, spell, depth):
    try:
        aux = split_multi_word.dict[word]
        return aux[0], aux[1]
    except:
        if word == '':
            return '', 0
        else:
            if spell.known([word]):
                return word, 1/len(word)
            else:
                if depth > 0:
                    the_score = len(word)
                    the_sub_words = word
                    for l in range(min(12, len(word)), 0, -1):
                        for i in range(0, len(word)-l+1):
                            sub_word = word[i:i+l]
                            if spell.known([sub_word]):
                                score = 1/len(sub_word)

                                word_left = word[0:i]
                                word_right = word[i+l:]

                                sub_words_left, score_left = split_multi_word(word_left, spell, depth - 1)
                                sub_words_right, score_right = split_multi_word(word_right, spell, depth - 1)

                                score = score_left + score + score_right
                                sub_words = sub_words_left + ' ' + sub_word + ' ' + sub_words_right

                                if the_score > score:
                                    the_score = score
                                    the_sub_words = sub_words
                else:
                    the_score = 1/len(word)
                    the_sub_words = word
                split_multi_word.dict[word] = [the_sub_words, the_score]
                return the_sub_words, the_score


split_multi_word.dict = {}


def find_non_vector(docs, nlp_vects, spell):

    no_vects = {}
    vects = {}
    vectorable = set()

    for i, doc in enumerate(docs):

        if i % 500 == 0:
            print(i)
        if i > 5500:
            print(i)


        for sentence in doc.sents:
            for word in sentence:
                if not word.has_vector:
                    v, s = split_multi_word(str(word), spell)
                    if v:
                        vectorable.add(v)
                    else:
                        try:
                            no_vects[str(word)] += 1
                        except:
                            no_vects[str(word)] = 1
                else:
                    try:
                        vects[str(word)] += 1
                    except:
                        vects[str(word)] = 1

    print('Unknown')
    index = sorted(no_vects.items(), key=lambda item: item[1], reverse=True)
    for j, element in enumerate(index):
        print('{0} : {1}'.format(element[0], element[1]))
        j += 1
        if j == 10000:
            break

    print(len(no_vects))

    print('Known')
    index = sorted(vects.items(), key=lambda item: item[1], reverse=True)
    for j, element in enumerate(index):
        print('{0}: {1}'.format(element[0], element[1]))
        j += 1
        if j == 100:
            break

    print('Done!!!')



