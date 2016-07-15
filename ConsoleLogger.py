from Logger import Logger

class ConsoleLogger(Logger):
    """ Log messages to console """

    def __init__(self, logger):
        self.baseLogger = None
        if logger != None:
            self.baseLogger = logger

    def log_info(self, msg):
        """ Log info message """
        if self.baseLogger != None:
            self.baseLogger.log_info(msg)
        print(msg)

    def get_log(self):
        """ Returns the log message, if any """
        return ""

