from assignment import *

def main():
    # -----
    # 1. Load corpus data using your load_corpus_data function.
    # 2. Use the save_pkl utility function to save this data to a file named
    #    data.pkl
    # 3. Obtain the word frequency dictionary using your get_word_freq function.
    # 4. Use the save_json utility function to save the word frequency
    #    dictionary to a file named wfd.json
    # 5. Obtain two lists of words: top 100 and top 5000.
    # 6. Save the two lists in two files named top_100_list.txt and
    #    top_5000_list.txt respectively. Write plain text words, one word per
    #    line. You will need to write your own code for that (instead of using a
    #    function). Refer to your lecture notes or Python documentation for
    #    how to do that. The words should be ordered by decreasing frequency.
    # 7. Generate a frequency graph for the top 100 words, and use the
    #    graph_top_k function to save it to a file named top_100_fig.png
    # 8. Answer the question: What type of behavior do English words exhibit?
    #    What is the class of functions that describe such behavior? What is the
    #    name of this law in linguistics? Answers should be inside comments.
    #
    # YOUR CODE GOES HERE
    data = load_corpus_data('english-brown.txt')
    save_pkl('data.pkl', data)
    wfd = get_word_freq(data)
    save_json('wfd.json', wfd)
    top_100 = top_k_words(wfd, 100)
    top_5000 = top_k_words(wfd, 5000)
    t100 = open('top_100_list.txt', 'w')
    for word in top_100:
        t100.write(word + '\n')
    t100.close()
    t5000 = open('top_5000_list.txt', 'w')
    for word in top_5000:
        t5000.write(word + '\n')
    t5000.close()
    graph_top_k(wfd, top_100, 'top_100_fig.png')

    # YOUR ANSWERS GO HERE
    # When looking at the list of the most-frequently used words, it can be
    # observed that the most frequent word 'the' appears twice as many times as
    # the second most frequent word. This characteristic causes for the resulting
    # graph to be a rational function, the inverse function for a linear function.
    # This behaior is called a Zipf's law in linguistics.
    # -----
    return

if __name__ == "__main__":
    main()
