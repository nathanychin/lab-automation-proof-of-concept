import json
from development.classes.Network import *

Transfer = NetServers("10.122.153.158",
                      "calo",
                      "calo",
                      "10.122.153.158")

Device1 = NetDevice("10.0.0.1", "2029", "admin",
                   "cisco!123", "cisco_ios_telnet", Transfer)

Device2 = NetDevice("10.0.0.2", "2030", "admin",
                   "cisco!123", "cisco_ios_telnet", Transfer)

Device3 = NetDevice("10.0.0.3", "2031", "admin",
                   "cisco!123", "cisco_ios_telnet", Transfer)

ManagedDevices = [{'Device1': Device1.__dict__['Device']},
                  {'Device2': Device2.__dict__['Device']}, 
                  {'Device3': Device3.__dict__['Device']}]

jsonString = json.dumps(ManagedDevices)
jsonFile = open("_data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()
