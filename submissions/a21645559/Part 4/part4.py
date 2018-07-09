from assignment import *

def main():
    # -----
    # 1. Load the context dictionary using the load_pkl function.
    # 2. Compute a 10 nearest neighbors graph using your implementation of the
    #    get_knn_graph function for all the words appearing in the corpus.
    # 3. Save the graph neighbor dictionary to a file named knng_10.json using
    #    the save_json utility function.
    # 4. Use the wne JavaScript code I provided to explore the graph. Save a
    #    screenshot of a star neighborhood at the word language to a file named
    #    language.png.
    # 5. Use the wn JavaScript code I provided to generate static pictures of
    #    3n2g neighborhoods of each of the following words: green, interesting,
    #    jumped, law, sky. Save screenshots of the obtained graphs in files
    #    named green.png, interesting.png, jumped.png, law.png, sky.png.
    # 6. Answer the questions: How do you feel about this assignment, and the
    #    obtained results? Can you think of any use cases for such a graph of
    #    words? How about word similarity in general? What other common type of
    #    data might be a good candidate for similarity clustering based on some
    #    set of derived features (i.e. other than text)?


    # Question 1

    cd = load_pkl("cd.pkl")

    # Question 2

    cd_10_nearest = get_knn_graph(cd, 10)

    # Question 3
    
    save_json("knng_10.json", cd_10_nearest)
    
    # Question 4 & 5

    ## No code for this question.

    # Question 6 

    ## This assignment was hard for me because I suffered with writing codes efficiently. 
    ## I will make efforts on trying to improve this. 
    ##
    ## I feel the obtained result still does not make sense completely, probably because the 
    ## data is not large enough. However, we still can see some sensible result, in 
    ## language.png where language and sentence is connected for example. It feels amazing 
    ## that the structure of language can be identified from just loading the text corpus. 
    ##
    ## One way I would use this graph of words is for language learners because sometimes 
    ## it is more efficient to learn relationships between words than memorizing the 
    ## definitions. Learners can just explore neighbors of words. Learners will also be able 
    ## to guess meaning of the words by understanding structures of any sentence, which is an 
    ## important skill when they are still learning the new languages. It might be interesting 
    ## to put graph of words as a feature in dictionary. 
    ##
    ## For word similarity, I think it would be interesting if similarity value 
    ## can be used to turn sentences, involving advanced terminologies, into sentences with 
    ## less advanced terminologies. To decide the word, occurence of the word can be 
    ## considered because people use words that are simpler more, thus more the occurence 
    ## easier the word. With this method, I think it would be easier to share more ideas 
    ## between people.
    ##
    ## The good candidate for similarity clusterting might be a chess strategy. Each step 
    ## can be put into a word, and similarity of strategy can be obtained from set of 
    ## steps players make. This data will help human players to improve their skill of 
    ## playing chess because if similarity of 2 startegies is high and a player is losing, 
    ## they can do something to improve it. 

    return

if __name__ == "__main__":
    main()
