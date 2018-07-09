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


    # Question 1

	data = load_corpus_data('english_brown.txt')

	# Question 2

	def save_pkl(file_name, data):
	    with open(file_name, 'wb') as f:
	        pkl.dump(data, f)
	save_pkl("data.pkl",data)

	# Question 3

	wfd = get_word_freq(data)

	# Question 4

	def save_json(file_name, data):
	    with open(file_name, 'w') as f:
	        json.dump(data, f)
	save_json("wfd.json", wfd)

	# Question 5

	top_100words = top_k_words(wfd, 100)
	top_5000words = top_k_words(wfd, 5000)

	# Question 6

	dtxt = open("top_100_list.txt","w")
	dtxt.write(str(top_100words))
	dtxt.close

	dtxt = open("top_5000_list.txt","w")
	dtxt.write(str(top_5000words))
	dtxt.close	

	# Question 7

	graph_top_k(wfd, 100, 'top_100_fig.png')

	# Codes below are just for myself

	def data_flat(data_func):
	    flat_list = []
	    for sublist in data_func:
	        for item in sublist:
	            flat_list.append(item)
	    return flat_list   
	words = data_flat(data)

	def save_pkl(file_name, data):
	    with open(file_name, 'wb') as f:
	        pkl.dump(data, f)
	save_pkl("words.pkl",words)
	save_pkl("top_100_list.pkl",top_100words)
	return
    
    # Question 8

    ## English words exihibit exponential increase in frequency of the words 
    ## being used, as the ranking of the words based on their occurence decrease 
    ## (to 1). This means that certain words are more important in communication, 
    ## and people tend to overuse them over the other words at least in English. 
    ## Hence, I think this is an exponential function, which describe the behavior. 
    ## This phenomena can be explained by Zipf's law, which states that when taking 
    ## logarithmic numbers of rankings and frequency of the words, frequency 
    ## increases when raking decreases (to 1), and the slope of the curve 
    ## representing this negative relationship is -1. 


if __name__ == "__main__":
    main()
