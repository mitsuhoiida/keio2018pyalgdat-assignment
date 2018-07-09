from assignment import *

def main():
    # -----
    # 1. Load corpus data using the load_pkl utility function.
    # 2. Use your implementation of get_context_dictionary to obtain context
    #    data for all the words in the corpus. You need to obtain the list of
    #    all words first.
    # 3. Save the computed context dictionary to a file named cd.pkl using the
    #    save_pkl utility function.
    #    width = 3
    # 4. Answer the question: Why do we care about word contexts? What kind of
    #    information can co-occurrence patterns (contexts) of words provide?
    #
    # YOUR CODE GOES HERE

    #1
    data = load_pkl("../data/data.pkl")
    #2
    wfd = load_json("../data/wfd.json")
    words = wfd.keys()
    cd = get_context_dictionary(data, words, width=3)
    #3
    save_pkl("../data/cd.pkl", cd)
    #4
    # Word contexts are showing a position or a location where a word you set
    # is in the corpus. Plus, you can know how the words are used in the text.
    # This means that we can know how similar the words are by observing other
    # words surrounding an assigned word. Co-occurrence patterns may show the
    # word type of the word or an ease of use of another word with the word. By
    # using this idea, it's easy to make a good flow of sentences.

    # YOUR ANSWERS GO HERE
    # -----

    return

if __name__ == "__main__":
    main()
