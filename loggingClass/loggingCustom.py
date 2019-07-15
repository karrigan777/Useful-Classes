class Logger:

    typeLogging={"Info":0, "Warning":1, "Error":2}

    def __init__(self):
        self.currentLoggingLevel=0
    
    def setLevel(self,userLevel):
        if(self.typeLogging[userLevel]!=""):
            self.currentLoggingLevel=(self.currentLoggingLevel | (1 << self.typeLogging[userLevel]+1))-1
        else:
            print("Invalid Log Level")
    
    def turnOnLevel(self,*kwargs):
        for userLevel in kwargs:
            if(self.typeLogging[userLevel]!=""):
                self.currentLoggingLevel=self.currentLoggingLevel | (1 << self.typeLogging[userLevel])
    
    def Info(self, logMessage):
        self.log(logMessage,"Info")
    
    def Error(self, logMessage):
        self.log(logMessage,"Error")

    def Warning(self, logMessage):
        self.log(logMessage,"Warning")

    def log(self,logMessage, logType):
        if(self.currentLoggingLevel==-1):
            print("Set Logging Level First")
            return
        if(self.currentLoggingLevel & (1 << self.typeLogging[logType])):
            print(" [ "+logType+" ] : "+logMessage)