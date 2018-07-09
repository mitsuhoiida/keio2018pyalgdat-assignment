from assignment import *

def main():
    # -----
    # 1. Load the context dictionary using the load_pkl function.
    cd = load_pkl('cd.pkl')

    # 2. Compute a 10 nearest neighbors graph using your implementation of the
    #    get_knn_graph function for all the words appearing in the corpus.
    k = 10
    knng = get_knn_graph(cd, k)

    # 3. Save the graph neighbor dictionary to a file named knng_10.json using
    #    the save_json utility function.
    file_name = 'knng_10.json'
    save_json(file_name, knng)

    # 4. Use the wme JavaScript code I provided to explore the graph. Save a
    #    screenshot of a star neighborhood at the word language to a file named
    #    language.png.

    # 5. Use the wm JavaScript code I provided to generate static pictures of
    #    3n2g neighborhoods of each of the following words: green, interesting,
    #    jumped, law, sky. Save screenshots of the obtained graphs in files
    #    named green.png, interesting.png, jumped.png, law.png, sky.png.
    

    # 6. Answer the questions: How do you feel about this assignment, and the
    #    obtained results? Can you think of any use cases for such a graph of
    #    words? How about word similarity in general? What other common type of
    #    data might be a good candidate for similarity clustering based on some
    #    set of derived features (i.e. other than text)?
    #
    #   Although this assignment was a challenge, I am satisfied with the results
    #   I have obtained from the functions. In fact, I was amazed by the way how 
    #   word texts can be analyzed through the sets of computational functions. 
    #   Other than this text analysis, similarity measures can be used in the context
    #   of mapping (GPS) when it needs to navigate the fastest way to its destination. 

    # YOUR CODE GOES HERE
    #
    # YOUR ANSWERS GO HERE
    # -----
    return

if __name__ == "__main__":
    main()
