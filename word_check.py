from gettext import install
#import pip
import nltk

#nltk.download("words")
from nltk.corpus import words

#print(words.words())

# Words printed include both uppercase and lowercase words
# We want all the words to be lowercase for uniformity and easy readability

verified_words = set(word.lower() for word in words.words())
#print(verified_words)

# To check if a word exists in the verified words list

my_word = "example"

if my_word in verified_words:
    print(f"Yes, '{my_word},' is a valid English word.")
else:
    print(f"No, '{my_word},' is not a valid English word.")


