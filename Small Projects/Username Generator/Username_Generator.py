#Generate a username using a database of words. 

#Find a database of words or create your own. 

#Access data base from python code. 

#Usernames can have the option to be two words, I.E UnfamiliarMonkey, Unfamiliar_Monkey, Horse Toucher Stinky Batman 

import pandas as pd
import random

df = pd.read_excel('/Users/norbertsowul/Python/Python-Projects/SmallProjects/Username_Generator/Username_Database.xlsx')

#Noun Adjective Verb
#Noun Verb Adjective
#Adjective Noun Verb
#Adjective Verb Noun
#Verb Adjective Noun
#Verb Noun Adjective



def createUserName():

    nounLength = 699
    adjectiveLength = 171
    verbLength = 436
    
    iNoun = random.randint(0,nounLength)
    Noun = df.loc[iNoun,'Noun']
    iAdjective = random.randint(0,adjectiveLength)
    Adjective = df.loc[iAdjective,'Adjective']
    iVerb = random.randint(0,verbLength)
    Verb = df.loc[iVerb,'Verb']

    return Adjective + ' ' + Verb + ' ' + Noun

for i in range(0,50):
    print(createUserName())





