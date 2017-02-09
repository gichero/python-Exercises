myStr = raw_input("Write something? ")

replacements = (("A", "4"), ("E", "3"), ("G", "6"), ("I", "1"), ("O", "0"), ("S", "5"), ("T", "7"))

newStr = myStr
for old, new in replacements:

    newStr = newStr.replace(old, new)

print(newStr)
