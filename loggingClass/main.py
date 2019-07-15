from loggingCustom import *

def Main():    
    logger=Logger()
    logger.setLevel("Info")
    logger.turnOnLevel("Error")
    logger.log("Sample Info 1", "Info")
    logger.log("Sample Warning 1", "Warning")
    logger.log("Sample Error 1", "Error")
    logger.Info("Sample Info 2")
    logger.Warning("Sample Warning 2")
    logger.Error("Sample Error 2")

    
if __name__ == "__main__":
    Main()