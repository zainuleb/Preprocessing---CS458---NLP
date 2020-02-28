#!/usr/bin/env python
# coding: utf-8

# In[39]:


import re
corpus=open('Movies_TV.txt').read()


# In[40]:


#Removing first line, which is unnecessary.
res=re.sub(r'Domain.*\n','',corpus)
#res


# In[41]:


#1) Read data from the dataset and separate it into 4 columns with each row as a review submitted.
rows=res.split('\n')
rows.remove(rows[-1])
necsData=[]
for data in rows:
    
    #a) Removing unwanted whitespaces
    _,_,_,review=data.split('\t')
    
    #b) Normalizing case
    necsData.append(review.lower())  #Conversion to lower case.


# In[42]:


#c) Removinig stopwords
from sklearn.feature_extraction import stop_words
stopWordsList=list(stop_words.ENGLISH_STOP_WORDS)


# In[43]:


from string import punctuation as punc
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

ps = PorterStemmer()
wl = WordNetLemmatizer()


# In[44]:


tempList=[]
stemmingList=[]
for rev in necsData:
    tempList=rev.split(" ")
    remStopWord=[word for word in tempList if word not in stopWordsList] #Removing stop words.
    remPunctuation=[word for word in remStopWord if word not in punc]


# In[45]:


tempList=[]
stemmingList=[]
finalList=[]
joinOn=" "
tempSplit=[]

for rev in necsData:
    tempList=rev.split(" ")
    remStopWord=[word for word in tempList if word not in stopWordsList] #Removing stop words.
    remPunctuation=[word for word in remStopWord if word not in punc]
    for word in remPunctuation:
        
        
        stemmingList.append(wl.lemmatize(ps.stem(word),'v')) #Stemming and lemmetizing words.
    #Joining words back toghether of the review after preprocessing techniques to make it whole.
    joinStr=joinOn.join(stemmingList)
    #List that contains reviews after the preprocessing techniques as elements.
    finalList.append(joinStr)
    stemmingList=[]


# In[46]:


#3) Find all possible unigrams, bigrams and trigrams for the first review (its computationally expensive)

from nltk import ngrams
tempStr=finalList[0] #Selecting first review
ngramsList=tempStr.split(" ") #List of words of the first review.
unigrams=list(ngrams(ngramsList,1))
bigrams=list(ngrams(ngramsList,2))
trigrams=list(ngrams(ngramsList,3))
#print("unigrams", unigrams)
#print("bigrams", bigrams)
#print("trigrams", trigrams)


# In[47]:


#4) Find the probabilities of unigrams, bigrams and trigrams.
#tempStr contains first review.

unigram_freq=[unigrams.count(x)/len(set(tempStr)) for x in unigrams]
#unigram_freq

bigram_freq=[bigrams.count(x)/ngramsList.count(x[0]) for x in bigrams]
#bigram_freq

trigram_freq=[trigrams.count(x)/bigrams.count(x[:2]) for x in trigrams]
#trigram_freq


# In[48]:


#5) Provide the following information about reivews;
emptySpace = " "
tempStr2 = emptySpace.join(finalList)

tokkenList = tempStr2.split(" ")

#a) total tokens
#len(tokkenList)

#b) Vocabulary (unique tokens) before preprocessing
#len(set(tokkenList)) 


# In[38]:


tempStr3=emptySpace.join(necsData)
uniqueTokkensAft=tempStr3.split(" ")
len(uniqueTokkensAft)
len(set(uniqueTokkensAft)) #Number of unique tokkens before processing

wordList=[]
counter=0
lengthRev=0
for rev in necsData:
    wordList=rev.split(" ") 
    lengthRev=lengthRev+len(wordList) #Total number of words in a review.
    counter=counter+1         #Total reviews


# In[49]:


#c) Average length of a review
avgLengthRev=lengthRev/counter
avgLengthRev

wordList=[]
counter=0
wordLength=0
tWords=0
avg1Rev=0
for rev in necsData:
    wordList=rev.split(" ")
    tWords=len(wordList)   #Number of words in a single review.
    counter=counter+1
    for x in wordList:
        wordLength=wordLength+len(x)

    avg1Rev=avg1Rev+(wordLength/tWords) 
    wordLength=0


# In[51]:


# d) Average length of tokens within a review
totalAvg=avg1Rev/counter
#totalAvg

