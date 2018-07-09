from assignment import *

def main():
    # -----
    # 1. Load corpus data using the load_pkl utility function.
    # 2. Use your implementation of get_context_dictionary to obtain context
    #    data for all the words in the corpus. You need to obtain the list of
    #    all words first.
    # 3. Save the computed context dictionary to a file named cd.pkl using the
    #    save_pkl utility function.
    # 4. Answer the question: Why do we care about word contexts? What kind of
    #    information can co-occurrence patterns (contexts) of words provide?
    #
    # YOUR CODE GOES HERE

    data = load_pkl("../data/data.pkl")
    wfd = load_json("../data/wfd.json")
    words = wfd.keys()
    cd = get_context_dictionary(data, words, width=3)
    save_pkl("../data/cd.pkl", cd)


    # YOUR ANSWERS GO HERE
    # We care about the word contexts because it is important to be able to
    # extract the words that we actually need from the set of text/datasself.
    # Co-occurrance patterns of the words gives us the information, such as what 
    # does the text talks about, and the important point that is repeatedly stated
    #
    # -----
    return

if __name__ == "__main__":
    main()
