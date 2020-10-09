# Import the modules
import sys
import random
#how to improve such if else logic with contineous QA?
#Answer = You Can add while True statement
# You doesnot need to create a boolean for this one
answers = random.randint(1,8) # Here I have put this not in while loop because it will generate a random number everytime.
# print(answers)
while True:
    question = int(input("Ask the magic 8 ball a question: (Enter to quit) "))
    if question == "":
        sys.exit()
    # Here I have put question bcoz the number that the user enters will be put in the variable(question). You can do better.
    elif answers == question:
        print("Nice, you r correct")
        answers = random.randint(1,8)
        # print(answers)
        # Always Remember to typecast the numbers in int not in string........I have worked in your project. Plz save it.Thanks
        # From India
    else:
        print("you are incorrect")
