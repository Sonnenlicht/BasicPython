#! python3

words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}

def translate(langkey):
    english = ' '
    newwords = langkey.split()
    for w in range(len(newwords)):
        for k, v in words.items():
            if(k == newwords[w]):
                english += str(v) + ' '
    return english

spanish = 'el gato esta en la casa'
english = translate(spanish)
print(english)
