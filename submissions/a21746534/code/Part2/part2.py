from assignment import *

def main():
    #python3 part3.py # in terminal
    # -----
    # 1. Load corpus data using the load_pkl utility function.
    file_name = "data.pkl"
    data = load_pkl(file_name)

    # 2. Use your implementation of get_context_dictionary to obtain context
    #    data for all the words in the corpus. You need to obtain the list of
    #    all words first.

    all_list = set()
    for item in data:
        all_list = all_list | set(item)
        #print(all_list)
    all_words = list(all_list)
    k = 2
    cd = get_context_dictionary(data, all_words, k)

    # 3. Save the computed context dictionary to a file named cd.pkl using the
    #    save_pkl utility function.
    save_pkl("cd.pkl",cd)

    # 4. Answer the question: Why do we care about word contexts? What kind of
    #    information can co-occurrence patterns (contexts) of words provide?
    
    #   Contexts of the texts are important as readers can understand the meaning through 
    #   a careful examination on the co-occurrence of the words. By looking at the 
    #   concurrence of the words, readers can indicate the semantic similarity based on the 
    #   likeness of each words' meanings and consequently derive semantic relationship
    #   between each unit of words, and thus, an idea/concept. 
    #
    # YOUR CODE GOES HERE
    #
    # YOUR ANSWERS GO HERE
    # -----
    return

if __name__ == "__main__":
    main()
