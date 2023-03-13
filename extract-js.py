#this is a python script to extract all of the filenames of javascript files listed within the given .txt file. This file will open, read, sort and return a list of javascript files.

# step 1 is to open/read the file. create a variable called f (for file)
# now define another variable called data to store the text from the file.
# now we need to search through this text for matches to the ".js" match

import re

mypattern = re.compile("[^/]*\.js", re.IGNORECASE)

f = open("/home/kali/access_log.txt", "r") # open the file

data = str(f.read()) #make sure we pass all of this as a string as we save it into this variable to be safe

listofmatches = mypattern.findall(data) #use the findall method on the pattern object, tell it to search the string data

deduplicatedlist = list(dict.fromkeys(listofmatches)) #make a dictionary to remove the duplicates (dictionaries can't include any duplicate keys) and then convert the dictionary back into a list.

sortedlist = sorted(deduplicatedlist) #sort it

for item in sortedlist:
    print(item) # print each item on a new line to stdout



f.close() # close the file when done