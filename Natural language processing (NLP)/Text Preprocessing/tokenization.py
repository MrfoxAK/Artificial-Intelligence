from faker import Faker
from nltk.tokenize import sent_tokenize,word_tokenize

# Create a Faker object
fake = Faker()

# Generate dummy text
dummy_text = fake.text()

# Sentance Tokenization
sents = sent_tokenize(dummy_text)
print(sents)


# Word Tokenization
for sent in sents:
     print(word_tokenize(sent))