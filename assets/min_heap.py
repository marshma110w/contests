class Heap:
    def __init__(self):
        self.array = [0, 0]
        self.size = 2
        self.first_empty_index = 0
        self.hash = {}

    def add(self, number):
        if self.first_empty_index >= self.size:
            self.array += [0 for _ in range(len(self.array))]
            self.size *= 2

        i = self.first_empty_index
        self.array[self.first_empty_index] = number
        self.hash[number] = i
        self.shift_up(i)
        self.first_empty_index += 1

    def shift_up(self, i):
        while i > 0 and self.array[i] < self.array[(i - 1) // 2]:            
            self.array[i], self.array[(i - 1) // 2] = self.array[(i - 1) // 2], self.array[i]
            self.hash[self.array[i]] = i
            self.hash[self.array[(i - 1)// 2]] = (i - 1) // 2
            i = (i - 1) // 2

    def shift_down(self, i):
        while i * 2 + 2 < self.first_empty_index:
            if self.array[i * 2 + 1] < self.array[i * 2 + 2]:
                min_n = self.array[i * 2 + 1]
                min_i = i * 2 + 1
            else:
                min_n = self.array[i * 2 + 2]
                min_i = i * 2 + 2
            
            if min_n >= self.array[i]:
                break

            self.array[i], self.array[min_i] = self.array[min_i], self.array[i]
            self.hash[self.array[i]] = i
            self.hash[self.array[min_i]] = min_i
            i = min_i

        if i * 2 + 1 < self.first_empty_index and self.array[i * 2 + 1] < self.array[i]:
            self.array[i * 2 + 1], self.array[i] = self.array[i], self.array[i * 2 + 1]

    def pop(self):
        res = self.array[0]

        self.array[0] = self.array[self.first_empty_index - 1]

        self.shift_down(0)

        self.array[self.first_empty_index - 1] = 0
        self.first_empty_index -= 1
        return res
    
    def pop_by_value(self, number):
        index = self.hash[number]
        self.array[index] = self.array[self.first_empty_index - 1]

        self.shift_down(index)

        del self.hash[number]
        self.array[self.first_empty_index - 1] = 0
        self.first_empty_index -= 1 
    

    def __repr__(self):
        return f'{self.array[:self.first_empty_index]}\n{self.hash}'
