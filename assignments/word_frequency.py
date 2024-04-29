import string

def process_file(filename):
    word_hist = dict()
    fin = open(filename, encoding="utf8")
    for line in fin:
        process_line(line, word_hist)
    return word_hist


def process_line(line, word_hist):
    line = line.replace('_', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        word_hist[word] = word_hist.get(word, 0) + 1

def total_words(word_hist):
    return len(word_hist)

def word_occurences(word_hist):
    return sum(word_hist.values())

def most_common(word_hist):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in word_hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t

def main():
    word_hist = process_file('romeo and juliet.txt')
    print(f'Total number of words: {total_words(word_hist): ,}')
    print(f'Total word occurences: {word_occurences(word_hist): ,}')
    #for word in word_hist:
     #   print(word)

if __name__ == '__main__':
    main()