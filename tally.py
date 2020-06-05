"""
A program used for printing out the number of points each NSBE member has.

See files "app.py" and "nps.json" for more info. KEEP ALL THREE FILES IN THE
SAME FOLDER/DIRECTORY (preferably the same folder).

- Giovannie Webb, gaw97@cornell.edu
"""

import json

class color():
    """
    Holds a few colors. Use this to change the color of the text!

    Source code: https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python

    See source code for proper usage of this class.
    """

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


def process(file_name):
    """
    Prints out each member's name, net id, and the number of points they've
    accumulated thus far.

    Parameters -
    file_name [str] : the name of the JSON file
    """

    # Read the file, assign variable "info" to be outermost dictionary
    file = open(file_name, "r")
    info = json.load(file)

    mem_info = info["member_info"]

    for key in mem_info: # key is a member's netID at each iteration, which has
                         # a key value of a dictionary mapping information such
                         # as name, points, etc.
        n = color.BOLD + info["member_info"][key]["name"] + color.END

        poin = info["member_info"][key]["points"]
        p = color.BOLD + color.RED + str(info["member_info"][key]["points"]) + color.END + color.END

        print("\n")
        if (int(poin) == 1):
            print(n + " has " + str(p) + " point.")
            print("NetID: " + key)
        elif (int(poin) > 1):
            print(n + " has " + str(p) + " points.")
            print("NetID: " + key)


print("\n")
print("Tallying points for each member...")
process("info.json")
print("\n")
