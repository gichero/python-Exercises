def openFile():

    fileName = raw_input("Name your file: ")

    myFile = open(fileName)

    fileContent = myFile.read()

    print fileContent

openFile()
