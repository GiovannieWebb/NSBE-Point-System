"""
NSBE Point System Tracker Prototype. Will be used to determine who gets
chosen for conference.

- By Giovannie Webb, gaw97. Membership Chair. Completed January 2020.

  Feel free to email gaw97@cornell.edu if you have any questions or further
  suggestions.
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


# CLASS OF INFORMATION TO KEEP TRACK OF FOR EACH MEMBER

"""
-------------------------------------------------------------------------------
"""

class NSBEMember():
    """
    A class representing a member of NSBE.
    """

    def __init__(self, netID, name, major, year):
        self.netID = netID
        self.name = name
        self.major = major
        self.graduationYear = year
        self.isRegistered = False
        self.points = 0

"""
-------------------------------------------------------------------------------
"""

# HELPER FUNCTIONS

def eventPoints(event):
    '''
    Return the number of points that a member should receive, depending on
    the current event that they attend.

    Parameter: event is of type string.
    '''
    if (event != None):
        assert type(event) == str

        e = event.lower()

        if e == 's':
            return 3
        elif e == 'c':
            return 2
        elif e == 'g':
            return 1


def isValidNetID(NetID):
    '''
    Return True if n is a valid netID. Return False otherwise.
    A valid netID has two or three letters and any amount of number following it.

    Parameter: NetID is of type string.
    '''
    assert type(NetID) == str

    if len(NetID) < 3:
        return False

    if NetID.isdigit() or NetID.isalpha() or not NetID.isalnum():
        return False

    letterPortion = ''
    numberPortion = ''

    for character in NetID:
        if character.isalpha():
            letterPortion = letterPortion + character
        if character.isdigit():
            numberPortion = numberPortion + character

    if len(letterPortion) < 2 or len(letterPortion) > 3:
        return False

    if letterPortion + numberPortion != NetID:
        return False

    return True


def netIDCorrection(NetID):
    '''Prompts the user to enter a valid netID if they hadn't done so before.
    (See docummentation in the helper function isValidNetID).

    Parameter: NetID is of type string.
    '''

    if (NetID == 'quit' or NetID == 'Quit'):
        return None
    if isValidNetID(NetID):
        return NetID.lower()
    elif not isValidNetID(NetID):
        canProceed = False
        while canProceed != True:
            nID = input("Error. Please enter a valid netID: ")
            if (nID == "quit" or nID == "Quit"):
                return None
            canProceed = isValidNetID(nID)

    nID = nID.lower()
    return nID


def isValidYesOrNo(response):
    '''
    Return True iff response is valid. False otherwise.
    A valid response is either 'y' for yes or 'n' for no. Uppercase letters
    allowed too.

    Parameter: response is of type string.
    '''

    return response == 'y' or response == 'Y' or response == 'n' or response == 'N'


def yesOrNoCorrection(response):
    '''
    Prompts the user to enter a valid yes or no response if they hadn't done so
    before.
    (See documentation for isValidYesOrNo).

    Parameter: response is of type string.
    '''

    if (response == 'quit' or response == "Quit"):
        return None
    if isValidYesOrNo(response):
        return response
    elif not isValidYesOrNo(response):
        canProceed = False
        while canProceed != True:
            yesOrNo = input("Error. Please enter a valid response [y/n]: ")
            if (yesOrNo == 'quit' or yesOrNo == 'Quit'):
                return None
            canProceed = isValidYesOrNo(yesOrNo)
    return yesOrNo


def isValidEventType(eventTypeResponse):
    '''
    Return True iff response is a valid event type. False otherwise.
    A valid event type is either 's' for a service event, 'c' for a corporate
    event, or g for a G-Body event.
    Uppercase letters allowed too.

    Parameter: response is of type string.
    '''

    return eventTypeResponse == 's' or eventTypeResponse == 'S' or eventTypeResponse == 'c' or eventTypeResponse == 'C'\
           or eventTypeResponse == 'g' or eventTypeResponse == 'G'


def eventTypeCorrection(eventTypeResponse):
    '''
    Prompts the user to enter a valid event type if they hadn't done so before.
    (See documentation for isValidEventType).

    Parameter: eventTypeResponse is of type string.
    '''

    if (eventTypeResponse == 'quit' or eventTypeResponse == 'Quit'):
        return None
    if isValidEventType(eventTypeResponse):
        return eventTypeResponse
    elif not isValidEventType(eventTypeResponse):
        canProceed = False
        while canProceed != True:
            type = input("Error. Please enter a valid event type [s/c/g]: ")
            if (type == "quit" or type == "Quit"):
                return None
            canProceed = isValidEventType(type)
    return type


def isValidTitle(response):
    """
    Return True iff user inputs a valid response for their name or their major.
    A valid name or major does nit have any numbers in it. Other characters
    could make a name invalid, but that could be difficult to account for.
    """

    for character in response:
        try:
            int(character)
            return False
        except ValueError:
            None
    return True


def titleCorrection(titleResponse):
    """
    Prompts the user to enter a valid title if they hadn't done so before. ]
    (See documentation for isValidTitle).
    """

    if (titleResponse == 'quit' or titleResponse == 'Quit'):
        return None
    if (isValidTitle(titleResponse)):
        return titleResponse
    else:
        canProceed = False
        while (canProceed != True):
            title = input("Error. Please enter a valid response with no numbers: ")
            if (title == 'quit' or title == "Quit"):
                return None
            canProceed = isValidTitle(title)
    return title


def isValidYear(response):
    """
    Returns True iff the response is a valid year, which should consist of four
    numbers alone (assuming that this software is being used between the years
    2020 and 9999, ha.)
    """

    if (len(response) != 4):
        return False
    if (not response.isnumeric()):
        return False
    return True


def yearCorrection(year):
    """
    Prompts the user to enter a valid gradutation year.
    (See documentation for isValidYear).
    """

    if (year == 'quit' or year == 'Quit'):
        return None
    if (isValidYear(year)):
        return year
    else:
        canProceed = False
        while (canProceed != True):
            new_year = input("Error. Please enter a valid graduation year: ")
            if (new_year == 'quit' or new_year == "Quit"):
                return None
            canProceed = isValidYear(new_year)
    return new_year

"""
-------------------------------------------------------------------------------
"""
'''~'''
"""
-------------------------------------------------------------------------------
"""

# JSON FUNCTIONS

# READ JSON FILE TO GET PRE-EXISTING MEMBER INFORMATION

def readJSON(file_name):
    """
    Reads the JSON file with the old dictionary.

    Parameters:
    file_name : str : the name of the JSON file to be edited.
    """

    file = open(file_name, "r")
    return json.load(file)

# Essentially, this stores the information previously saved in the JSON file
# into the variable mem_info. Updates to this dictionary are then made in this
# Python script, and JSON file is rewritten with the new dictionary.

def updateJSON(file_name, new_dict):
    """
    Updates the JSON file with the new dictionary.

    Parameters:
    file_name : str : the name of the JSON file to be edited.
    new_dict : dict : the Python dictionary in use, gathered from the previous
                      JSON file.
    """

    with open(file_name, "w") as updating_file:
        json.dump(new_dict,updating_file)

"""
-------------------------------------------------------------------------------
"""

# SCRIPT PROCEEDURE(S)

def intro():
    """
    Protocol to start the program. This is where the type of event is set.
    Returns the number of points each member should be awarded for attending
    this event.
    """

    print("\n")
    print(color.BOLD + "Answer the next question only if you're in charge of taking attendance for this event. If not, please give device "
          "to the person in charge of doing so." + color.END)
    print("\n")

    typeOfEvent = eventTypeCorrection(input("Enter " + color.UNDERLINE + "event type" + color.END + " [s for Service Event, c for Corporate Event, g for G-Body event]: "))
    print("\n")

    return eventPoints(typeOfEvent)


def signIn(json, pta):
    """
    Call this procedure in the run method to have members sign in.
    Returns the updated dictionary to be put back into the JSON file at the end.

    Parameters -
    json (type dict) : The current dictionary of member information within JSON.
    pta (type int) : 'Points to award' determined by the type of event.
    """

    entered = set() # Set of net-id's already entered for this event.

    while True:

        print(color.BOLD + "NSBE Event Sign-in" + color.END)
        print("\n")

        ID = netIDCorrection(input("Enter your " + color.UNDERLINE + "net ID" + color.END + ": "))
        if (ID == None):
            break
        else:

            if (ID not in json["member_info"]):
                # Add new member to the dictionary
                Name = titleCorrection(input("Enter your " + color.UNDERLINE + "full name" + color.END + ": "))
                if (Name == None):
                    break

                Major = titleCorrection(input("Enter your " + color.UNDERLINE + "major" + color.END + ": "))
                if (Major == None):
                    break

                grad_year = yearCorrection(input("Enter your " + color.UNDERLINE + "graduation year" + color.END + ": "))
                if (grad_year == None):
                    break

                regis = yesOrNoCorrection(input("Are you a " + color.UNDERLINE + "registered NSBE member" + color.END + "? [y/n]: "))
                if (regis == None):
                    break

                if (regis == 'y' or regis == 'Y'):
                    regis = True
                else:
                    regis = False

                json["member_info"][ID] = {"name" : Name, "major": Major, "graduation_year": int(grad_year), "is_registered": regis, "points": pta}
                entered.add(ID)

            else:
                if (ID not in entered):
                    json["member_info"][ID]["points"] = json["member_info"][ID]["points"] + pta
                    entered.add(ID)
                else:
                    print("\n")
                    print(color.BOLD + color.RED + "You've already signed in for this event." + color.END + color.END)


            print("\n")
            print("\n")
            print(color.GREEN + color.BOLD + "Thank you for your attendance!" + color.END)
            print("\n")
            print("\n")
            fin = input(color.BOLD + "Enter any key to sign in, or [only if you're in charge of this event] enter 'end' to close the application: " + color.END)
            print("\n")
            if (fin == 'end' or fin == "End"):
                print("Finished taking attendance.")
                print("\n")
                return json

    return json


def run():
    """
    Call this procedure at the end of this script to run the program.
    """

    mem_info = readJSON("info.json")

    points_to_award = intro()

    new_json = signIn(mem_info, points_to_award)

    updateJSON("info.json", new_json)


# Run the program
run()
