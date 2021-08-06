# DSAceCleaner
DSAceCleaner is a Python-Script to remove junk/unnecessary lines from Discovery Freelancer's DSAce chatlogs.

## Usage
Start the script:

`python .\DSAceCleaner.py` OR `start DSAceCleaner.exe`

Follow the given instructions:
`
Input Path for DSAce log file("default" for .\DSAce.txt):
`
`
Output Path for cleaned DSAce log("default" for DSAce_cleaned.txt):
`
`
Include timestamps (y/n):
`

------------


The script can also be used as a library, acting as a parser. It'll return a list of the Names and another of the Message Contents.
```python
from DSAceCleaner import parser
parsedList = parser('DSAce.txt',      True)
#		    ^Input File	^Include timestamps

nameList = parsedList[0]
contentList = parsedList[1]
```

------------

Compiled using [Nuitka](https://www.nuitka.net/ "Nuitka").
