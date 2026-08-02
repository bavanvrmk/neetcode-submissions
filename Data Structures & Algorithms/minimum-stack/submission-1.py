class MinStack:

    def __init__(self):
        self.lis=[]
        self.minl: List=[]

    def push(self, val: int) -> None:
        if len(self.minl)==0:
            self.minl.append(val)
        else:
            if self.minl[-1]>=val:
                self.minl.append(val)
        self.lis.append(val)

    def pop(self) -> None:
        if self.top()==self.minl[-1]:
            self.minl.pop()
        return self.lis.pop()


    def top(self) -> int:
        return self.lis[-1]

    def getMin(self) -> int:

        return self.minl[-1]

