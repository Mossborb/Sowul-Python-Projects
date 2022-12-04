"""
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"

Names given are always valid strings.
"""

def are_you_playing_banjo(name):
    if name[0].upper() == 'R':
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"
    return name

#Other submissions

def stringConcatination(name):
   return name + " plays banjo" if name[0].lower() == 'r' else name + " does not play banjo"

def newFormat(name):
    if name[0].lower() == 'r':
        return "{} plays banjo".format(name)
    return "{} does not play banjo".format(name)

def oldFormat(name):
    if name[0] == 'r' or name[0] =='R':
        return ("%s plays banjo"%name)
    else:
        return ("%s does not play banjo"%name)

#Alternate Solution

def fStringsFormat(name):
    if name[0].upper() == 'R':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"


