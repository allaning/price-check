from Logger import Logger

class ConsoleLogger(Logger):
    """ Log messages to console """

    def __init__(self, logger):
        self.baseLogger = None
        if logger != None:
            self.baseLogger = logger

    def logInfo(self, msg):
        """ Log info message """
        if self.baseLogger != None:
            self.baseLogger.logInfo(msg)
        print(msg)

    def getLog(self):
        """ Returns the log message, if any """
        pass

