import nltk
import numpy as np
import networkx as nx


def form_sentences(text):
    article = text.split(". ")
    for sentence in article:
        yield sentence.replace("[^a-zA-Z]", " ").split(" ")


def sentence_similarity(sentence_one, sentence_two, stop_words):
    sentence_one = [word.lower() for word in sentence_one]
    sentence_two = [word.lower() for word in sentence_two]

    unique_words = list(set(sentence_one + sentence_two))

    vector_one = [0 for _ in range(len(unique_words))]
    vector_two = vector_one[:]

    for word in sentence_one:
        if word in stop_words:
            continue
        vector_one[unique_words.index(word)] += 1

    for word in sentence_two:
        if word in stop_words:
            continue
        vector_two[unique_words.index(word)] += 1

    return 1 - nltk.cluster.util.cosine_distance(vector_one, vector_two)


def build_similarity_matrix(sentences, stop_words):
    sentence_length = len(sentences)
    similarity_matrix = np.zeros([sentence_length for _ in range(2)])
    for y in range(sentence_length):
        for x in range(sentence_length):
            if y == x:
                continue
            similarity_matrix[y][x] = sentence_similarity(sentences[y], sentences[x], stop_words)
    return similarity_matrix


def generate_summary(text):
    nltk.download("stopwords")
    stop_words = nltk.corpus.stopwords.words("english")
    summarize_text = []
    sentences = [sentence for sentence in form_sentences(text)]
    scores = nx.pagerank(nx.from_numpy_array(build_similarity_matrix(sentences, stop_words)))
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summarize_text.append(" ".join(ranked_sentence[0][1]))
    return ". ".join(summarize_text)
