import time
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def mad1():
    verb1 = input("Enter a verb ending in ing: ")
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter a adjective: ")
    bodypart = input("Enter a body part: ")
    noun2 = input("Enter a  plural noun: ")
    noun3 = input("Enter a noun: ")
    verb2 = input("Enter a verb ending in ing: ")
    verb3 = input("Enter a verb: ")
    adjective2 = input("Enter a adjective: ")
    name = input("Enter a name: ")


    print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
    print(color.BOLD + color.RED + "                  Summer camp letter" + color.END)
    print("   To Mom")
    print("Hi mom I am " + verb1 + " to you from summer camp. How is it going back home, it is good down here.")
    print("There was a violent " + noun1 + " down here last night. It " + adjective1 + "ed everyone. I hope there are no more.")
    print("We also went on a hiking trip. I almost broke my " + bodypart + " wile hiking.")
    print("One of the " + noun2 + " in our " + noun3 + " burned out and they don't have any replacement " + noun2 + ".")
    print("We had to do a lot of " + verb2 + " on Tuesday. We also had to " + verb3 + " on making a art project.")
    print("The pillows down here are nice and " + adjective2)
    print("Any ways i will write back to you latter ")
    print("with much love: ")
    print("             " + name)
    time.sleep(5)
    print("-----------------------\n Thank you for playing \n" + color.BOLD + color.BLUE + "      Credits: " + color.END + " \n Main programing: Me \n Color/Boldness: Jim \n-----------------------")

def mad2():
    name = input("Enter a woman's name: ")
    gender = input("Enter son or daughter: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    verb1 = input("Enter a verb ending in ing: ")
    noun3 = input("Enter a noun: ")
    dc = input("Enter a last name: ")
    adjective1 = input("Enter a adjective: ")
    date = input("Enter a date in this format: \"Month\" \"Day\" \"Year\": ")
    verb2 = input("Enter a verb: ")
    name2 = input("Enter a name: ")
    if gender == "son":
        gender2 = "He"
    else:
        gender2 = "She"



    print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
    print(color.BOLD + color.RED + "             Doctors note" + color.END)
    print("Dear Mrs." + name)
    print("my " + gender + " has came down with a case of the " + noun1 + ".")
    print(gender2 + " will " + color.BOLD + "NOT " + color.END + "be attending " + noun2 + " today")
    print(gender2 + " has been " + verb1 + " all " + noun3 + ".")
    print("I have made a appointment with Dc." + dc + ", " + gender2 + " is \n" + adjective1 + " for a appointment on " + date + ".")
    print("Dc." + dc + " has been " + verb2 + "ed at a very high level. \nHe will get back to you with all of the information ASAP.")
    print("      sincerely " + name2 + ".")
    time.sleep(5)
    print("-----------------------\n Thank you for playing \n" + color.BOLD + color.BLUE + "      Credits: " + color.END + " \n Main programing: Me \n Color/Boldness: Jim \n-----------------------")

def mad3():
    year = input("Enter a year. Example:\"1993\": ")
    place = input("Enter a place: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    bodypart = input("Enter a Body part: ")
    somthing_scarry = input("Enter something scary: ")
    number = input("Enter a  number: ")

    print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
    print(color.BOLD + color.RED + "                          War" + color.END)
    print("It was the year, " + year + ". It took place in a place called " + place + ".")
    print("it was the war named " + noun1 + ". Suddenly are commander yelled " + color.BOLD + verb1 + color.END + ".")
    print("He yelled " + verb1 + "because a explosion just went off beside me.")
    print("I lost my " + bodypart + "(s) in a explosion. It was as scary as " + somthing_scarry + ".")
    print("Finally after a whole " + number + "days the white flag appeared on the other side of the field.")
    print("WE WON.")
    time.sleep(5)
    print("-----------------------\n Thank you for playing \n" + color.BOLD + color.BLUE + "      Credits: " + color.END + " \n Main programing: Me \n Color/Boldness: Jim \n-----------------------")



X = input("Chose a Mad Lib 1-3: ")
if X == "1":
    print("Initiating Mad Libs 1")
    time.sleep(2)
    print("initiated")
    time.sleep(.5)
    mad1()
elif X == "2":
    print("Initiating Mad Libs 2")
    time.sleep(2)
    print("initiated")
    time.sleep(.5)
    mad2()
elif X == "3":
    print("Initiating Mad Libs 3")
    time.sleep(2)
    print("initiated")
    time.sleep(.5)
    mad3()
elif not(X == "1") and not(X == "2"):
    print("Not a valid Mad Lib")



