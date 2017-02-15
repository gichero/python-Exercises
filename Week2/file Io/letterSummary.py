word = raw_input('enter a word: ')

counts = {}

for char in word:
     counts[char] = counts.get(char, 0) + 1

for char, count in counts.items():
    print "%d %s' " % (count, char)
