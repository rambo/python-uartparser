"""UART Parser module errors"""
from exceptions import RuntimeError

class UARTParserError(RuntimeError):
    pass

class TimeoutError(UARTParserError):
    def __init__(self, command, time, *args, **kwargs):
        self.command = command
        self.time = time
        super(TimeoutError, self).__init__(str(self), *args, **kwargs)

    def __str__(self):
        return "'%s' timed out after %f seconds" % (self.command, self.time)
