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
    # 6. How do you feel about this assignment?
    #    I think this assignment is difficult for me because I don't know how 
    #    to improve both the accuracy and efficiency of the code. 
    #    Thank you:)
    #    Can you think of any use cases for such a graph of words? 
    #    We can use such graph for analyzing the characteristics of different languages.  
    #    How about word similarity in general? What other common type of data might 
    #    be a good candidate for similarity clustering based on some set of derived 
    #    features (i.e other than text)?
    #    Other than text, data like graphs, sounds and numbers might also be a good 
    #    candidate for similarity clustering.  
    #    
    return

if __name__ == "__main__":
    main()
