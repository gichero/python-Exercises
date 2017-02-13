
fileName = raw_input('Enter a file name: ')

def fileWrite(fileName):

    myFile = open(fileName, 'w')

    fileContent = myFile.write('the path of the righteous man is beset')

    print fileContent

fileWrite(fileName)
