class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.arr = [None] * self.capacity

    def get(self, i: int) -> int:
        if i >= 0 and i < len(self.arr):
            return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i >= 0 and i < len(self.arr):
            self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        arr = [None] * self.capacity

        for i in range(self.length):
            arr[i] = self.arr[i]
        self.arr = arr


    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity