import nltk
import numpy as np
import re

filteredStory= []
with open("shortStory", "r") as f:
    sentences = nltk.sent_tokenize(f.read())
    for sent in range(len(sentences)):
        sentences[sent] = re.sub(r"[\d]", "", sentences[sent])
        filteredStory.append(sentences[sent] + "\n")
    print(filteredStory)

# print(story)
# with open("shortStory", "a") as f:
