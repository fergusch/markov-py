import random

def build_model(sentences):
    """Builds a markov chain based on the given input. 
    sentences: array of strings"""
    wordbank = {None: {}}
    for sentence in sentences:
        words = sentence.split(" ")
        words.insert(0, None)
        words.append(None)
        for i, word in enumerate(words[:-1]):
            if word not in wordbank:
                wordbank[word] = {}
            if words[i+1] not in wordbank[word]:
                wordbank[word][words[i+1]] = 1
            else:
                wordbank[word][words[i+1]] += 1
    return wordbank

def pick_words(totals):
    """Given the outcomes of a specific word, 
    chooses a random word."""
    words = list(totals.keys())
    n = sum([totals[word] for word in words])
    weights = [totals[word]/n for word in words]
    return random.choices(population=words, weights=weights)[0]

def write_sentences(n, model, punctuate=False):
    """Writes n sentences using the given model."""
    sentences = []
    for i in range(n):
        last_word = pick_words(model[None])
        sentence = last_word
        while True:
            last_word = pick_words(model[last_word])
            if last_word is None:
                break
            sentence += " " + last_word
        if punctuate:
            sentences.append(sentence + ".")
        else:
            sentences.append(sentence)
    return sentences
