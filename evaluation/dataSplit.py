from random import random
from tool.file import FileIO
class DataSplit(object):

    def __init__(self):
        pass

    @staticmethod
    def dataSplit(data,test_ratio = 0.3,output=False,path='./',order=1):
        testSet = []
        trainingSet = []
        for entry in data:
            if random() < test_ratio:
                testSet.append(entry)
            else:
                trainingSet.append(entry)

        if output:
            FileIO.writeFile(path,'testSet['+str(order)+']',testSet)
            FileIO.writeFile(path, 'trainingSet[' + str(order) + ']', trainingSet)
        return trainingSet,testSet

    @staticmethod
    def crossValidation(data,k,output=False,path='./',order=1):
        if k<0 or k>10:
            k=3
        trainingSet = []
        testSet = []
        for i in range(k):
            trainingSet.append([])
            testSet.append([])
        for i,line in enumerate(data):
            testSet[i%k].append(line)
            for n in range(k):
                if n!=i%k:
                    trainingSet[n].append(line)
        return trainingSet,testSet


