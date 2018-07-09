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
    #
    with open('top_100_list.txt') as f:
        top100 = f.readlines()
        top100 = [i.strip() for i in top100]
    cdor = load_pkl('cd.pkl')
    cd = dict()
    for i in top100:
        cd.update({i:cdor[i]})
    sim_matrix, word_index = get_sim_matrix(cd)
    l = get_normalized_laplacian(sim_matrix)
    k = 10
    v = get_eigenvector_matrix(l, k)
    wv = get_word_vectors(v, word_index)
    distlist = open('top_100_dist.txt','w')
    simlist = open('top_100_simvec.txt','w')
    distlist.write('\n'.join(top100))
    distlist.close()
    n = 0
    for w1 in top100:
        sims = []
        for w2 in top100:
           sims.append(word_distance(w1, w2, wv))
        sims = [str(i).ljust(25) for i in sims]
        n = n+1
        if n == 100:
           simlist.write(' '.join(sims))
        else:
           simlist.write(' '.join(sims)+'\n')
            
    # YOUR ANSWERS GO HERE
    # I think calculating vector is the better way in general.
    # However for this particular assignment, this is not true,
    # because the data size is small.
    # -----
    return

if __name__ == "__main__":
    main()
