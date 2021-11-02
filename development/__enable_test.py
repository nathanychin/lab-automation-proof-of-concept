from development.classes.Network import *

# Format for host
Transfer = NetServers("10.122.153.158",
                   "calo",
                   "calo",
                   "10.122.153.158")

Device = NetDevice("F241-06-15-COMM", "2029", "admin", "cisco!123", "cisco_ios_telnet", Transfer)

print(Device.__dict__)

#Device.NetConnect()

#Device.NetDisconnect()

