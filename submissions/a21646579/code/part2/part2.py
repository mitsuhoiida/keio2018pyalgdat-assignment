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
    data1 = set()
    for centence in data:
        for word in centence:
            data1.add(word)

    data1 = list(data1)

    cd = get_context_dictionary(data, data1, 3)
    # 3
    save_pkl('cd.pkl', cd)
    # YOUR ANSWERS GO HERE
    """
    Even if we do not know the meaning of the word, we can infer the meaning by understanding the 
    circumstances of the setting of the word in the centence. 
    The context provides when,where, who, what, why, and how the centence was created
    and it provides the overall background of the centence to make the centence easier to
    understand compared to understanding each word individually. 
    """
    # -----
    return


if __name__ == "__main__":
    main()
