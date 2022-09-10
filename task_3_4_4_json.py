import json
import sys


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
    autoTest = True
    if autoTest:
        text = '[{"name": "B", "parents": ["A", "C"]}, {"name": "A", "parents": []}, {"name": "C", "parents": ["A"]}]'
        obj = json.loads(text)
    else:
        text = sys.stdin
        obj = json.load(text)
    classesDict = {}
    for item in obj:
        className = item['name']
        parents = set(item['parents'])
        someClass = classWithParents(className)
        someClass.addDirectParents(parents)
        classesDict[className] = someClass

    for item in classesDict:
        someClass = classesDict[item]
        someClass.addParents(findAllParents(classesDict, someClass))

    classesDict = dict(sorted(classesDict.items()))

    for item in classesDict:
        someClass = classesDict[item]
        cnt = 0
        for value in classesDict.values():
            if value.isDescendant(someClass):
                cnt += 1
        print(f"{someClass.getName()} : {cnt}")
