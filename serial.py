"""Python serial number generator."""

import ssl


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
    def __init__(self, start, current = None):
        '''constructor for serial. sets starting and current values'''
        self.start = start
        if current:
            self.current = current
        else:
            self.current = self.start
            
    def __repr__():
        return "SerialGenerator(start={self.start}, current={self.current})"
        
    def generate(self):
        '''increments the current value and returns the previous current value
        (like this.current++ in languages where expressions-with-side-effects are more common)
        
        >>> serial = SerialGenerator(start=100)
        
        >>> serial.generate() == serial.start
        True
        
        >>> serial.generate() == serial.start
        False
        
        >>> serial.generate() == serial.start + 2
        True
        '''
        to_return = self.current
        self.current += 1
        return to_return

    def reset(self):
        '''resets the current value to the starting value
        >>> serial = SerialGenerator(start=100)
        
        >>> type(serial.generate()) == int
        True
        
        >>> serial.current == serial.start
        False
        
        >>> serial.reset()
        
        >>> serial.current == serial.start
        True
        '''
        self.current = self.start
