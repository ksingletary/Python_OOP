"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """Initializing the class with dunder init"""
        self.start = start
        self.incrmnt = start
        
    def generate(self):
        """generate instance method where we increment each time generate called"""
        self.incrmnt = self.incrmnt + 1
        return self.incrmnt - 1
    
    def reset(self):
        """reset method to revert back to original start number"""
        self.incrmnt = self.start

    def __repr__(self):
        """Show repr representation."""

        return f"<SerialGenerator start={self.start} increment={self.incrmnt}>"

