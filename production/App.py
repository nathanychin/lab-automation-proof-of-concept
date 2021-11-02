from features.Main_Menu import display_main_menu
from utilities.clear import clear

# Welcome banner
def welcome_banner():
    print("===================================")
    print("||      CX LABS AUTOMATION TOOL  ||")
    print("||          MAIN MENU            ||")
    print("===================================\n")

# Program begins
clear()
welcome_banner()

user_choice = None

# Loop to keep user in menu
while user_choice != "":
    print("Press RETURN to view menu")
    user_choice = input()
    if user_choice == "":
        # Clear console
        clear()
        display_main_menu()
        user_choice = None