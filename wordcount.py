# put your code here.
import sys
from collections import Counter 

def count_unique_words(filename):
    """For any text file, prints dictionary of unique words and number of occurences."""

    words = []
    # dict_of_words = {}
    file_data = open(filename)
    for line in file_data: 
        line = line.strip()
        line = line.split()
        for word in line:
            word = word.strip('.,!?:; -"_\n')
            word = word.lower()
            # dict_of_words[word] = 1 + dict_of_words.get(word, 0)
            if len(word) > 0:
                words.append(word)
            # if word not in dict_of_words:
            #     dict_of_words[word] = 1
            # else:
            #     dict_of_words[word] += 1
    file_data.close()
    word_counts = Counter(words)
    list_of_tuples = sorted(word_counts.items())
    sorted_by_count = sorted(list_of_tuples, key=lambda tup: tup[1], reverse=True)
    # print sorted_by_count

    for item in sorted_by_count:
        print item[0], item[1]

    # for key, value in word_counts.iteritems():
    #     print key, value

filename=sys.argv[1]
count_unique_words(filename)
