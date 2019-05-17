import os

import pandas as pd
import numpy as np
from nltk.tokenize import sent_tokenize
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer


def df_review():
    path_to_csv = "reviews.csv"
    return pd.read_csv(path_to_csv)

def X_reviews(data=df_review):
    reviews = df_review()['review'].values
    word_tokenizer = Tokenizer(num_words=20000)
    word_tokenizer.fit_on_texts(reviews)

    X = np.zeros((len(reviews), 10, 100), dtype='int32')
    # 构建含有分句的矩阵
    for i, review in enumerate(reviews):
        sentences = sent_tokenize(review)  #对每一条评论，分句，返回的sentences是一个分句list
        tokenized_sentences = word_tokenizer.texts_to_sequences(
            sentences
        )
        tokenized_sentences = pad_sequences(
            tokenized_sentences, maxlen=100
        )  #填充数据长度到100

        pad_size = 10 - tokenized_sentences.shape[0]

        if pad_size < 0:
            tokenized_sentences = tokenized_sentences[0:10]
        else:
            tokenized_sentences = np.pad(
                tokenized_sentences, ((0, pad_size), (0, 0)),
                mode='constant', constant_values=0
            )

        # Store this observation as the i-th observation in
        # the data matrix
        X[i] = tokenized_sentences[None, ...]

    return X