#12.10.2024
#grace wafle


#init






#functions

def intro ():
    print ("""Welcome to MadLibs! Today you will be asked to write a few words to finsih the story.
    After you have typed in the words you will see the final story you created.""")


def finalSentence ():
    print ("While " + str(verb) + "down the street Ava was looking at a " + str(noun) + ". While looking at the " + str(noun) +  " she fell. Ava fell so hard she broke her " + str(bodyPart) + " and had to go to the doctor. At the doctors they have a special question for people who break their bones. 'What is your favorite animal?' they asked Ava. (Knowing her favorite animal is a(n) " + str(animal) +") Ava responded saying her favorite animal was a(n) " +  str(animal) + ". So everyone stopped worrying and knew everything would be okay because she still knew the special questions answer. ")


# main

intro()
print("Please Follow the instructions.")
verb = input("Insert a verb:")
noun = input ("Insert a noun:")
animal = input("Insert an animal:")
bodyPart = input("Insert a body part:")
finalSentence()
