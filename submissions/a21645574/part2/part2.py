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

    
    data = load_corpus_data('english-brown.txt')
    words = []
    with open('english-brown.txt', 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word.lower())
    print(words)
    wait = input("write continue")
    width = 3
    cd = get_context_dictionary(data, words, width)
    save_pkl('cd.pkl', cd)
    # YOUR ANSWERS GO HERE
    # The word context includes all the intersections of all the words, 
    # and the co-ocurrence patters of words can be used to calculate the frequency of occurance of words.
   
    return


if __name__ == "__main__":
    main()
