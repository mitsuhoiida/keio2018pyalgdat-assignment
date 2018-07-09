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
    # 1
    data = load_pkl('data.pkl')

    # 2
    all_vocabulary = set()
    for array in data:
        for word in array:
            all_vocabulary.add(word)

    context_dictionary = get_context_dictionary(data, all_vocabulary, 3)

    # 3
    save_pkl('cd.pkl', context_dictionary)

    # YOUR ANSWERS GO HERE
    # By comparing two words' word contexts, we can measure the similarity of
    # the words. For example, it is expected that a word 'good' and 'nice' have
    # similar usage, so they must have similar words around them  (=have similar
    # contexts.)
    # Also, same parts of speech words have similar words around them, so we can
    # categolize the part of speech with unsupervised learning.

    return

if __name__ == "__main__":
    main()
