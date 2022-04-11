class Door():

    def __init__(self):
        self.is_opened = False

    def open_door(self):
        self.is_opened = True
        print("Door is Open")



    def close_door(self):
        self.is_opened = False
        print("Door is closed")

class BlockedDoor(Door):
    def __init__(self):
            pass

    def open_door(self):
        print("This is an Error")


    def close_door(self):
        print("This is an Error")
