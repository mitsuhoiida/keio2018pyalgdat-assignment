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


    # Question 1

	def load_pkl(file_name):
	    with open(file_name, 'rb') as f:
	        data = pkl.load(f)
	    return data
	data = load_pkl('data.pkl')

	# Codes below are just for myself

	words = load_pkl('words.pkl')

	# Question 2

	contxt_dictionary = get_context_dictionary(data, words, 3)

	# Question 3

	def save_pkl(file_name, data):
	    with open(file_name, 'wb') as f:
	        pkl.dump(data, f)
	save_pkl("cd.pkl",contxt_dictionary)
    
    # Question 4
    
	## Finding out about word contexts is important because it reveals the 
	## relationship between words. Unigram features allow us to see which words 
	## tend to be used together with the specific word, thus revealing grammertical 
	## order the English language possess. Bigram features also reveal us the similar 
	## things as unigram features, however, it also takes into account of 
	## relationships between words around the specific words. In this way, words that 
	## are similar in grammertial context, such as verbs, nouns, past tense, and 
	## adjectives, can be identified. Moreover, by collecting more data, meaning of 
	## the words can also be identified because once grammertical context is identified, 
	## sentence sharing similar grammertical context can be put together and alogrithms 
	## can organize words based on it. It's also important because some combinations of 
	## words are more "natural" than the other, such as "powerful computer" rather than 
	## "strong computer",so identifying these "natural" combinations can lead to 
	## understanding about sensible structure in the language. 

if __name__ == "__main__":
    main()
