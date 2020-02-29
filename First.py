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


def yes_or_no(question):
    answer = input(question + "(1-3): ")
    print("")
    while not(answer == 1  or answer == 2 or answer == 3):
        print("Input a number, 1-3")
        answer = input(question + "(1 - 3):")
        print("")

    if answer == 1:
        verb1 = raw_input("Enter a verb ending in \"ing\": ")
        noun1 = raw_input("Enter a noun: ")
        adjective1 = raw_input("Enter a adjective: ")
        bodypart = raw_input("Enter a body part: ")
        noun2 = raw_input("Enter a  plural noun: ")
        noun3 = raw_input("Enter a noun: ")
        verb2 = raw_input("Enter a verb ending in ing: ")
        verb3 = raw_input("Enter a verb: ")
        adjective2 = raw_input("Enter a adjective: ")
        name = raw_input("Enter a name: ")


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

        return True
    if answer == 2:
        print("You typed a 2")
        return True
    if answer == 3:
        print("You typed a 3.  Pfft. 3 is for LOOSERS. :-p")
        return True                
    else:
        return False
#print(args.echo)
if yes_or_no("This part of the code is the text of the question"):
    print("Excellent! :D")
else:
    print(bcolors.FAIL + "Operation cancelled. \nNo mail sent!\n ")
    exit()