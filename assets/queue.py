class Queue:
    def __init__(self, n):
        self.n = n
        self.array = [0 for _ in range(n)]
        self.head = self.tail = 0
        self.length = 0
    
    def __repr__(self):
        return "{}\nhead: {}\ntail:{}\nlength: {}".format(self.array, self.head, self.tail, self.length)
    
    def push(self, number):
        if self.head == self.tail and self.length > 0:
            print('OWERFLOW!!')
            return
        self.array[self.head] = number
        self.head = (self.head + 1) % self.n
        self.length += 1


    def pop(self):
        if self.length == 0:
            print('EMPTY!!')
            return
        res = self.array[self.tail]
        self.tail = (self.tail + 1) % self.n
        self.length -= 1
        return res
