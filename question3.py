import string

def word_frequency(sentence):
    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", string.punctuation)
    sentence = sentence.translate(translator).lower()

    # Count the frequency of each word
    words = sentence.split()
    frequency_dict = {}

    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    return frequency_dict

# Sample input
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
