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
    top100 = open('top_100_list.txt').read()
    words = top100.split('\n')
    # 2

    cd = load_pkl('cd.pkl')
    cd2 = dict()
    for x in cd.keys():
        if x in words:
            values = cd[x]
            cd2[x] = values
    cd = cd2
    # 3
    sim_matrix, word_index = get_sim_matrix(cd)
    l = get_normalized_laplacian(sim_matrix)
    k = 100
    v = get_eigenvector_matrix(l, k)
    wv = get_word_vectors(v, word_index)
    word_dist = []
    for w1 in words:
        for w2 in words:
            word_dist.append(word_distance(w1, w2, wv))

    f = open('top_100_dist.txt', 'w')
    for n, i in enumerate(word_dist):
        if (n + 1) % 100 == 0:
            f.write(str(i) + "\n")
        else:
            f.write(str(i) + ",")
    f.close()

    # YOUR ANSWERS GO HERE
    # To get the spectral distance I had to get the normalized laplacian
    # for the 40,000+ individual words and when getting the matrix of (40,000+ , 40,000+),
    # I have hit an memmory error when getting 'l'.  From my own experiment,
    # I found out that for this corpus, using the similarity method
    # saves data and it is much faster to compute compared to spectral distance.
    # Thus, from reasons above, context similarity is better when obtaining nearest neighbors.
    # -----
    return


if __name__ == "__main__":
    main()
