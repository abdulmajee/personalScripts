import nltk
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from nltk import pos_tag
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree
from nltk.tree import Tree

style.use('fivethirtyeight')


# Process text
def process_text(txt_file):
    raw_text = open("220-01.txt").read()
    token_text = word_tokenize(raw_text)
    return token_text


# # Stanford NER tagger
# def stanford_tagger(token_text):
#     st = StanfordNERTagger('/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
#                            '/usr/share/stanford-ner/stanford-ner.jar',
#                            encoding='utf-8')
#     ne_tagged = st.tag(token_text)
#     return (ne_tagged)
#
#
# # NLTK POS and NER taggers
# def nltk_tagger(token_text):
#     tagged_words = nltk.pos_tag(token_text)
#     ne_tagged = nltk.ne_chunk(tagged_words)
#     return (ne_tagged)


# Tag tokens with standard NLP BIO tags
def bio_tagger(ne_tagged):
    bio_tagged = []
    prev_tag = "O"
    for token, tag in ne_tagged:
        if tag == "O":  # O
            bio_tagged.append((token, tag))
            prev_tag = tag
            continue
        if tag != "O" and prev_tag == "O":  # Begin NE
            bio_tagged.append((token, "B-" + tag))
            prev_tag = tag
        elif prev_tag != "O" and prev_tag == tag:  # Inside NE
            bio_tagged.append((token, "I-" + tag))
            prev_tag = tag
        elif prev_tag != "O" and prev_tag != tag:  # Adjacent NE
            bio_tagged.append((token, "B-" + tag))
            prev_tag = tag
    return bio_tagged


tokenized_text = process_text('./220-01.txt')

# print(tokenized_text)
bio_tagged = bio_tagger(tokenized_text)
print(bio_tagged)