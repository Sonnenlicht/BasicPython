#! python3

def get_ascii_codes(words):
    encoded_words = {}
    for word in words:
        codes = []
        for letter in word:
            codes.append(ord(letter)) #converts letter to ascii

        codes = [ord(letter) for letter in word]
        encoded_words[word] = codes
        #encoded-words = {word: codes
        #                 for word in words
        #                 for letter in word}
    return encoded_words

    #return {
    #    word: [ord[c] for c in word]
    #    for word in words
    #}

words = ["hello", "bye", "yes", "no", "python"]
newdict = get_ascii_codes(words)
print(newdict)
