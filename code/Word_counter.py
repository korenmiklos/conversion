#!/usr/bin/env python
# coding: utf-8

def words(text):
    list_of_words = []
    for word in text.split():
        list_of_words.append(word.lower())
    return list_of_words

def word_count(words):
    counter = {}
    for word in words:
        if word in counter:
            # print('Increment:', word)
            counter[word] = counter[word] + 1
        else:
            # print('First time:', word)
            counter[word] = 1
        # print(counter)
    return counter

def read_text(filename):
    with open(filename, 'rt', encoding='latin1') as textfile:
        print('I am inside with:')
        data = textfile.read()
    print('I am now outside, file is closed.')
    return data

# .csv file looks like:
# ```
# word,count
# sea,36
# man,218
# ```
def write_csv(filename, counter):
    with open(filename, 'wt') as textfile:
        textfile.write('word,count\n')
        for word in counter:
            textfile.write(word + ',' + str(counter[word]) + '\n')
    print('Outside the "with", file is closed.')


old_man_and_the_sea = read_text('../data/raw/gutenberg/hemingway.txt')
list_of_words = words(old_man_and_the_sea)
counter = word_count(list_of_words)
write_csv('../data/derived/hemingway.csv', counter)
