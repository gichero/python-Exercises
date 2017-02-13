# word = raw_input("enter a word: ")
#
# doubleVowels = ('aa', 'ee', 'ii', 'oo', 'uu')
# result = ''
# for v in range (len(word)):
#     twoLetters = word[v:v+2]
#
# if v in doubleVowels:
#
#     result += word[v]
#     print result
#
#     print word *3

word = raw_input("enter a word: ")


word = word.replace('aa', 'aaaaa')
word = word.replace('ee', 'eeeee')
word = word.replace('ii', 'iiiii')
word = word.replace('oo', 'ooooo')
word = word.replace('uu', 'uuuuu')

print word
