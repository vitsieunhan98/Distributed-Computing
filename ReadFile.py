import numpy as np
from UltilityFunctions import *

class ReadFile:
    def getAdjacencyNodeFeatureMatrix(egoNetworkNodeNumber):
        featMatrix = []
        with open('./facebook/' + str(egoNetworkNodeNumber) + '.feat') as f:
            lines = f.read().splitlines()
            for line in lines:
                line = line.split()
                line = [int(x) for x in line]
                featMatrix.append(line)
    
        return featMatrix
    
    def getEdges(allNodeSimilarityList, egoNetworkNodeNumber):
        fbNode = None
        with open('./facebook/' + str(egoNetworkNodeNumber) + '.edges') as f:
            lines = f.read().splitlines()
            for line in lines:
                line = line.split()
                fbNode = UltilityFunctions.getFBNode(allNodeSimilarityList, 'N' + str(line[0]))
                fbNode.edgeList.append('N' + str(line[1]))
                
                for i in range(len(allNodeSimilarityList)):
                    if allNodeSimilarityList[i].nodeNumber == fbNode.nodeNumber:
                        allNodeSimilarityList[i].edgeList = fbNode.edgeList
                        break

        return allNodeSimilarityList
    
    
