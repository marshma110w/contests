# Longest coomon subsequence

class Lcs:
    def __init__(self, word1, word2):
        self.word1 = word1
        self.word2 = word2
        self.n = len(word1)
        self.m = len(word2)
        self.table = [[0 for j in range(self.m + 1)] for i in range(self.n + 1)]

    def count(self):
        for i in range(self.n):
            for j in range(self.m):
                if self.word1[i] == self.word2[j]:
                    self.table[i][j] = self.table[i-1][j-1] + 1
                else:
                    self.table[i][j] = max(self.table[i-1][j], self.table[i][j-1])
        return self.table[self.n-1][self.m-1]
    
    def track(self):
        track = ''
        i = self.n - 1
        j = self.m - 1
        while i >= 0 and j >= 0:
            if self.word1[i] == self.word2[j]:
                track = self.word1[i] + track
                i -= 1
                j -= 1
            elif i == 0:
                j -= 1
            elif j == 0:
                i -= 1
            else:
                if self.table[i][j-1] > self.table[i-1][j]:
                    j -= 1
                else:
                    i -= 1
        return track

                
    def print_table(self):
        print(' ' * 5, end='')
        for j in range(self.m):
            print(f'{self.word2[j]:5}', end='')
        print()
        for i in range(self.n):
            print(self.word1[i], end='')
            for j in range(self.m):
                print(f'{self.table[i][j]:5}', end='')
            print()
        print()
    


w1 = input('word 1: ')
w2 = input('word 2: ')

s = Lcs(w1, w2)

print(f'LCS lenght: {s.count()}')
s.print_table()
print(f'LCS: {s.track()}')
