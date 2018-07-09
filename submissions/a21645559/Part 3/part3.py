from assignment import *

def main():
        # -----
    # 1. Load the list of 100 most frequent words from Part I.
    # 2. Load the context dictionary using the load_pkl function.
    # 3. Create a text file called top_100_sim.txt, with 100 lines, each line
    #    corresponding to a word on the same line in the top_100_list.txt file.
    #    The top_100_sim.txt file should contain a series of 100 floating point
    #    numbers in each line (10000 numbers total). The numbers should be your
    #    computed similarities to each of the words in the top_100_list.txt, in
    #    the same order. This means the diagonal numbers should all be 1.0, and
    #    a number in row i, column j should represent similarity of the ith and
    #    jth word in the top_100_list.txt loaded in step 1. You need to use your
    #    implementation of the similarity function to compute those numbers.
    # 4. Answer the question: What kind of matrix would you obtain if you
    #    computed similarity on an empty corpus (with non-empty word list), or
    #    on a non-empty corpus with words that don't appear in it? There is a
    #    name for this kind of matrix. Write it down.

     
    # Question 1

    top_100_list = load_pkl("top_100_list.pkl")

    # Question 2
    
    cd = load_pkl('cd.pkl') 

    # Question 3

    ## Creating matrix

    np.set_printoptions(threshold=np.inf)
    sim_list = list()
    for words in top_100_list:
        sim_sublist = list()
        for words2 in top_100_list:
            sim_sublist.append(similarity(cd, words, words2))
        sim_list.append(sim_sublist)
    matrix = np.matrix(sim_list)

    ## Creating txt file

    dtxt = open("top_100_sim.txt","w")
    dtxt.write(str(matrix))
    dtxt.close
    
 	# Question 4

 	## It would produce zero matrix as the words don't share common word contexts.


      

if __name__ == "__main__":
    main()
