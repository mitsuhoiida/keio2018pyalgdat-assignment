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
    data = load_pkl("data.pkl")
    words = set(itertools.chain.from_iterable(data))
    width = 3
    cd= get_context_dictionary(data, words, width)
    save_pkl('cd.pkl', cd)

    #
    # YOUR ANSWERS GO HERE
    # It is because context is necessary for computer to learn meaning, grammar, and usage of each word.
    # Co-occurrence patterns of word can provide information about the meaning of words. (sementics)
    #
    #-----
    return

if __name__ == "__main__":
    main()
