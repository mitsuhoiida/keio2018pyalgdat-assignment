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
    # YOUR CODE GOES HERE

    #1
    cd = load_pkl("../data/cd.pkl")
    #2
    knng = get_knn_graph(cd,10)
    #3
    save_json("../data/knng_10.json",knng)
    #6
    # I feel like this assignment (until part.4) must be pretty basic for l
    # inguistic megascope, and part.5 must be the main topic, which was too
    # difficult to me. I enjoyed seeing results. I agree with a result that
    # shows "the" is the top word to be appeared. I personally think the use
    # for such graph of words could be used for translation, auto correct or
    # Siri. The similarity can be used in prededicted transform.

    # YOUR ANSWERS GO HERE
    # -----
    return

if __name__ == "__main__":
    main()
