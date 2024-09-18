import sys

class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        sub = self.s[i:j+1]  
        str_rem = self.s[:i] 
        
        if j+1 < len(self.s):
            str_rem = str_rem + self.s[j+1:]
        
        if k < len(str_rem):
            self.s = str_rem[:k] + sub + str_rem[k:]
        else:
            self.s = str_rem + sub


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())