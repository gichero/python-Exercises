word = raw_input("enter a word: ")

doubleVowels = ('aa', 'ee', 'ii', 'oo', 'uu')
result = ''
for v in range len(word):
    twoLetters = word[v:v+2]

if v in doubleVowels:

    result += word[v]
    print result

    print word * 3
