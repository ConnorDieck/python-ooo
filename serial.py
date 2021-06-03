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
    def __init__(self, start):
        "Creates a serial number generator"
        self.start = start
        self.count = 0
    
    def generate(self):
        "Generates the starter serial number and adds one to count"
        self.count +=1
        return self.start + self.count - 1
    
    def reset(self):
        "Resets counter number"
        self.count = 0
