import os
import configparser
def parser(inputFile, boolean):
    ree = False
    config = configparser.ConfigParser()
    config.read('config.ini')
    if not config.read('config.ini') == []:
        if not config['EXCLUSIONS']['exclusions'] == "":
            try:
                exclusions = config['EXCLUSIONS']['exclusions'].split(", ")
            except:
                exclusions = config['EXCLUSIONS']['exclusions']
            if not boolean:
                if not ree:
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
                                ex = 0
                                for exclusion in exclusions:
                                    if exclusion[-3:] == "[0]":
                                        if not exclusion[:-3] in hehe[0]:
                                            ex += 1
                                    elif exclusion[-3:] == "[1]":
                                        if not exclusion[:-3] in hehe[1]:
                                            ex += 1
                                    elif exclusion[-3:] == "[2]":
                                        if not exclusion[:-3] in hehe[0]:
                                            if not exclusion[:-3] in hehe[1]:
                                                ex += 1
                                    elif exclusion[-3:] == "[3]":
                                        if not exclusion[:-3] in hehe[1][:len(exclusion)]:
                                            ex += 1
                                    else:
                                        print("Invalid exclusion formatting. Each exclusion must end with either '[0]', '[1]', '[2]' or '[3]'. \n   [0] = Exclude from Name List \n   [1] = Exclude from Content List \n   [2] = Exclude from both Lists \n   [3] = Exclude if at the beginning of Content List. Used for ooRP messages.")
                                        os._exit(0)
                                    if ex >= len(exclusions):
                                        nameList.append(hehe[0])
                                        contentList.append(hehe[1])

                        i = i + 1
                        ree = True
            else:
                if not ree:
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
                                ex = 0
                                for exclusion in exclusions:
                                    if exclusion[-3:] == "[0]":
                                        if not exclusion[:-3] in hehe[0]:
                                            ex += 1
                                    elif exclusion[-3:] == "[1]":
                                        if not exclusion[:-3] in hehe[1]:
                                            ex += 1
                                    elif exclusion[-3:] == "[2]":
                                        if not exclusion[:-3] in hehe[0]:
                                            if not exclusion[:-3] in hehe[1]:
                                                ex += 1
                                    elif exclusion[-3:] == "[3]":
                                        if not exclusion[:-3] in hehe[1][:len(exclusion)]:
                                            ex += 1
                                    else:
                                        print("Invalid exclusion formatting. Each exclusion must end with either '[0]', '[1]', '[2]' or '[3]'. \n   [0] = Exclude from Name List \n   [1] = Exclude from Content List \n   [2] = Exclude from both Lists \n   [3] = Exclude if at the beginning of Content List. Used for ooRP messages.")
                                        os._exit(0)

                                    if ex >= len(exclusions):
                                        nameList.append(hehe[0])
                                        contentList.append(hehe[1])
                        i = i + 1
                        ree = True
        else:
            print("No exclusions defined.")
        if not boolean:
            if not ree:
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
                            if not "Death" in hehe[0]:
                                if not "has requested to dock" in hehe[1]:
                                    if not "Options" in hehe[0]:
                                        if not "Tip" in hehe[0]:
                                            nameList.append(hehe[0])
                                            contentList.append(hehe[1])
                    i = i + 1
                    ree = True
        else:
            if not ree:
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
                    ree = True
    else:
        if not boolean:
            if not ree:
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
                    ree = True
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
                    ree = True
        else:
            if not ree:
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
                            if not "Death" in hehe[0]:
                                if not "Tip" in hehe[0]:
                                    if not "has requested to dock" in hehe[1]:
                                        nameList.append(hehe[0])
                                        contentList.append(hehe[1])
                    i = i + 1
                    ree = True
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
                    ree = True
    return nameList, contentList
config = configparser.ConfigParser()
config.read('config.ini')

useInputFile = False
useOutputFile = False
useIncludeTimestamps = False
if not config.read('config.ini') == []:
    if not config['SETTINGS']['inputFile'] == "":
        useInputFile = True
    else:
        useInputFile = False
    if not config['SETTINGS']['outputFile'] == "":
        useOutputFile = True
    else:
        useOutputFile = False
    if not config['SETTINGS']['includeTimestamps'] == "":
        useIncludeTimestamps = True
    else:
        useIncludeTimestamps = False

if not useInputFile:
    inputFile = input('Input Path for DSAce log file("default" or blank for .\DSAce.txt): ')
    if inputFile == "default":
        inputFile = "DSAce.txt"
    if inputFile == "":
        inputFile = "DSAce.txt"
else:
    inputFile = config['SETTINGS']['inputFile']

if not useOutputFile:
    if "." in inputFile:
        outputFile = input('Output Path for cleaned DSAce log("default" for ' + inputFile.rsplit(".", 1)[0] + '_cleaned.' + inputFile.rsplit(".", 1)[1] + '): ')
        if outputFile == "default":
            outputFile = inputFile.rsplit(".", 1)[0] + '_cleaned.' + inputFile.rsplit(".", 1)[1]
        if outputFile == "":
            outputFile = inputFile.rsplit(".", 1)[0] + '_cleaned.' + inputFile.rsplit(".", 1)[1]
    else:
        outputFile = input('Output Path for cleaned DSAce log file("default" or blank for ' + inputFile + '_cleaned): ')
        if outputFile == "default" or outputFile == "":
            outputFile = inputFile + '_cleaned'
        if outputFile == "":
            outputFile = inputFile + '_cleaned'
else:
    outputFile = config['SETTINGS']['outputFile']

if not useIncludeTimestamps:
    while True:
        perhaps = input('Include timestamps (y/n): ')
        if "y" in perhaps:
            perhaps = True
            break
        elif "n" in perhaps:
            perhaps = False
            break
        else:
            print("Invalid input.")
else:
    if "y" in config['SETTINGS']['includeTimestamps']:
        perhaps = True
    elif "Y" in config['SETTINGS']['includeTimestamps']:
        perhaps = True
    elif "n" in config['SETTINGS']['includeTimestamps']:
        perhaps = False
    elif "N" in config['SETTINGS']['includeTimestamps']:
        perhaps = False
    else:
        print("Invalid 'includeTimestamps' entry.")
        os._exit(0)

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

print("Done.")