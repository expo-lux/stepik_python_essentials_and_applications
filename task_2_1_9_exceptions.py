class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x <= 0:
            raise NonPositiveError(str(x) + " is not positive")
        else:
            super().append(x)

myList = PositiveList()
myList.append(1)
myList.append(-1)