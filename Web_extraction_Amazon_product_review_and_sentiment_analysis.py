# Web scrapping for Amazon Product and Sentiment analysis


import requests   # Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 

boat_reviews=['']

### Extracting reviews from Amazon website ################
for i in range(1,10):
  al=[]  
  url="https://www.amazon.in/gp/product-reviews/B07JLFK74H/ref=cm_cr_arp_d_paging_btm_next_2?pageNumber="+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.find_all("span",{"class" : "a-size-base review-text review-text-content"})# Extracting the content under specific tags  
  for i in range(len(reviews)):
    al.append(reviews[i].text)  
  boat_reviews=boat_reviews+al  # adding the reviews of one page to empty list which in future contains all the reviews

# writng reviews in a text file 
with open("boat.txt","w",encoding='utf8') as output:
    output.write(str(boat_reviews))
    

import nltk
import re    
# Sentiment Analysis
# Joinining all the reviews into single paragraph 
boat_rev_string = " ".join(boat_reviews)



# Removing unwanted symbols incase if exists
boat_rev_string = re.sub("[^A-Za-z" "]+"," ",boat_rev_string).lower()
boat_rev_string = re.sub("[0-9" "]+"," ",boat_rev_string)



# words that contained in boat 7 reviews
boat_reviews_words = boat_rev_string.split(" ")

from nltk.corpus import stopwords
stop_words = stopwords.words('english')

with open("stop.txt","r") as sw:
    stopwords = sw.read()

stopwords = stopwords.split("\n")




boat_reviews_words = [w for w in boat_reviews_words if not w in stopwords]


# Joinining all the reviews into single paragraph 
boat_rev_string = " ".join(boat_reviews_words)

# WordCloud can be performed on the string inputs. That is the reason we have combined 
# entire reviews into single paragraph
# Simple word cloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud

wordcloud_boat = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(boat_rev_string)

plt.imshow(wordcloud_boat)

# positive words # Choose the path for +ve words stored in system
with open("positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")
  
poswords = poswords[36:]



# negative words  Choose path for -ve words stored in system
with open("negative-words.txt","r") as neg:
  negwords = neg.read().split("\n")

negwords = negwords[37:]

# negative word cloud
# Choosing the only words which are present in negwords
boat_neg_in_neg = " ".join ([w for w in boat_reviews_words if w in negwords])

wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(boat_neg_in_neg)

plt.imshow(wordcloud_neg_in_neg)

# Positive word cloud
# Choosing the only words which are present in positive words
boat_pos_in_pos = " ".join ([w for w in boat_reviews_words if w in poswords])
wordcloud_pos_in_pos = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(boat_pos_in_pos)

plt.imshow(wordcloud_pos_in_pos)

nltk 

# Unique words 
boat_unique_words = list(set(" ".join(boat_reviews).split(" ")))
