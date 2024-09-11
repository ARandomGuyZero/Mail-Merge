"""
Mail Merge

Author: Alan
Date: September 11th 2024

This script can generate a letter for each line of the invited_names.txt file.
Then, it creates a file for each name, and it's saved in the Output/ReadyToSend folder
"""

def get_list_of_guests():
    """
    Extracts a list of guests from the invited_names file
    :return: Returns a list of String that contains the guests' names
    """
    with open("Input/Names/invited_names.txt", mode="r+") as guest_file:
        return guest_file.readlines()

def create_letter(new_guest):
    """
    Creates a new file using the guest's name.
    :param new_guest: String of the guest's name.
    """
    # Open the starting letter as the base letter to modify
    with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
        # Create a new letter that will contain the name of the guest
        with open(f"./Output/ReadyToSend/letter_for_{new_guest}.txt", mode="w") as new_letter:
            # Get the information data
            invitation = letter.read()
            # Replace the word [name] for the name of the guest
            new_invitation = invitation.replace("[name]", new_guest)
            # Write the new invitation
            new_letter.write(new_invitation)

list_of_guests = get_list_of_guests()

# Simple loop to iterate the guest list
for guest in list_of_guests:
    create_letter(guest.strip())