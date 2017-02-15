

import pickle

phoneBookDict = {}

try:
    myFile = open('phonebook.pickle', 'r')
    phoneBookDict = pickle.load(myFile)
    myFile.close()
    print 'Restored phone book data.'
except IOError:
    print 'No phone book data restored.'



    print """
        Electronic Phone Book
        =====================
        1. Look up an entry:
        2. Set up an entry:
        3. Delete an entry:
        4. List all entries:
        5. Quit
        """
while True:
    choice = int(raw_input("What do you want to do(1 - 5)? "))
    if choice == 1:
        name = raw_input('Enter Name: ')
        phone = phoneBookDict.get(name, 'not listed')
        print "%s's number is: %s" % (name, phone)

    elif choice == 2:
        name = raw_input('Enter Name: ')
        phone = raw_input('Enter Phone Number: ')
        if name in phoneBookDict:
            prompt = "%s is already in phone book, do you want to overwrite it? (Yes or No)" % name
            answer = raw_input(prompt)
            if answer == 'y':
                phoneBookDict[name] = phone
        else:
            phoneBookDict[name] = phone

    elif choice == 3:
        name = raw_input('Name? ')
        del phoneBookDict[name]

    elif choice == 4:
        for entry in phoneBookDict.items():
            print "%s's number is: %s" % entry

    elif choice == 5:
        myFile = open('phonebook.pickle', 'w')
        pickle.dump(phoneBookDict, myFile)
        myFile.close()
        print 'Phonebook saved'
        break
