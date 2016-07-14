from Logger import Logger

class StringBuilderLogger(Logger):
    """ Build a string based on messages """

    def __init__(self, logger):
        self.baseLogger = None
        if logger != None:
            self.baseLogger = logger
        self.message = ""

    def log_info(self, msg):
        """ Log info message """
        if self.baseLogger != None:
            self.baseLogger.log_info(msg)
        self.message += msg
        self.message += "\n"

    def get_log(self):
        """ Returns the log message, if any """
        return self.message

