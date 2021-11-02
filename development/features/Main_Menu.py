from development.classes.Menu import *


# Main menu
def display_main_menu():
    Menu.DisplayMainMenu(Menu)
    print("0 - View managed devices")

    user_choice = None
    while user_choice != "":
        # User makes selection
        user_choice = input("> ")
        if user_choice == "1":
            from development.features.change_device_name import change_device_name
            change_device_name()
            user_choice = ""
        elif user_choice == "2":
            #change_port_status()
            user_choice = ""
        elif user_choice == "3":
            user_choice = ""
        elif user_choice == "4":
            user_choice = ""
        elif user_choice == "5":
            user_choice = ""
        elif user_choice == "0":
            user_choice = ""
        else:
            # If user does not make selection or selection is invalid
            print("> Invalid selection\n> Press RETURN to make a selection")
