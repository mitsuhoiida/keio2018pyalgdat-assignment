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
    with open('top_100_list.txt', 'r') as t:
        list = t.read().split()
    dict = load_pkl('cd.pkl')
    cd = {}
    for word in list:
        if word in dict:
            cd[word] = dict[word]
    sim_matrix, word_index = get_sim_matrix(cd)
    l = get_normalized_laplacian(sim_matrix)
    v = get_eigenvector_matrix(l,10)
    wv = get_word_vectors(v,word_index)
    with open('top_100_dist.txt', 'w') as f:
        for w1 in list:
            for w2 in list:
                f.write(str(word_distance(w1,w2,wv)) + '\t')
            f.write('\n')

    # YOUR ANSWERS GO HERE
    # I believe that finding nearest neighbors through the calculation of
    # eigenvector is generally a better method because of the difference in time
    # computation. While the knn graph of similiarty method took hours to finish
    # its computation, obtaining the similarity matrix only took less than five
    # minutes. This massive difference in result is due to the simplicity of the
    # code, as the get_knn_graph function included nested loops, while the
    # functions for the similarity matrix contained of only one loop. 
    # -----
    return

if __name__ == "__main__":
    main()
