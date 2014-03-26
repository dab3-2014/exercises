""" Features

The objective of this task is to explore the corpus, deals.txt. 

The deals.txt file is a collection of deal descriptions, separated by a new line, from which 
we want to glean the following insights:

1. What is the most popular term across all the deals?
2. What is the least popular term across all the deals?
3. How many types of guitars are mentioned across all the deals?

"""
import nltk
from nltk import *
import enchant
d = enchant.Dict("en_US") # will be used to remove non-English words from search results.

f = open('../data/deals.txt','rU') #read deals.txt file
raw = f.read()
blk_list = list(['as','As','in','In','on','On','to','To','if','If','and','And','of','Of','off','Off','when','When','where','Where','the','The','at','At','for','For','a','A','with','With','your','Your','or','Or','all','All','from','From','now','Now']) # words that are not interesting to our task. 
tokens = filter(lambda x: x not in blk_list, nltk.word_tokenize(raw)) # x not in ',;_$#@!&%.:-()[]?' and <--- was removed since the removal of symbols gave exaggerated results for 3rd question.

deals = nltk.Text(tokens)

Freq = FreqDist(deals)	#Frequency table for words in deals.
pop_words = filter(lambda x: x.isalpha() and d.check(x),Freq.keys())	#filter out undesired results.
print '1. The most common word is:', pop_words[0],'\n'
print '2. The least common word is:', pop_words[-1],'\n'

index_guitar = filter(lambda x: x[1] in ['guitar','Guitar','guitars','Guitars'], enumerate(deals))
index = list(max(0,x[0]-1) for x in index_guitar) + list(max(0,x[0]-2) for x in index_guitar)	#index of guitar adjectives

# First approach: guitar_brands = ['Fender','Squier','Gibson','Epiphone','Jackson','ESP','Schecter','Dean','Ibanez', 'Carvin','Martin', 'Taylor', 'Yamaha','Takamine','Ovation','Marshall','Bassman','Vox']	#Guitar brands to be filtered out
# prec_adj = filter(lambda x: x.isalpha() and x not in guitar_brands, set(deals[i] for i in index))

# 2nd approach: There is only a finite number of Guitar types
guitar_types = ['electric','acoustic','classical','steel-string','bass','baritone','6-string','7-string','8-string','hollow-body','semi-hollow','semi-acoustic','archtop']
prec_adj = filter(lambda x: x.isalpha(), set(deals[i] for i in index))
prec_adj = map(lambda x: x.lower(), prec_adj)
### End 2nd approach

deal_guitar_types = set(guitar_types) & set(prec_adj)
print '3. There are ',len(deal_guitar_types), 'types of guitars in deals.txt, they are:',', '.join(deal_guitar_types), '\b.\n'

##### Remarks:
#1. Regarding 3rd question the code lists far too many guitar types than there really is. Several insignificant words need to be removed but I could not find the tool to do this kind of task. 2nd approach only looks for KNOWN types of guitars, much better!

#2. Performance can be improved via, more iteration, more use of built-in functions, utilizing regular expressions.
