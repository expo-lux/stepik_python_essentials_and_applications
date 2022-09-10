class ExtendedStack(list):
    def sum(self):
        if len(self) >= 2:
            value = self.pop() + self.pop()
            self.append(value)
            return value
        else:
            return None
        # операция сложения

    def sub(self):
        if len(self) >= 2:
            value = self.pop() - self.pop()
            self.append(value)
            return value
        else:
            return None
        # операция вычитания

    def mul(self):
        if len(self) >= 2:
            value = self.pop() * self.pop()
            self.append(value)
            return value
        else:
            return None
        # операция умножения

    def div(self):
        if len(self) >= 2:
            value = self.pop() // self.pop()
            self.append(value)
            return value
        else:
            return None
        # операция целочисленного деления


if __name__ == '__main__':
    x = ExtendedStack()
    x.append(1)
    x.append(2)
    x.sum()
    print(x.pop())
    x.clear()
    x.append(1)
    x.append(2)
    x.sub()
    print(x.pop())
    x.clear()
    x.append(1)
    x.append(2)
    x.mul()
    print(x.pop())
    x.clear()
    x.append(1)
    x.append(2)
    x.div()
    print(x.pop())
