class classWithParents:
    def __init__(self, name):
        self._allParents = set()
        self._allParents.add(name)
        self._directParents = set()
        self._directParents.add(name)
        self._className = name

    def getName(self):
        return self._className

    def getDirectParents(self):
        return self._directParents

    def addParents(self, parentsSet):
        self._allParents.update(parentsSet)

    def addDirectParents(self, parentsSet):
        self._directParents.update(parentsSet)
        self.addParents(parentsSet)

    def isDescendant(self, testClass):
        return testClass.getName() in self._allParents

def findAllParents(classesDct, someClass: classWithParents):
    allParents = set()
    for item in someClass.getDirectParents():
        parentClass = classesDct[item]
        if parentClass.getName() == someClass.getName():
            continue
        allParents.add(parentClass.getName())
        allParents.update(findAllParents(classesDct, parentClass))
    return allParents

if __name__ == '__main__':
    auto = False
    classesDict = {}
    if auto:
        strings = ['winter', 'is', 'coming', 'OMG : winter is coming']
        # strings = ['ArithmeticError', 'ZeroDivisionError : ArithmeticError', 'OSError', 'FileNotFoundError : OSError']
        cntClasses = len(strings)
    else:
        cntClasses = int(input())
    for i in range(cntClasses):
        if auto:
            inputString = strings[i]
        else:
            inputString = input()
        try:
            className = inputString.split(':')[0].strip()
            parents = inputString.split(':')[1].strip().split(' ')
            parents = set(parents)
        except IndexError: #если в строке нет разделителя ':' значит нет и прямых предков
            parents = set()

        someClass = classWithParents(className)
        someClass.addDirectParents(parents)

        classesDict[className] = someClass

    for item in classesDict:
        someClass = classesDict[item]
        someClass.addParents(findAllParents(classesDict, someClass))

    if auto:
        # strings = ['ZeroDivisionError', 'OSError', 'ArithmeticError', 'FileNotFoundError']
        strings = ['winter', 'is', 'coming', 'OMG']
        cntQuestions = len(strings)
    else:
        cntQuestions = int(input())
        strings = [input() for i in range(cntQuestions)]
    for i in range(1, cntQuestions):
        inputString = strings[i]
        for k in range(0, i):
            class1 = classesDict[inputString]
            class2 = classesDict[strings[k]]
            if class1.isDescendant(class2):
                print(class1.getName())
                break



