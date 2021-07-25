import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

f1 = open('/home/njeyepatch/Computer Science/Machine Learning/NLP/NLTK_practice/read.txt',encoding='utf-8')
text = f1.read()
f1.close()
lower = text.lower()
# print(lower) # made everything lower case
# print(string.punctuation) - list of all punctutations in string library
cleaned_text = lower.translate(str.maketrans('','',string.punctuation))

words = word_tokenize(cleaned_text)
final_text = []
emotion_list = []
# can also copy list of stop words from the internet and store in a list
for i in words:
    if i not in set(stopwords.words("english")):
        final_text.append(i)
# print(final_text)
f = open('/home/njeyepatch/Computer Science/Machine Learning/NLP/NLTK_practice/emotions.txt','r')
for line in f:
    clear_line = line.replace("\n",'').replace(",",'').replace("'",'')
    clear_line = clear_line.strip()
    word,emotion = clear_line.split(':')
    # print("Word : "+ word+ " "+"Emotion : "+emotion)
  
    if word in final_text:
        emotion_list.append(emotion)
f.close()  
print(emotion_list)
w = Counter(emotion_list)

# this method leads to cluttering in x axis when there are too many values - plt.bar(w.keys(),w.values())
fig,ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate() # auto tilts x axis to fit everything
plt.savefig('graph.png')
plt.show()

#for i in final_text:
   # if i in emotions:
       # final_list.append(i)
#print(final_list)