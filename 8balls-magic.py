# Import the modules
import sys
import random
#how to improve such if else logic with contineous QA?
ans = True

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")
    ansList = ["It is certain","Outlook good","You may rely on it", "Ask again later",
               "Concentrate and ask again","Reply hazy, try again","My reply is no","My sources say no"]
    
    answers = random.randint(0,7)
    
    if question == "":
        sys.exit()
    else:
        print(ansList[answers])
