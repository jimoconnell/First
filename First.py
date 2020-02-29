# # Here is a comment, to demonstrate Pull Requests
# import time
# def one_three(question):
#     answer = input(question)
#     print("")
#     while not(answer == "2" or \
#     answer == "1"):
#         print("Input 1-3 please")
#         answer = input(question + ": ")
#         print("")
#     if answer[0] == "1":
#         return True
#     else:
#         return False

# if one_three("1"):
#      print("Initiating Mad Libs 1")
#      time.sleep(2)
#      print("initiated")
#      time.sleep(.5)
#      mad1()
# else:
#     print("Initiating Mad Libs 2")
#     time.sleep(2)
#     print("initiated")
#     time.sleep(.5)
#     mad2()
#     exit()
def yes_or_no(question):
    answer = input(question + "(1-3): ")
    print("")
    while not(answer == 1  or answer == 2 or answer == 3):
        print("Input a number, 1-3")
        answer = input(question + "(1 - 3):")
        print("")
    if answer == 1:
        print("You typed a 1")
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