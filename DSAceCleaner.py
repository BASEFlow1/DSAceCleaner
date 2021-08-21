import os
import configparser
import time

# Start timing.
startTime = time.time()

def parser(inputFile, includeTimestamps):
    configPresent = False
    exclusionsPresent = False
    exclusions = []
    tryExcept = []
    nameList = []       # returns
    contentList = []    # returns
    config = configparser.ConfigParser()
    config.read('config.ini')
   
    # --- CONFIG PRESENT ---
    # Check if the config-file is present, set variable 'configPresent' to True if it is.
    # Used in 'EXCLUSIONS PRESENT' to determine whether exclusions 
    # are present in the config or not.
    if not config.read('config.ini') == []:
        configPresent = True

    # --- EXCLUSIONS PRESENT ---
    # Check if the exclusions in the config-file are present, 
    # set variable 'exclusionsPresent' to True if it is.
    # Used for deciding whether to split the exclusions or not.
    if configPresent:
        if not config['EXCLUSIONS']['exclusions'] == "":
            exclusionsPresent = True

    # --- SPLIT EXCLUSIONS ---
    # Try to split the exclusions stored inside 
    # the config and assign that list to variable 'exclusions'.
    # If it fails, only one(1) exclusion is present.
    if exclusionsPresent:
        try:
            exclusions = config['EXCLUSIONS']['exclusions'].split(", ")
        except:
            exclusions = config['EXCLUSIONS']['exclusions']

    # --- OPEN INPUT-FILE ---
    # Try to open the input-file specifed as an argument in the function.
    # If it fails, raise an exception.
    try:
        with open(inputFile, 'r') as input:
            input = input.read()
            input = input.split('\n')
    except:
        raise

    i = 0

    # --- MAIN LOOP ---
    # All the parsing happens here.
    for x in input:

        # --- INCLUDE TIMESTAMPS ---
        # If 'includeTimestamps' is False, remove the first 22 characters from the 
        # start of the current line, as those will always be Timestamps.
        # (Except if the timestamps weren't logged to begin with, that'd cause things to break)
        # TODO: Check if current line is Timestamped
        if not includeTimestamps:
            x = x[22:]

        # --- WORKS ---
        # Check if ':' is present in the current line. If it's not, it can be discarded.
        # If ':' is present, try to declare variable 'splitX' and append it's second index
        # to 'tryExcept'. If no exception is thrown, set 'works' to be True. Else, set it to be False.
        if ":" in x:
            try:
                splitX = x.split(': ', 1)
                tryExcept.append(splitX[1])
                works = True
            except IndexError:
                works = False

            # --- EXCLUSION LOOP ---
            # If 'works' and 'exclusionsPresent' are True, run the exclusion Loop.
            # If 'exclusionsPresent' is False, use a hardcoded, bad, horrible, terrible, small list of exclusions.
            if works:
                if exclusionsPresent:
                    ex = 0

                    # For each exclusion, check what suffix it has. 
                    # If it doesn't have a valid one, print an error message and exit.
                    for exclusion in exclusions:
                        
                        # If the exclusion ends with '[0]', check if it is in the current line. If it does, increment 'ex' by one(1).
                        # This is repeated for every suffix.
                        if exclusion[-3:] == "[0]":
                            if not exclusion[:-3] in splitX[0]:
                                ex += 1
                        elif exclusion[-3:] == "[1]":
                            if not exclusion[:-3] in splitX[1]:
                                ex += 1
                        elif exclusion[-3:] == "[2]":
                            if not exclusion[:-3] in splitX[0]:
                                if not exclusion[:-3] in splitX[1]:
                                    ex += 1
                        elif exclusion[-3:] == "[3]":
                            if not exclusion[:-3] in splitX[1][:len(exclusion)]:
                                ex += 1
                        else:
                            print("Invalid exclusion formatting. Each exclusion must end with either '[0]', '[1]', '[2]' or '[3]'. \n   [0] = Exclude from Name List \n   [1] = Exclude from Content List \n   [2] = Exclude from both Lists \n   [3] = Exclude if at the beginning of Content List. Used for ooRP messages.")
                            os._exit(0)

                        # If 'ex' is less than or equal to the number of exclusions,
                        # append 'splitX[0]' to 'nameList' and 'splitX[1]' to 'contentList' respectively.
                        if ex >= len(exclusions):
                            nameList.append(splitX[0])
                            contentList.append(splitX[1])
                else:
                    if not "Death" in splitX[0]:
                        if not "has requested to dock" in splitX[1]:
                            if not "Options" in splitX[0]:
                                if not "Tip" in splitX[0]:
                                    nameList.append(splitX[0])
                                    contentList.append(splitX[1])                    

        i = i + 1
    # Return the 'nameList' and 'contentList'
    return nameList, contentList

# Initialise the configParser and read 'config.ini'
config = configparser.ConfigParser()
config.read('config.ini')

useInputFile = False
useOutputFile = False
useIncludeTimestamps = False

# If the config-file isn't empty, determine whether to use the specified
# input- and output-file and whether or not to include timestamps by checking if 
# the respective key's value is empty or not.
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

# If no input-file is specified in the config, ask for user-input.
# Else use it.
if not useInputFile:
    inputFile = input('Input Path for DSAce log file("default" or blank for .\DSAce.txt): ')
    if inputFile == "default":
        inputFile = "DSAce.txt"
    if inputFile == "":
        inputFile = "DSAce.txt"
else:
    inputFile = config['SETTINGS']['inputFile']

# If no output-file is specified in the config, ask for user-input.
# Else use it.
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

# If 'includeTimestamps' is not specified in the config, ask for user-input.
# Else use it.
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

# Call 'parser' and assign its indices to 'nameList' and 'contentList' respectively.
parserList = parser(inputFile, perhaps)
nameList = parserList[0]
contentList = parserList[1]
commentList = []

i = 0

# For each name in 'nameList', append the full, assembled message
for name in nameList:
    commentList.append(nameList[i] + ": " + contentList[i] + "\n")
    i += 1

# Try to open the output-file and write 'commentList' to it.
# Raise an exception if it fails.
try:
    with open(outputFile, "w") as input:
        input.writelines(commentList)
except:
    raise

# End timing.
executionTime = (time.time() - startTime)

# Print "Done" message and time spent executing the script.
print('Proccessing done.\nExecution time: ' + str(round(executionTime, 3)) + "s")