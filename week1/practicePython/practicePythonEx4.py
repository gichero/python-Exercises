num = int(raw_input("enter a number: "))

newList = list(range(1,num+1))

divisorList = []

for number in newList:

    if num % number == 0:
        divisorList.append(number)
print(divisorList)

    #for x in num:
    #newList.append(x)
#print newList



#num = int(input("Please choose a number to divide: "))

#listRange = list(range(1,num+1))

#divisorList = []

#for number in listRange:
#    if num % number == 0:
#        divisorList.append(number)

# print(divisorList)
# view raw
