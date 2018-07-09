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
    # 1
    data = load_corpus_data('../data/english-brown.txt')
    # 2
    save_pkl('data.pkl', data)
    # 3
    wfd = get_word_freq(data)
    # 4
    save_json('wfd.json', wfd)
    # 5
    top100 = top_k_words(wfd, 100)
    top5000 = top_k_words(wfd, 5000)
    # 6
    testfile = open('top_100_list.txt', 'w')
    for item in top100:
        testfile.write("%s\n" % item)

    testfile = open('top_5000_list.txt', 'w')
    for item in top5000:
        testfile.write("%s\n" % item)

    # 7
    graph_top_k(wfd, top100, 'top_100_fig.png')
    # YOUR ANSWERS GO HERE
    """
    I found that the word 'the', was by far the most frequent word used in the english.
    The word 'the' is a definite aritcle used to refer to specific or particular nouns. 
    'The' signals that the noun is definate or that it refers to a particular member of a 
    group. This is because the rule of English grammer require that a noun must come after a 
    determiner(e.g. my, the), to clarify what the referent of the noun phrase is. After 'the',prepositions
    like 'of' follow. and the graph top_100_fig.PNG looks like it is has a Pareto distribution. 

    From wikipedia, I found Zipf's law. This law states that given some corpus of natural language utternace, the frequency of any word is
    inversely proportional to its rank in the frequency tabel. This is conform with the results from 
    the brown-english corpus.
    """
    # -----
    return


if __name__ == "__main__":
    main()
