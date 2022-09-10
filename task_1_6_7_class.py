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
    auto = True
    classesDict = {}
    if auto:
        # strings = ['animal', 'panda : animal', 'A', 'B', 'B : A', 'X : A B', 'M : X', 'J : X']
        strings = ['form', 'polygon: form', 'button : polygon', 'triangle : polygon', 'styledButton : button', 'A', 'B', 'B : A', 'X : A B', 'M : X', 'J : X']
        # strings = ['A', 'J', 'E : A', 'K : A', 'F : J', 'D : E K', 'M : K', 'C : F D M', 'B : C']
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
        # 'A B' является ли B потомком A == А предком B ?
        strings = ['A X', 'A J', 'B X', 'Y A', 'A B', 'animal panda', 'triangle form', 'form triangle', 'Z Z']
        # strings = ['A B', 'K B', 'M J', 'M M', 'J C']
        cntQuestions = len(strings)
    else:
        cntQuestions = int(input())
    for i in range(cntQuestions):
        if auto:
            inputString = strings[i]
        else:
            inputString = input()
        try:
            className1 = inputString.split(' ')[0]
            className2 = inputString.split(' ')[1]
            class1 = classesDict[className1]
            class2 = classesDict[className2]
            if class2.isDescendant(class1):
                print('Yes')
            else:
                print('No')
        except KeyError:
            print('No')



