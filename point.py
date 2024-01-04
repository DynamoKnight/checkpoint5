# Create a Point class as per instructions
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
      
    def __repr__(self):
        print("I am me")

    def display(self):
        print(f'({x},{y})')

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y
    