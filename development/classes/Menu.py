class Menu:
    # Menu.DisplayMainMenu(Menu)
    def __init__(self):
        self.options = []

    def DisplayMainMenu(self):
        print("Select an action")
        print("Press RETURN after typing your choice")
        print("")
        print("===================================")
        features = [
            'Change device name',
            'Change port status',
            'Set IP address of device',
            'Set IP route',
            'Download image to device from FTP server'
        ]
        for feature in features:
            feature_index = features.index(feature) + 1
            print(str(feature_index) + " - " + feature)
        print("===================================")


def clear():
    import os
    return os.system('cls')
