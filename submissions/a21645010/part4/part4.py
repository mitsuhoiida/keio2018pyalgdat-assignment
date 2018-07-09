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
    # 1
    cd = load_pkl('cd.pkl')

    # 2
    knng_10 = get_knn_graph(cd, 10)

    # 3
    save_json('knng_10.json', knng_10)
    #
    # YOUR ANSWERS GO HERE
    # Coding part was not really motivarting for me because I can only get rows
    # of numbers as results. But when I get the results in wn and wne, I was
    # fascinated by the results.
    # The graph of words can be utilized into study of linguistics. We may find
    # unrealized connection between words. The similarity in general can be used
    # for learning purposes. For example, google's service called "WORD COACH" 
    # asks me questions like "Which word is similar to offer, green or 
    # proposal?". I think google gets synonyms by algorithm like this 
    # assignment (but more complicated one). Getting synonyms is also useful
    # when making dictionaries.
    # Pictures, sounds, radio waves, and movies can be a good candidate for
    # similarity clustering.
    # -----
    return

if __name__ == "__main__":
    main()
