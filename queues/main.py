class Queue:
    def __init__(self):
        self.queue = []
    
    def enque(self, val) -> None:
        self.queue.append(val)

    def deque(self) -> None:
        self.queue.pop(0)

    def peek(self):
        return self.queue[0]
    
    def view(self):
        print(self.queue)
    

