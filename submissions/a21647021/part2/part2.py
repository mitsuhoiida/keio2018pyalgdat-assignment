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
    data = load_pkl('data.pkl')
    #data = load_corpus_data('english-brown.txt')
    words = list(get_word_freq(data))
    dict = get_context_dictionary(data, words, 3)
    save_pkl('cd.pkl',dict)
    # YOUR ANSWERS GO HERE
    # We care about word contexts because to compare different words, it is
    # necessary to know the relative position of the word within the sentence,
    # as words that have similar functions tend to be located in similar places
    # even within different sentences. Co-occurrence happens when certain words
    # or phrases appear frequently in a certain order within the sentence. Co-
    # occurrence patterns of words provide information about how similar words
    # are, or how they are related to each other --certain words tend to appear
    # with another word often, even if they are different in parts of speech or
    # meaning.
    # -----
    return

if __name__ == "__main__":
    main()
