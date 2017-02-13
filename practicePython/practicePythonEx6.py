myStr = raw_input("enter a word or phrase: ")

#for i in range (len(myStr)):

if myStr == myStr[::-1]:
    print "This is a palindrome"
else:
    print "This isn't a palindrome"
