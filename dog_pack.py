# Implement DogPack
class DogPack:
    '''
    Represents a list of Dogs
    '''

    def __init__(self):
        self._dogs = []

    def add_dog(self, dog):
        self._dogs.append(dog)

    def all_bark(self):
        for dog in self._dogs:
            dog.bark()