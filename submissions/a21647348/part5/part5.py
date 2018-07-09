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
    #    ith to the jth word in the top_100_list.txt loaded in step 1.
    #    Use your implementation of the word_distance function.
    # 4. Answer the question: Which method of finding nearest neighbors do you
    #    suspect might be better in general (context similarity or spectral
    #    distance)? Why? Why do you think the results in this particular
    #    exercise might favor the similarity method (think data size used).
    #
    with open('top_100_list.txt') as f:
        top_100_list = f.read().replace('\n',' ').split()
    all_dict = load_pkl('cd.pkl')

    cd = {}
    
    for word in top_100_list:
        cd[word] = all_dict[word]
    
    sim_matrix, word_index = get_sim_matrix(cd)

    
    l = get_normalized_laplacian(sim_matrix)

    
    v = get_eigenvector_matrix(l, 10)
    
    wv = get_word_vectors(v, word_index)

    
    with open ('top_100_dist.txt', "w+") as ff:
        for w1 in cd:
            for w2 in cd:
                ff.write(str(word_distance(w1, w2, wv)) + ' ')
            ff.write('\n')
    #
    # In general, I suspect that context similarity is the better way to find
    # context data. Because this method computes all words' similarity to each other, 
    # it gives more accurate similarity result.
    # 
    # However, in this particular exercise, spectral distance is the better way,
    # because there are about 50,000 words in the corpus data and it takes too
    # much time and memory to compute context data. By taking the first k eigenvectors,
    # we can take the projection and reduce the dimensions, so that we can compute
    # cosine distance between words. Although this method may not be as accurate as context
    # dictionary, the computation time will be reduced sigfinicantly. 
    # 
    #
    # -----
    return

if __name__ == "__main__":
    main()
