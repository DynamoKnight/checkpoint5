# Write your solution here!
class Pair:
    '''
    Represents a tuple-like object
    '''
    def __init__(self, val1, val2):
        self._val1 = val1
        self._val2 = val2

    def __repr__(self):
        return f'({self._val1}, {self._val2})'

    def __eq__(self, other):
        return ((self._val1 == other._val1) and (self._val2 == other._val2))

    def __getitem__(self, i):
        return self._val1 if i == 0 else self._val2
    
    def __setitem__(self, i, v):
        print('Error: Pair is immutable!')