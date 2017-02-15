secret = raw_input("Enter a string? ")
offset = 13
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ''

for char in secret:
    if char == ' ':
        newChar = ' '
    else:

        idx = alphabet.find(char)
        newIdx = idx + offset
        if newIdx > 25:
            newIdx = newIdx - 26
        newChar = alphabet[newIdx]
        result += newChar

    print result
