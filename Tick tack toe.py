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
import time
def tic_tac_toe():
    print(color.BOLD + color.RED + "                        Tic Tac Toe" + color.END)

    print("____________________________________________________________")
    print("| 1                | 2                 | 3                 |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|__________________|___________________|___________________|")
    print("| 4                | 5                 | 6                 |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|__________________|___________________|___________________|")
    print("| 7                | 8                 | 9                 |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|__________________|___________________|___________________|")

tic_tac_toe()
time.sleep(2)
X = input("X Chose a square 1-9")

if X == "1":
    print(color.BOLD + color.RED + "                        Tic Tac Toe" + color.END)

    print("____________________________________________________________")
    print("| 1     \    /     | 2                 | 3                 |")
    print("|        \  /      |                   |                   |")
    print("|         \/       |                   |                   |")
    print("|         /\       |                   |                   |")
    print("|        /  \      |                   |                   |")
    print("|_______/____\_____|___________________|___________________|")
    print("| 4                | 5                 | 6                 |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|__________________|___________________|___________________|")
    print("| 7                | 8                 | 9                 |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|                  |                   |                   |")
    print("|__________________|___________________|___________________|")
else:
    print("fail")