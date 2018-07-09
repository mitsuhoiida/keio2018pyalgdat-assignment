from assignment import *

def main():
    # -----
    # 1. Load the context dictionary using the load_pkl function.
    # 2. Compute a 10 nearest neighbors graph using your implementation of the
    #    get_knn_graph function for all the words appearing in the corpus.
    # 3. Save the graph neighbor dictionary to a file named knng_10.json using
    #    the save_json utility function.
    # 4. Use the wne JavaScript code I provided to explore the graph. Save a
    #    screenshot of a star neighborhood at the word language to a file named
    #    language.png.
    # 5. Use the wn JavaScript code I provided to generate static pictures of
    #    3n2g neighborhoods of each of the following words: green, interesting,
    #    jumped, law, sky. Save screenshots of the obtained graphs in files
    #    named green.png, interesting.png, jumped.png, law.png, sky.png.
    # 6. Answer the questions: How do you feel about this assignment, and the
    #    obtained results? Can you think of any use cases for such a graph of
    #    words? How about word similarity in general? What other common type of
    #    data might be a good candidate for similarity clustering based on some
    #    set of derived features (i.e. other than text)?
    #
    cd = load_pkl('cd.pkl')
    knng = get_knn_graph(cd, 10)
    save_json('knng_10.json', knng)
    # YOUR ANSWERS GO HERE
    # How do you feel about this assignment, and theobtained results? 
    # This assignment is difficult for a beginner to complete it, and the text file that we
    # are required to use is too big. Therefore, if there is any error in the code, it takes time 
    # to notice it and change it. For the efficiency problem, we are not able to accelerate the code, 
    # since finishing it correctly is already difficult for us. 
    # For the assignment, I am sorry that the cd.pkl that I use for part 3 and part 4 is not the exact 
    # output of the current code, since I can the code in the previous part when I am doing part3, but 
    # I don't have enough time to run part2.py again.
    # 
    # Can you think of any use cases for such a graph of words? 
    # We can use the structure to distingusish the charactistic of individual language.
    #
    # How about word similarity in general? What other common type of data might be a good candidate for similarity 
    # clustering based on some set of derived features (i.e. other than text)?
    # For the similarity of words, we can use in translation of a language or maybe in using the whole language 
    # learning process, it is efficicent to learn the words with the similer meaning at one time. 
    # 
    # For other usage of similarity clustering, we can use it in analyzing the frequency related word that 
    # peopple search in google or yahoo and people type in their social media account.
    # It is possible to know what do each individual cares about and what they are interested in.
    # If we are at the company side, we can target potential consumer groups for the specific market with their needs and demands. 
    # 
    #  

    return

if __name__ == "__main__":
    main()
