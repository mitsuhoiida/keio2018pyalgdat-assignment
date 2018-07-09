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

    #1
    with open('../data/top_100_list.txt') as f:
        top100 = f.readlines()
        top100 = [i.strip() for i in top100]
    #2
    cdor = load_pkl('../data/cd.pkl')
    cd = dict()
    #3
    for i in top100:
        cd.update({i:cdor[i]})
    sim_matrix, word_index = get_sim_matrix(cd)
    l = get_normalized_laplacian(sim_matrix)
    k = 10
    v = get_eigenvector_matrix(l, k)
    wv = get_word_vectors(v, word_index)
    distlist = open('../data/top_100_dist.txt','w')
    simlist = open('../data/top_100_simvec.txt','w')
    #simvec = sim
    for w1 in wv:
        sims = []
        distlist.write(w1+'\n')
        for w2 in wv:
           sims.append(word_distance(w1, w2, wv))
        sims = [str(i).ljust(25) for i in sims]
        simlist.write(' '.join(sims)+'\n')
    #4
    # Observing vectos is a better way for me. Because of the small data size,
    # it is easy to compute.

    # YOUR ANSWERS GO HERE
    # -----
    return

if __name__ == "__main__":
    main()
