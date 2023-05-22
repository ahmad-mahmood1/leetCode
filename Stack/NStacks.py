class NStack:
    def __init__(self, n, s):
        self.top = [-1 for _ in range(n)]
        self.next = [i + 1 if i != s - 1 else -1 for i in range(s)]
        self.arr = [0] * s
        self.freespot = 0

        pass

    def push(self, x, m):
        if self.freespot == -1:
            return -1
        index = self.freespot

        self.freespot = self.next[index]

        self.arr[index] = x

        self.next[index] = self.top[m - 1]

        self.top[m - 1] = index

        return True

    def pop(self, m):
        if self.top[m - 1] == -1:
            return -1

        index = self.top[m - 1]

        self.top[m - 1] = self.next[index]

        self.next[index] = self.freespot

        self.freespot = index

        return self.arr[index]


nstack = NStack(3,6)


nstack.push(20, 1)

print(nstack)
