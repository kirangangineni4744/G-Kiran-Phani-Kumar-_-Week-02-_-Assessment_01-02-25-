class Electronics:
    def __init__(self):
        self.brand = "General Brand"

    def power_on(self):
        print("Device is powering on")

class MobileDevice(Electronics):
    def __init__(self):
        super().__init__()

    def power_on(self):
        print(f"{self.brand} mobile device is powering on.") 

class SmartPhone(MobileDevice):
    def __init__(self):
        super().__init__()

    def power_on(self):
        print(f"{self.brand} smartphone is powering on.")

smartphone=SmartPhone()
smartphone.power_on()
