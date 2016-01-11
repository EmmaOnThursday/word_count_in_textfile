# put your code here.
import sys


def count_unique_words(filename):
    """For any text file, prints dictionary of unique words and number of occurences."""

    # words = []
    dict_of_words = {}
    file_data = open(filename)
    for line in file_data: 
        line = line.rstrip()
        line = line.split()
    #     words.extend(line.split(" "))
    # file_data.close()

    # unique_words = set(words)
    # dict_of_words = {}

    # for item in unique_words: 
    #     count = words.count(item)
    #     dict_of_words[item] = count
        for word in line:
            word = word.strip('.,!?:; -"_')
            word = word.lower()
            dict_of_words[word] = 1 + dict_of_words.get(word, 0)
            # if word not in dict_of_words:
            #     dict_of_words[word] = 1
            # else:
            #     dict_of_words[word] += 1
    file_data.close()

    for key, value in dict_of_words.iteritems():
        print key, value

filename=sys.argv[1]
count_unique_words(filename)
# count_unique_words("test.txt")
