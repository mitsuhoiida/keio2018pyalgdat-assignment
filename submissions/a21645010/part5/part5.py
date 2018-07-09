from assignment import *

def main():
    # -----
    # 1. Load the list of 100 most frequent words from Part I.
    # 2. Load the context dictionary using the load_pkl function.
    # 3. Compute the spectral word embeddings for the top 100 words.
    # 3. Create a text file called top_100_dist.txt, with 100 lines, each line
    #    corresponding to a word on the same line in the top_100_list.txt file.
    #    The top_100_sim.txt file should contain a series of 100 floating point
    #    numbers in each line (10000 numbers total). The numbers should be your
    #    computed spectral distances to each of the words in the
    #    top_100_list.txt. This means the diagonal numbers should all be 0.0,
    #    and a number in row i, column j should represent the distance from the
    #    ith to the jth word in the top_100_list.txt loaded in step 1. Use your
    #    Use your implementation of the word_distance function.
    # 4. Answer the question: Which method of finding nearest neighbors do you
    #    suspect might be better in general (context similarity of spectral
    #    distance)? Why? Why do you think the results in this particular
    #    exercise might favor the similarity method (think data size used).
    #
    # YOUR CODE GOES HERE
    # 1
    with open('/Users/kasab/Documents/School/python/hw/keio2018pyalgdat-master/\
assignment/code/top_100_list.txt') as f:
        frequent_100 = f.read()
        frequent_100 = frequent_100.split()
    # 2
    cd = load_pkl('cd.pkl')

    # 3
    cd100 = dict()
    for word in frequent_100:
        cd100[word] = cd[word]

    cd = cd100
    simmat, word_index = get_sim_matrix(cd)
    normalized_laplacian = get_normalized_laplacian(simmat)
    eigenvector_matrix = get_eigenvector_matrix(normalized_laplacian, 3)
    wv = get_word_vectors(eigenvector_matrix, word_index)

    
    f = open('top_100_dist.txt', 'w')
    for vocabulary in frequent_100:
        for another_vocabulary in frequent_100:
            if vocabulary == another_vocabulary:
                f.write('0.0, ')
            else:
                wd_comma = str(word_distance(vocabulary, another_vocabulary,\
 wv)) + ', '
                f.write(wd_comma)
        f.write('\n')
    f.close()

    return

    # YOUR ANSWERS GO HERE
    # Using spectral distance is better. Since we have 100 dimensions, it is
    # less likely to have high cosine similarity if two words' semantics are
    # different.
    # However, in this case, using similarity method may work better because
    # data size is very large and it takes too much time to compute if we use
    # spectral distance.
    # -----

if __name__ == "__main__":
    main()
