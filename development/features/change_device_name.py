from development.utilities.ping import ping
from development.classes.Menu import clear
from development.classes.Network import *

# Change device host name
def change_device_name():
    clear()
    print("===================================")
    # Ping 8.8.8.8 to verify user is connected to internet
    if ping("8.8.8.8") == True:
        print("\n")
        print("> User connected to internet\n\n\n")
        
        # Start telnet process
        clear()
        D = DeviceInfo().set_device_info()
        Transfer = NetServers("10.122.153.158",
                              "calo",
                              "calo",
                              "10.122.153.158")
        Device = NetDevice(D[0], D[1], D[2], D[3], D[4], Transfer)

        new_name = input("Enter new valid device hostname: ")
        host = D[0]
        port = D[1]
        print(f"Attempting to connect to Telnet://{host}:{port}")
        print("#" * 60)
        # Connect to device - Send user back to main menu if connection fails
        try:
            Device.NetConnect()
            print(f"Successfully connected to Telnet://{host}:{port}")
            print("#" * 60)
            Device.NetEnable()
            # Send commands
            print(f"Changing Telnet://{host}:{port} hostname to {new_name}")
            Device.NetHostName(new_name)
            # Get verifications
            print(f"Successfully changed Telnet://{host}:{port} hostname to {new_name}")
            print("Verification:")
            print(Device.FindPrompt() + "\n")
            # Disconnect
            print("#" * 60)
            Device.NetDisconnect()
            print(f"Disconnected from Telnet://{host}:{port}")
            print("#" * 60)
            # Return user to main menu
            print("Press ANY KEY to return to main menu")
            user_choice = input("> ")
            clear()
        except:
            print("===================================")
            print(f"Unable to connect to Telnet://{host}:{port}")
            # Return user to main menu
            print("Press ANY KEY to return to main menu")
            user_choice = input("> ")
            clear()
    # If user cannot ping 8.8.8.8
    else:
        print("===================================")
        print("Unable to verify internet connection")
        # Return user to main menu
        print("Press ANY KEY to return to main menu")
        user_choice = input("> ")
        clear()
