# Welcome Banner
def welcome_banner():
    print("===================================")
    print("||    CX LABS AUTOMATION TOOL    ||")
    print("||          . | | | .            ||")
    print("===================================\n")

def start():
    # Program begins
    from development.classes.Menu import clear
    from development.features.Main_Menu import display_main_menu
    
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
