################################################################################
#                                                                              #
#                               INTRODUCTION                                   #
#                                                                              #
################################################################################

# This is the first assignment for keio2018pyalgdatself. Because this is your
# first time implementing code in Python independently, I will guide you by
# providing templates in this source code file. This file provides a general
# outline of your program. You will implement the details of various pieces of
# Python code grouped in functions. Those functions are called within the main
# function, at the end of this source file. Please refer to the lecture slides
# for the background behind this assignment. You will implement something I
# refer to as the linguistic megascope. Given an input file consisting of plain
# English corpus of literature, your task is to analyze this data in order to
# derive syntactic and semantic structure relating linguistic units on the level
# of words. The task progresses gradually, from simple token statistics, to more
# interesting features of language. The last section is a bit more
# computationally involved, so I decided to make it optional. Completing the
# extra credit section can give you extra points that can subsidize your final
# grade in the course, so I recommend doing it. However, not being able to
# complete it won't hurt your final grade in the course. The goal of this
# assignment is to obtain a form of pre-deep-learning vector space embedding
# of words. This embedding maps the words of the language to points in a
# high-dimensional real vector space. We can think of this process as converting
# the linguistic structure of the corpus into a noisy point cloud from a
# neighborhood of what I call a linguistic manifold. The shape of that manifold
# is dictated by the grammar of the language used in the corpus. By embedding
# aligned corpora from different languages (e.g. English and French), we can
# compare the differences in topologies of their corresponding manifolds to gain
# insights into linguistic phenomena. Because the ambient embedding space is a
# real vector space, it comes with a metric. This means we an measure distance
# between vectors corresponding to various words, and use it to cluster them
# into syntactic or semantic categories. If you take my course on Artificial
# Intelligence, you will see different embedding methods that can be applied on
# varying levels of granularity, ranging from letters to entire documents, as
# well as different forms of data. Such vector space embeddings allow for
# linguistically meaningful linear algebra operations, and there likely exist
# interesting subspaces of those manifolds corresponding to various grammatical
# properties of languages. I have also included some visualization tools that
# I wrote in JavaScript, which you can use to explore your results. Don't worry
# if you don't understand the specifics of the visualization code, or some of
# the mathematics involved (especially in the extra credit section). I will
# explain how to use them during lecture. Each function has instructions inside
# its docstring. To view them from a Python interpreter type
# help(name_of_function). For instance, help(w_i). You will submit a single zip
# file with everything the exercises ask you to save to the hard drive, as well
# as your completed assignment.py, part1.py, part2.py, part3.py, part4.py,
# and part5.py source code files. This is the right time to start asking TA
# questions, and involve in discussions on Slack or Piaza with your classmates.
# Good luck!

################################################################################
#                                                                              #
#                                    CODE                                      #
#                                                                              #
################################################################################

#############
#           #
#  IMPORTS  #
#           #
#############

import re
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import cosine as cs
import itertools
import pickle as pkl

###############
#             #
#  UTILITIES  #
#             #
###############

def load_pkl(file_name):
    with open(file_name, 'rb') as f:
        data = pkl.load(f)
    return data

def save_pkl(file_name, data):
    with open(file_name, 'wb') as f:
        pkl.dump(data, f)

def load_json(file_name):
    with open(file_name) as f:
        data = json.load(f)
    return data

def save_json(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)

##############################
#                            #
#  PART I: word frequencies  #
#                            #
##############################

def extract_words(sentence):
    """
    # extract_words: extract clean words from a sentence
    #
    # Input:
    # sentence - a string representing a raw sentence from the corpus
    #
    # Output:
    # words - list of lowercase words from the input sentence
    #
    # Instructions:
    # This is a utility function you will use to process the corpus. The argument
    # is any sentence from a corpus. You must tokenize it, and return a list or word
    # tokens from the sentence. This means you must strip the sentence from
    # anything that wouldn't be part of a dictionary word in English (e.g. especial
    # characters, whitespace, etc.) Single characters or numbers are not considered
    # words, and should be discarder from the result. In case of apostrophe, keep
    # only the part of the word preceding the special character.
    #
    # Hint:
    # Use regular expressions.
    #
    # Example:
    # > extract_words("Let's strip this sentence! :)")
    # > ['let', 'strip', 'this', 'sentence']
    """
    words = []

    # -----
    # YOUR CODE GOES HERE
    tokens = re.sub("[^\w]", " ", sentence.strip()).split()
    words = [w.lower() for w in tokens if len(w) > 1]
    # -----

    return words

def load_corpus_data(file_name):
    """
    # load_corpus_data: load the corpus data
    #
    # Input:
    # file_name - string representing the name of the text file containing the
    # corpus
    #
    # Output:
    # data - list of elements of the form [s_1, s_2, ...], where s_i is the ith
    # stripped sentence from the corpus
    #
    # Instructions:
    # Each s_i should be a list of words that appear in the corresponding sentence
    # of the input file. You should use your extract_words utility function above.
    #
    # Hint:
    # Opening a text file will be explained during lecture.
    """
    data = []


    # -----
    # YOUR CODE GOES HERE
    with open(file_name) as f:
        for l in f:
            data.append(extract_words(l))

    # -----

    return data

def get_word_freq(data):
    """
    # get_word_freq: generate word frequency dictionary
    #
    # Input:
    # data - list of lists of words (corpus data generated by the load_corpus_data
    # function)
    #
    # Output:
    # wfd - a dictionary where keys are words, and the values are their counts
    # within the corpus
    #
    # Instructions:
    # Add words of the corpus data as keys to the dictionary, and count how many
    # times each word appears in the data. The size of the dictionary should be
    # equal to the total number of distinct word tokens stripped from the text.
    # Each value should be an integer >= 1.
    #
    # Hint:
    # The total number of keys should be in tens of thousands.
    """
    wfd = dict()

    # -----
    # YOUR CODE GOES HERE
    for sen in data:
        for word in sen:
            if word not in wfd:
                wfd.update({word:1})
            else: wfd[word]= wfd[word] +1
    # -----

    return wfd

def top_k_words(wfd, k):
    """
    # top_k_words: obtain a list of most frequent words in the corpus
    #
    # Input:
    # wfd - word frequency dictionary
    # k - an integer
    #
    # Output:
    # top_k - a sorted list of k most frequent words in the corpus, in the
    # decreasing order of frequencies
    #
    # Instructions:
    # Generate a list of k most frequent words in the corpus data using the
    # dictionary obtained from your get_word_freq function.
    #
    # Hint:
    # There is a native sort function that works on sequence objects such as lists.
    # More details are given during the lecture.
    """
    top_k = []

    # -----
    # YOUR CODE GOES HERE
    slist = sorted(wfd.items(), key=lambda x: -x[1])
    slist = slist[:k]
    for word in slist:
        top_k.append(word[0])
    # -----

    return top_k

def graph_top_k(wfd, top_k, file_name):
    """
    # graph_top_k: generate a chart of top word frequencies
    #
    # Input:
    # wfd - word frequency dictionary
    # top_k - list of top k most frequent words
    # file_name - name of the file to save the figure
    #
    # Output:
    # None
    #
    # Instructions:
    # This function does not return output inside the program. However, it has a
    # side effect of saving a figure to a file named top_k.png. You need to enter
    # part of the code replacing the empty fs list with the sorted list (in
    # decreasing order of frequencies) of integers corresponding to corpus word
    # frequencies of the top k most frequent words. In your write-up, explain what
    # you observed based based on the produced figure.
    """
    fs = []

    # -----
    # YOUR CODE GOES HERE
    for word in top_k:
        fs.append(wfd[word])
    # -----

    fig = plt.figure(figsize=(800/192, 800/192), dpi=192)
    plt.bar(range(1, len(fs)+1), fs, figure = fig)
    plt.ylabel("frequency")
    plt.xlabel("rank")
    plt.title('Brown corpus word frequency')
    # plt.show()
    plt.tight_layout()
    plt.savefig(figure=fig, fname=file_name, pad_inches=0.5)

###########################
#                         #
#  PART II: word context  #
#                         #
###########################

def w_i(data, word, width):
    """
    # w_i: obtain unigram features
    #
    # Input:
    # data - list of lists of words (corpus data generated by the load_corpus_data
    # function)
    # word - a single string representing a word in the corpus
    # width - context window size
    #
    # Output:
    # features - a set of unigram features (set of strings)
    #
    # Instructions:
    # Go through each sentence in the corpus containing the given word, and add all
    # the words surrounding it within the width of the context to the feature set.
    # That means, for example if a word appears at position 5 in a sentence of
    # of length 10, and the width size is 3, you will add words at positions 2, 3,
    # 4, 6, 7, 8. If there are no words to the left of right of a given word
    # (beginning or end of sentence), you will add as many words as you can until
    # reaching the sentence boundary. Therefore in the above scenario, if the word
    # position was 8, you would add words at positions 5, 6, 7, 9 (notice that
    # positions are 0-indexed). This is explained in more detail during lecture.
    #
    # Example:
    # > w_i([['extract', 'unigram', 'features', 'from', 'text'], ['another', 'fake',
    # 'sentence', 'from', 'corpus', 'data']], 'from', 2)
    # > {'unigram', 'features', 'text', 'fake', 'sentence', 'corpus', 'data'}
    """
    features = set()

    # -----
    # YOUR CODE GOES HERE
    for st in data:
        if word in st:
            appear = [x for x, y in enumerate(st) if y == word]
            for loc in appear:
                if loc - width > 0:
                    con = st[loc-width:loc]+ st[loc+1:loc + width+1]
                else:
                    con = st[:loc]+ st[loc+1:loc + width+1]
                features =features.union(set(con))
    # -----

    return features

def w_ij(data, word, width):
    """
    # w_ij: obtain bigram features
    #
    # Input:
    # data - list of lists of words (corpus data generated by the load_corpus_data
    # function)
    # word - a single string representing a word in the corpus
    # width - context window size
    #
    # Output:
    # features - a set of bigram features (set tuples of strings)
    #
    # Instructions:
    # Go through each sentence in the corpus containing the given word, and add all
    # tuples of words surrounding it within the width of the context to the feature
    # set. That means, for example if a word appears at position 5 in a sentence of
    # of length 10, and the width size is 3, you will add all possible 2-element
    # subsets of words from the range of positions 2, 3, 4, 6, 7, 8. Same boundary
    # rules apply as in the unigram case. This is explained in more detail during
    # lecture.
    """
    features = set()

    # -----
    # YOUR CODE GOES HERE
    for st in data:
        if word in st:
            appear = [x for x, y in enumerate(st) if y == word]
            for loc in appear:          
                if loc -width <0:
                    around = st[:loc + width+1]
                    around = [x for x in around if x != word]
                else:
                    around = st[loc - width:loc + width+1]
                    around = [x for x in around if x != word]
                features = features.union(itertools.combinations(around,2))

    # -----

    return features

def context(data, word, width):
    """
    # context: obtain the width restricted context of a word within the corpus
    #
    # Input:
    # data - list of lists of words (corpus data generated by the load_corpus_data
    # function)
    # word - a single string representing a word in the corpus
    # width - context window size
    #
    # Output:
    # context - set of unigram and bigram features
    #
    # Instructions:
    # This function uses the w_i and w_ij functions you implemented above to derive
    # two sets of features, and then returns their union. Note that union is not
    # a set of two sets, but rather a set that contains all the elements from both
    # sets.
    """
    context = set()

    # -----
    # YOUR CODE GOES HERE
    context = set(w_ij(data, word, width)).union(set(w_i(data, word, width)))
    # -----

    return context

def get_context_dictionary(data, words, width):
    """
    # get_context_dictionary: create a dictionary with keys words, and values
    # word contexts
    #
    # Input:
    # data - list of lists of words (corpus data generated by the load_corpus_data
    # function)
    # words - a list of strings representing words in the corpus
    # width - context window size
    #
    # Output:
    # cd - a dictionary of word contexts
    #
    # Instructions:
    # Use your context function to derive contexts for all words in the the words
    # list. Return a dictionary indexed by the words, where values are context sets.
    # This might take a while, so you might find it helpful to have a counter inside
    # the main for loop and print progress status. I recommend using modular
    # arithmetic to print % complete only every k iterations, instead of after every
    # word.
    """
    cd = dict()

    # -----
    # YOUR CODE GOES HERE
    
    for word in words:
        cd.update({word:context(data, word, width)})

    # -----

    return cd

###############################
#                             #
#  PART III: word similarity  #
#                             #
###############################

def similarity(cd, w1, w2):
    """
    # similarity: compute context based similarity between two words in the corpus
    #
    # Input:
    # cd - a dictionary of word contexts
    # w1 - a string representing a word from the corpus
    # w2 - a string representing a word from the corpus
    #
    # Output:
    # sim - a floating point number in the range (0, 1)
    #
    # Instructions:
    # Use the formula from the lecture slides to compute similarity between the two
    # words, based on their corpus context. Your function should short-circuit
    # if the words are equal and return 1.0 immediately, or 0.0 if one of the
    # context sets is empty (except if the words are equal, even with empty
    # context).
    #
    # Hint:
    # The set class has useful methods to efficiently compute intersections.
    # However, you can also code this yourself with the material covered so far.
    """
    sim = 0

    # -----
    # YOUR CODE GOES HERE
    if w1 == w2:
        sim =1
    elif len(cd[w1]) ==0 or len(cd[w2]) ==0:
        sim = 0.0
    else:
        sim = 2*(len(cd[w1].intersection(cd[w2]))/float(len(cd[w1])+len(cd[w2])))
    # -----

    return sim

#########################
#                       #
#  PART IV: word graph  #
#                       #
#########################

def get_knn_graph(cd, k):
    """
    # get_knn_graph: obtain a graph of words with edges connecting each word to its
    # k nearest neighbors
    #
    # Input:
    # cd - a dictionary of word contexts
    #
    # Output:
    # knng - a dictionary with keys words, and values lists of neighbors ordered by
    # decreasing similarity
    #
    # Instructions:
    # Use your similarity function to generate a list of k most similar words, for
    # each word in the corpus context dictionary. The words within each list should
    # be ordered by decreasing similarity (i.e. the first word is the most similar).
    #
    # Hint:
    # This might take some time, so printing progress might be helpful.
    """
    knng = dict()

    # -----
    # YOUR CODE GOES HERE

    for w1 in cd:
        simdict=dict()
        for w2 in cd:
            if w1 != w2:
                simdict.update({w2:similarity(cd,w1,w2)})
            else:pass
        simdict = sorted(simdict, key=simdict.get, reverse=True)
        knng.update({w1:simdict[:k]})
       
    # -----

    return knng

##########################
#                        #
#  PART V: eigenvectors  #
#                        #
##########################

# This part is optional, for extra credit, but I recommend at least trying.

def get_sim_matrix(cd):
    """
    # get_sim_matrix: obtain a similarity matrix between words, together with index
    # mapping translating from word (string), to its row/column (integer) in the
    # matrix
    #
    # Input:
    # cd - a dictionary of word contexts
    #
    # Output:
    # sim_matrix - a numpy array representing the similarity matrix of words
    # word_index - a dictionary with keys words and values integers pointing to
    # the row/column of the matrix
    #
    # Instructions:
    # You should fill in the initialized numpy array with appropriate numbers.
    """
    sim_matrix = np.zeros((len(cd.keys()), len(cd.keys())))
    word_index = dict()

    # -----
    # YOUR CODE GOES HERE
    word_index = dict()
    rownum = 0
    length = len(cd)
    for w1 in cd:
        simlist = []
        for w2 in cd:
            sim = similarity(cd,w1,w2)
            simlist.append(sim)
        sim_matrix[rownum] = simlist
        rownum = rownum + 1
        
    word_index = dict(list(zip(cd.keys(),range(len(cd)))))
    # -----

    return (sim_matrix, word_index)

def get_normalized_laplacian(sim_matrix):
    """
    # get_normalized_laplacian: obtain a normalized Laplacian of the similarity
    # matrix
    #
    # Input:
    # sim_matrix - a numpy array representing the similarity matrix of words
    #
    # Output:
    # l - normalized Laplacian of the input matrix
    #
    # Instructions:
    # Use the formula from lecture slides to obtain the Laplacian. You can use
    # np.matmul and np.linalg.inv functions of the numpy module.
    """
    l = np.zeros(sim_matrix.shape)

    # -----
    # YOUR CODE GOES HERE
    D = l
    rownum = 0
    for row in sim_matrix:
        D[rownum,rownum]= sum(sim_matrix[rownum])*sim_matrix[rownum,rownum]
        rownum = rownum +1
    lap = D - sim_matrix
    inv = np.linalg.inv(D)
    l = np.matmul(inv, lap)
    # -----

    return l

def get_eigenvector_matrix(l, k):
    """
    # get_eigenvector_matrix: obtain a matrix composed of the first k eigenvectors
    # of the normalized Laplacian of the corpus context based word similarity matrix
    #
    # Input:
    # l - normalized Laplacian of the input matrix
    # k - an integer
    #
    # Output:
    # v - Laplacian eigenvector matrix
    #
    # Instructions:
    # You can use the np.linalg.eig method from the numpy library.
    """
    v = np.zeros((l.shape[0], k))

    # -----
    # YOUR CODE GOES HERE
    a, b = np.linalg.eig(l)
    v = b[:,:k]
    
    # -----

    return v

def get_word_vectors(v, word_index):
    """
    # get_word_vectors: obtain spectral vector space embedding of words
    #
    # Input:
    # v - Laplacian eigenvector matrix
    # word_index - a dictionary with keys words and values integers pointing to
    # the row of the eigenvector matrix v
    #
    # Output:
    # wv - a dictionary with keys words and values embedding vectors
    #
    # Instructions:
    # Generate a dictionary using the word_index, to access rows of v.
    """
    wv = dict()

    # -----
    # YOUR CODE GOES HERE
    wv = dict(list(zip(word_index.keys(),v)))
    # -----

    return wv

def word_distance(w1, w2, wv):
    """
    # word_distance: spectral word distance
    #
    # Input:
    # w1 - a word (string)
    # w2 - a word (string)
    # wv - a dictionary with keys words and values embedding vectors
    #
    # Output:
    # dist - a floating point number in the range (0, 1)
    #
    # Instructions:
    # You should use the cosine function (imported at the beginning of this file as
    # cs), to compute cosine angle similarity between the two words.
    """
    dist = 0.0

    # -----
    # YOUR CODE GOES HERE
    dist = cs(wv[w1],wv[w2])
    # -----

    return dist
