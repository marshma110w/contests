from random import randint

class Stack:
    def __init__(self):
        self.array = []

    def push(self, number):
        self.array.append(number)
    
    def pop(self):
        if len(self.array) == 0:
            print('EMPTY!!')
            return
        return(self.array.pop())
    
    def __repr__(self):
        return "{}\nlength: {}".format(self.array, len(self.array))

    