from assignment import *

def main():
    # $ python3 part3.py # in terminal
    # -----
    # 1. Load the list of 100 most frequent words from Part I.
    file_name = 'top_100_list.txt'
    f = open(file_name, 'r', encoding='utf-8')
    lines = f.readlines()
    f.close()

    # 2. Load the context dictionary using the load_pkl function.
    cd = load_pkl('cd.pkl')

    # 3. Create a text file called top_100_sim.txt, with 100 lines, each line
    #    corresponding to a word on the same line in the top_100_list.txt file.
    #    The top_100_sim.txt file should contain a series of 100 floating point
    #    numbers in each line (10000 numbers total). The numbers should be your
    #    computed similarities to each of the words in the top_100_list.txt, in
    #    the same order. This means the diagonal numbers should all be 1.0, and
    #    a number in row i, column j should represent similarity of the ith and
    #    jth word in the top_100_list.txt loaded in step 1. You need to use your
    #    implementation of the similarity function to compute those numbers.
    save_file_name = "top_100_sim.txt"
    fp = open(save_file_name, 'w')
    #print(lines)
    for w1 in lines:    #row
        for w2 in lines:    #column
            w1 = w1.replace("\n","")
            w2 = w2.replace("\n","")
            sim = similarity(cd, w1, w2)
            fp.write("%.4f " % sim)
        fp.write("\n")
    fp.close()
    # 4. Answer the question: What kind of matrix would you obtain if you
    #    computed similarity on an empty corpus (with non-empty word list), or
    #    on a non-empty corpus with words that don't appear in it? There is a
    #    name for this kind of matrix. Write it down.
    #   
    #   If a similarity matrix was computed with an empty corpus, similarity between
    #   each words will not exist beacuse the purpose of similarity calculation is to find 
    #   the co-occurrence between each words. Since the corpus is empty, the sim function will 
    #   collect 0. Non-empty corpus with words that don't appear in it also will show 0 similarity.
    #   The matrix is called Laplacian similarity matrix. 
    # 
    #
    # YOUR CODE GOES HERE
    #
    # YOUR ANSWERS GO HERE
    # -----
    return

if __name__ == "__main__":
    main()
