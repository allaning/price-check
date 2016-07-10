from Logger import Logger

class StringBuilderLogger(Logger):
    """ Build a string based on messages """

    def __init__(self, logger):
        self.baseLogger = None
        if logger != None:
            self.baseLogger = logger
        self.message = ""

    def logInfo(self, msg):
        """ Log info message """
        if self.baseLogger != None:
            self.baseLogger.logInfo(msg)
        self.message += msg
        self.message += "\n"

    def getLog(self):
        """ Returns the log message, if any """
        return self.message

