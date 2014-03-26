""" Groups and Topics

The objective of this task is to explore the structure of the deals.txt file. 

Building on task 1, we now want to start to understand the relationships to help us understand:

1. What groups exist within the deals?
2. What topics exist within the deals?

"""
import scipy as sp
import nltk
import nltk.data
import enchant
from sklearn.feature_extraction.text import CountVectorizer

d = enchant.Dict("en_US")
vectorizer = CountVectorizer(min_df=1)
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

deals = open('../data/deals.txt','rU').read() #read deals.txt file
sent_deals = tokenizer.tokenize(deals.strip())

X = vectorizer.fit_transform(sent_deals)
num_samples, num_features = X.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))
#print(vectorizer.get_feature_names())

# T O D O : 
# - Clustering with k-means, to determine the groups (clusters)
# - Latent Dirichlet Allocation with the 'gensim' package.
# - Build a Topic model.
