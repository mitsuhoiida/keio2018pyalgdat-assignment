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
    dict = load_pkl('cd.pkl')
    knng = get_knn_graph(dict,10)
    save_json('knng_10.json',knng)

    # YOUR ANSWERS GO HERE
    # After running the program, I was surprised of how accurate the results were.
    # For example, when generating the closest words with the word 'jumped,' it
    # gave back words that were just verbs, but they were also verbs with past
    # tense. A possible use case for these results is that it can be applied to
    # search engines, because it can suggest the users possible search topics with
    # the obtained search results/history.
    # Another good candidate for similarity clustering might be with DNA data,
    # as we can compare how much one set of DNA is simliar to anthor set of DNA,
    # so that we can compare which organisms or individuals are similart to each
    # other. In addition, similarity clustering can also be applied to marketing.
    # Through people's purchasing data, we can analyze what products are similar,
    # in the sense of product type, brand, price range, etc. After products are
    # clustered through similarity, we can analyze the characteristics of customers
    # who buy the same or similar product. From this information, we can target
    # marketing specifically to those potential customers to buy new products.
    # -----
    return

if __name__ == "__main__":
    main()
