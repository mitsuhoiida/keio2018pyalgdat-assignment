from assignment import *


data = load_pkl("/Users/sam/python local repository/linguistic manifold/data/data.pkl")
wfd = get_word_freq(data)
top_100_list = top_k_words(wfd, 100)
cd = load_pkl("/Users/sam/python local repository/linguistic manifold/data/cd.pkl")
cd = {k:cd[k] for k in top_100_list if k in top_100_list}
print(cd.keys())
