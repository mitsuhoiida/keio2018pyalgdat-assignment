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
    #
    # YOUR CODE GOES HERE
    with open('top_100_list.txt', 'r') as l:
        list = l.read().split()
    dict = load_pkl('cd.pkl')
    with open('top_100_sim.txt','w') as f:
        for i in list:
            for j in list:
                f.write(str(similarity(dict,i,j)) + '\t')
            f.write('\n')
    
    # YOUR ANSWERS GO HERE
    # Since the corpus is empty, the resulting matrix will compute 0.0 for all
    # calculations except for those when testing the same words, e.g.
    # similarity(dict,'word','word'), which will result in 1.0. As a result, the
    # matrix will have value 1.0 on the main diagonals and 0.0 elsewhere. This
    # type of matrix is called an identity matrix.
    # -----
    return

if __name__ == "__main__":
    main()
