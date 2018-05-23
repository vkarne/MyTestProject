# Contents of the File word count

from collections import Counter

with open('/home/vkarne/Documents/testdata/TestWordCount.txt', 'r') as f:
    p = f.read()  # p contains contents of entire file
    # logic to compute word counts follows here...

    words = p.split()

    wordCount = len(words)
    print("\nThe total word count is:", wordCount, '\n')

    c = Counter(words)
    for w, count in c.most_common():
        print(w, count)
