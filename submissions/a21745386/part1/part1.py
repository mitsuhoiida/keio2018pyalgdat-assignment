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
    save_pkl('data.pkl',data)
    wfd = get_word_freq(data)
    save_json('wfd.json', wfd)
    top100= top_k_words(wfd, 100)
    top5000=top_k_words(wfd, 5000)
    s100 = open('top_100_list.txt','w')
    s5000 = open('top_5000_list.txt','w')
    n=1
    for wr in top100:
        if n == 100:
            s100.write(wr)
        else:
            s100.write(wr +'\n')
        n= n+ 1
    for wd in top5000:
        s5000.write(wd +'\n')
    s100.close()
    s5000.close()
    graph_top_k(wfd, top100, 'top_100_fig.png')


    #
    # YOUR ANSWERS GO HERE
    # From the result, I can see words in the top of frequency ranking such as 'the', and 'of'
    # has a very high frequency of appearance. And there is a significant difference
    # between frequency of appearance with the word and words, which ranks below them.
    # The class of function describe this behavior is
    # '-log(x)'
    # The name of law is Zipf's law.
    # -----
    return

if __name__ == "__main__":
    main()
