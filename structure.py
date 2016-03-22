# -*- coding: utf-8 -*-
from collections import Iterable
from collections import defaultdict
def inverseIndexDict(sources, sourceIndex, targetKey, allowedTargets = []):
    '''
    used to generate inverse index
    sources: a group of doc
    sourceIndex: the index of doc
    targetKey: the key that we want to generate reverse index for
    allowedIndexes: a filter, if we just need to find some specified keys,
                    pass them by allowedTargets
    '''
    inverseIndex = defaultdict(lambda:[])
    if allowedTargets:
        filterOn = True
        allowedTargetset = set(allowedTargets)
    else:
        filterOn = False
    for source in sources:
        if source.get(targetKey):
            if isinstance(source[targetKey],Iterable):
                for target in source[targetKey]:
                    if filterOn and (not target in allowedTargetset):
                        continue
                    inverseIndex[target].append(source[sourceIndex])
            else:
                if filterOn and (not source[targetKey] in allowedTargetset):
                    continue
                inverseIndex[target].append(source[targetKey])
    return inverseIndex

if __name__ == '__main__':
    test = [{'name':"John", "class":"A"},
            {'name':"Mike", "class":"B"},
            {'name':"Kyon", "class":"A"},
            {'name':"Doug", "class":["A","C"]}]
    print iiDict(test, "name", "class")