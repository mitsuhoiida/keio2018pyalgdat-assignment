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
    # 6. Answer the qudestions: How do you feel about this assignment, and the
    #    obtained results? Can you think of any use cases for such a graph of
    #    words? How about word similarity in general? What other common type of
    #    data might be a good candidate for similarity clustering based on some
    #    set of derived features (i.e. other than text)?
    #
    # YOUR CODE GOES HERE
    # 1
    cd = load_pkl('cd.pkl')
    # 2
    neighbors = get_knn_graph(cd, 10)
    # 3
    save_json('knng_10.json', neighbors)

    # YOUR ANSWERS GO HERE
    # Before tackling this assignment I have never thought about distances of words in a centence.
    # And calculating the simularities between words in a centence was a fresh expericence. 
    # However, the results returned from my code for the assignment is very perplexed.
    # For example, the high frequency of proper nouns neighboring with vague nouns and verbs such as
    # 'nilsen' neighboring with 'green' and 'carolina' neighboring with 'jumped-kill'. 
    # It is hard to imagine that nouns such as these will pop up that frequently in english.
    # Thus, I may have misinterpreted the assignment and wrote wrong code somewhere.
    # I think one of the places to impliment the word neighbors obtained from this assignment is
    # for sentiment analysis dictionaries. sentiment analysis dictionaries are used to quantify sentiments
    # of a word in a centence. So, by understanding what kind of words are combined when used, 
    # the dictinary can become more detailed since it can list not only individual words but the context of the word in the centence.
    # I believe similarity clustring can be applied to location data too. 
    # If we can obtain coordinates of where people have been using GPS, then 
    # we can get the similarites of the coordinates for each individual and 
    # predict an individual's behavior based on people who have similar data.
    # -----
    return


if __name__ == "__main__":
    main()
