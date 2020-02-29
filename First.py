# Here is a comment, to demonstrate Pull Requests
import time
def one_three(question):
    answer = input(question + ": ").lower().strip()
    print("")
    while not(answer == "2" or \
    answer == "1"):
        print("Input 1-3 please")
        answer = input(question + ": ").lower().strip()
        print("")
    if answer[0] == "1":
        return True
    else:
        return False

if one_three("Pick 1-3"):
     print("Initiating Mad Libs 1")
     time.sleep(2)
     print("initiated")
     time.sleep(.5)
     mad1()
else:
    print("Initiating Mad Libs 2")
    time.sleep(2)
    print("initiated")
    time.sleep(.5)
    mad2()
    exit()
