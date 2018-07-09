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

    #1
    f = open("../data/top_100_list.txt")
    top_100 = f.read()
    #2
    pkl_100 = load_pkl("../data/cd.pkl")
    #3
    top_100_list = top_100.split("\n")
    with open("../data/top_100_sim.txt", mode='w') as f:
        for w1 in top_100_list:
            for w2 in top_100_list:
                sim = similarity(pkl_100, w1,w2)
                f.write(str(sim) + " ")
            f.write("\n")
            print(top_100_list.index(w1))
    #4
    # If we compute similarity on an empty corpus with a normal corpus, then
    # there will be only 0 inside a matrix. It's called a null matrix.

    # YOUR ANSWERS GO HERE
    # -----
    return

if __name__ == "__main__":
    main()
