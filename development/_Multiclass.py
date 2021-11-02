class NewDevice:
    def __init__(self, NAME = "", PORT = ""):
        self.NAME = NAME
        self.PORT = PORT
        self.list = [self.NAME, self.PORT]
        
    def PrintMe(self):
        print("Class made")
    
class DeviceInfo:
    def __init__(self, NAME = "", PORT = ""):
        self.NAME = NAME
        self.PORT = PORT

        
        
    def SetDeviceInfo(self):
        self.NAME = input("Enter name: ")
        self.PORT = input("Enter port: ") 
        self.list = [self.NAME, self.PORT]
        return self.list
    
    
my_list = DeviceInfo().SetDeviceInfo()
print("DeviceInfo object made")
print(my_list)

My_Device = NewDevice(my_list[0], my_list[1])
My_Device.PrintMe()
