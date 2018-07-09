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
    # -----
    
    data = load_pkl('data.pkl')
    
    words = [*get_word_freq(data)]
    
    context_data = get_context_dictionary(data, words, 3)
    
    save_pkl('cd.pkl', context_data)

    #
    # Becasue word contexts imply semantics and syntax of words. Semantics is the
    # meaning of words. Syntax is the set of rules that governs the structure of
    # sentences in a language. 
    # -----
    return

if __name__ == "__main__":
    main()
