class MyQueue:

    def __init__(self):
        self.inp = []
        self.out = []
        
    def push(self, x: int) -> None:
        while self.inp:
            self.out.append(self.inp.pop())
        self.inp.append(x)
        while self.out:
            self.inp.append(self.out.pop())

    def pop(self) -> int:
        return self.inp.pop()

    def peek(self) -> int:
        return self.inp[-1]

    def empty(self) -> bool:
        return not self.inp
