from assignment import *

def main():
    # -----
    # 1. Load corpus data using your load_corpus_data function.
    file_name = "english-brown.txt"
    data = load_corpus_data(file_name)

    # 2. Use the save_pkl utility function to save this data to a file named
    #    data.pkl
    save_pkl('data.pkl', data)

    # 3. Obtain the word frequency dictionary using your get_word_freq function.
    wfd = get_word_freq(data)

    # 4. Use the save_json utility function to save the word frequency
    #    dictionary to a file named wfd.json
    json_fname = "wfd.json"
    save_json(json_fname, wfd)

    # 5. Obtain two lists of words: top 100 and top 5000.
    top_100 = top_k_words(wfd,100)
    top_5000 = top_k_words(wfd,5000)
    #print(top_100)

    # 6. Save the two lists in two files named top_100_list.txt and
    #    top_5000_list.txt respectively. Write plain text words, one word per
    #    line. You will need to write your own code for that (instead of using a
    #    function). Refer to your lecture notes or Python documentation for
    #    how to do that. The words should be ordered by decreasing frequency.

    fp = open('top_100_list.txt', 'w')
    for item in top_100:
        fp.write("%s\n" % item)
    fp.close()
    fp = open('top_5000_list.txt', 'w')
    for item in top_5000:
        fp.write("%s\n" % item)
    fp.close()

    # 7. Generate a frequency graph for the top 100 words, and use the
    #    graph_top_k function to save it to a file named top_100_fig.png
    #print("wfd:", wfd)
    #print("top_100:", top_100)
    graph_top_k(wfd, top_100, 'top_100_fig.png')

    # 8. Answer the question: What type of behavior do English words exhibit?
    #    What is the class of functions that describe such behavior? What is the
    #    name of this law in linguistics? Answers should be inside comments.
    
    #   By looking at the graph derived from the code, it is apparent that there are words 
    # 	that appear more then any other words. The most frequent words appear to be grammars, 
    # 	which are the words, that connect the other words, for instance, the nouns. 
    # 	Such structure of the sentences exhibited in the text is revealed through the function
    # 	get_word_freq and correlates the law of generative grammar. The generative grammar theory
    # 	explains grammar as a system of rules that connect combinations of words to form a sentence
    # 	and such behavior is shown with our text. 
   
    return

if __name__ == "__main__":
    main()
