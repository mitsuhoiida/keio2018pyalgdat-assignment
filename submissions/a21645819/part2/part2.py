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
    data = load_pkl("/Users/sam/python local repository/linguistic manifold/data/data.pkl")
    words = []
    for sublist in data:
        for item in sublist:
            words.append(item)
    Unique_word_tokens = list(set(words))
    save_pkl("/Users/sam/python local repository/linguistic manifold/data/cd.pkl", get_context_dictionary(data, Unique_word_tokens, 3))
    #
    # We care about word contexts because we need to calculate context
    # similarity of words later. Co-occurrence patterns of words indicates the
    # degree of their positive correlation in the context.
    # -----
    return

if __name__ == "__main__":
    main()
