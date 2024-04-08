from statistics import mean, median, mode
from string import ascii_lowercase
def process_file(filename):
    words = dict()
    fin = open(filename)
    for word in fin:
        word_lengths(word, words)
    return words

def word_lengths(word, words):
    word = word.strip()
    words[word] = len(word)

def no_letter_e(words):
    count = 0
    for word in words:
        if has_no_e(word):
            count += 1
    return count
def has_no_e(word):
    if word.find('e') == -1:
        return True
    return False

def word_len_hist(words):
    hist = dict()
    for word in words:
        if len(word) <= 5:
            hist['1-5'] = hist.get('1-5', 0) + 1
        elif len(word) <= 10:
            hist['6-10'] = hist.get('6-10', 0) + 1
        elif len(word) <= 15:
            hist['11-15'] = hist.get('11-15', 0) + 1
        elif len(word) <= 20:
            hist['16-20'] = hist.get('16-20', 0) + 1
        else:
            hist['21+'] = hist.get('21+', 0) + 1
    return hist

def percentage(number, total):
    return round(100 * float(number) / float(total), 2)

def total_word_lengths(words):
    return sum(word_values(words))
def word_values(words):
    return words.values()

words = process_file('words.txt')
no_e_count = no_letter_e(words)
hist = word_len_hist(words)
print(f'Total words: {len(words):,}')
print(f'Words with no e: {no_e_count:,}; Percentage of words without e: {percentage(no_e_count, len(words))}%')
for bin in hist:
    print(bin, hist[bin], percentage(hist[bin], len(words)))

values = word_values(words)
print(f'Mean {round(mean(values), 2)}, Median {median(values)}, Mode {mode(values)}')

letter_counts = dict()
for word in words:
    for letter in ascii_lowercase:
        if word.startswith(letter):
            letter_counts[letter] = letter_counts.get(letter, 0) + 1

for letter in letter_counts:
    print(letter, letter_counts[letter])


"""
fin = open('words.txt')
total = 0
no_e_count = 0
for word in fin:
    word = word.strip()
    total += 1
    if has_no_e(word):
        no_e_count += 1
        print(word)

    #if len(word) > 20:
        #print(word)

print(f'The total number of words is {total:,}')
print(f'Total words with no letter e: {no_e_count:,}')
print(f'Percentage of words without e: {percentage(no_e_count, total)}%')
"""