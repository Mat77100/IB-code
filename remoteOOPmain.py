#main file

class remoteCtrlBtn:
    def __init__(self, appName, btnID, appID):
        self.appName = appName
        self.btnID = btnID
        self.appID = appID
    
    def press(self):
        print(f"[{self.appName} BUTTON PRESSED]")
        print(f"[BUTTON ID = {self.btnID}")
        print(f"[APP ID = {self.appID}]")
        print("[STARTING APP]")
        print(f"TV is now playing {self.appName}")
        print("")
    