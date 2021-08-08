# DSAceCleaner
DSAceCleaner is a Python-Script to remove junk/unnecessary lines from Discovery Freelancer's DSAce chatlogs.

## Usage
Start the script:

`python .\DSAceCleaner.py` OR `start DSAceCleaner.exe`

Follow the given instructions:

```
Input Path for DSAce log file("default" for .\DSAce.txt):
Output Path for cleaned DSAce log("default" for DSAce_cleaned.txt):
Include timestamps (y/n):
```

**OR:**

With the introduction of config-file support, this entire proccess can be automated.
The config-file includes the following keys:

`inputFile`
`outputFile`
`includeTimestamps`
`exclusions`

The *in-* and *outputFile* keys are self-explanatory. They take the in- and output path of the DSAce file. The *includeTimestamps* key also is. It defines wether to include Timestamps or not. It takes either 'y' or 'n' as arguments.

The *exclusions* key is a bit more special, it defines what is to be included in the cleaned file and what is to be filtered out. It can take multiple arguments, all of which must be seperated by a comma and space (', '). Each argument must end with either [0], [1], [2] or [3].

> [0] = Exclude argument from Name List.
[1] = Exclude argument from Content List.
[2] = Exclude argument from both Lists.
[3] = Exclude argument from and if at the beginning of Content List. Used for ooRP messages.

------------


The script can also be used as a library, acting as a parser. It'll return a list of the Names and another of the Message Contents.
```python
from DSAceCleaner import parser
parsedList = parser('DSAce.txt',      True)
#		      ^Input File	^Include timestamps

nameList = parsedList[0]
contentList = parsedList[1]
```

------------

Compiled using [Nuitka](https://www.nuitka.net/ "Nuitka").
