import os

def parser(inputFile, bool):
    if not bool:
        try:
            with open(inputFile, 'r') as input:
                input = input.read()
                input = input.split('\n')
        except:
            raise(FileNotFoundError)
        #doneAlready = []
        tryExcept = []
        nameList = []
        contentList = []
        i = 0

        for x in input:
            kek = x[22:]
            if ":" in kek:
                # if i not in doneAlready:
                #     print("Proccessing line: " +  str(i))
                # doneAlready.append(i)
                try:
                    hehe = kek.split(': ', 1)
                    tryExcept.append(hehe[1])
                    works = True
                except IndexError:
                    works = False

                if works:
                    if not hehe[0] == "Death":
                        if not " " in hehe[0]:
                            nameList.append(hehe[0])
                            contentList.append(hehe[1])
            i = i + 1
    else:
        try:
            with open(inputFile, 'r') as input:
                input = input.read()
                input = input.split('\n')
        except:
            raise(FileNotFoundError)
        #doneAlready = []
        tryExcept = []
        nameList = []
        contentList = []
        i = 0

        for x in input:
            kek = x
            if ":" in x:
                # if i not in doneAlready:
                #     print("Proccessing line: " +  str(i))
                # doneAlready.append(i)
                try:
                    hehe = kek.split(': ', 3)
                    tryExcept.append(hehe[1])
                    works = True
                    tryExcept = []
                except IndexError:
                    works = False

                if works:
                    if not "Death" in hehe[0]:
                        if not "has requested to dock" in hehe[1]:
                            if not "Options" in hehe[0]:
                                if not "Tip" in hehe[0]:
                                    nameList.append(hehe[0])
                                    contentList.append(hehe[1])
            i = i + 1        
    return nameList, contentList



inputFile = input('Input Path for DSAce log file("default" for .\DSAce.txt): ')
if inputFile == "default":
    inputFile = "DSAce.txt"
if inputFile == "":
    inputFile = "DSAce.txt"

if "." in inputFile:
    outputFile = input('Output Path for cleaned DSAce log("default" for ' + inputFile.rsplit(".", 1)[0] + '_cleaned.' + inputFile.rsplit(".", 1)[1] + '): ')
    if outputFile == "default":
        outputFile = inputFile.rsplit(".", 1)[0] + '_cleaned.' + inputFile.rsplit(".", 1)[1]
    if outputFile == "":
        outputFile = inputFile.rsplit(".", 1)[0] + '_cleaned.' + inputFile.rsplit(".", 1)[1]
else:
    outputFile = input('Output Path for cleaned DSAce log("default" for ' + inputFile+ '_cleaned): ')
    if outputFile == "default" or outputFile == "":
        outputFile = inputFile + '_cleaned'
    if outputFile == "":
        outputFile = inputFile + '_cleaned'

while True:
    perhaps = input('Include timestamps (y/n): ')
    if perhaps == "y":
        perhaps = True
        break
    elif perhaps == "n":
        perhaps = False
        break
    else:
        print("Invalid input.")

parserList = parser(inputFile, perhaps)
nameList = parserList[0]
contentList = parserList[1]
commentList = []

i = 0

for name in nameList:
    commentList.append(nameList[i] + ": " + contentList[i] + "\n")
    i += 1
try:
    with open(outputFile, "w") as input:
        input.writelines(commentList)
except:
    raise(FileNotFoundError)

os.system('pause')