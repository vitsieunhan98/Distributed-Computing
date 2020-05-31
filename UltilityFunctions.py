import numpy as np
from FacebookNode import *
from collections import defaultdict 

class UltilityFunctions:
    def mapFunction(line):
        line = line.split(" ")
        line = [int(x) for x in line]
        return line
        
    def calculateJacardCoeffiecient(adjacencyMatrix):
        allNodeSimilarity = []
        noOfRows = len(adjacencyMatrix)
        jaccardCoeff = 0.0
        topN = 0
        

        if noOfRows <= 100:
            topN = 8
        elif noOfRows > 100 or noOfRows <= 300:
            topN = 15
        elif noOfRows > 300 or noOfRows < 500:
            topN = 25
        else: 
            topN = 25
        
        for k in range(noOfRows):
            similarityMap = defaultdict()
            tempSimMap = defaultdict()
            topNMap = defaultdict()
            nodeNumber = 'N' + str(adjacencyMatrix[k][0])
            temp = 0.0
            total = 0.0

            for i in range(noOfRows):
                if i != k:
                    kthFeat = adjacencyMatrix[k][1:]
                    ithFeat = adjacencyMatrix[i][1:]
                    for j in range(len(kthFeat)):
                        if kthFeat[j] == 1 and ithFeat[j] == 1:
                            total = total + 1
                            temp = temp + 1
                        elif kthFeat[j] == ithFeat[j] and kthFeat[j] == 0:
                            continue
                        else:
                            total = total + 1
                else:
                    continue
                
                jaccardCoeff = temp/total
                jaccardCoeff = round(jaccardCoeff * 10000)/10000
                
                similarityMap['N' + str(adjacencyMatrix[i][0])] = jaccardCoeff
                tempSimMap['N' + str(adjacencyMatrix[i][0])] = jaccardCoeff
            
            tempSimMap = sorted(tempSimMap.items(), key=lambda k: k[1], reverse=True)
            
            count = 0
            for k in tempSimMap:
                topNMap[k[0]] = k[1]
                count = count + 1
                if count == topN:
                    break
            
            tempList = []
            newNode = FacebookNode(nodeNumber, similarityMap, topNMap, tempList)
            allNodeSimilarity.append(newNode)

        return allNodeSimilarity
        
    # def writeFacebookNodesToFile(allFBNodes):
    
    def writeCirclesToFile(allCircles):
        print('Number of circles: ' + str(len(allCircles)))


    def getFBNode(allNodeSimilarityList, nodeNumber):
        fbNode = None
        for facebookNode in allNodeSimilarityList:
            if facebookNode.nodeNumber == nodeNumber:
                fNodeNumber = facebookNode.nodeNumber
                fSimilarityMap = facebookNode.similarityMap
                fTopNMap = facebookNode.topNMap
                fEdgeList = facebookNode.edgeList
                fbNode = FacebookNode(fNodeNumber, fSimilarityMap, fTopNMap, fEdgeList)
        
        return fbNode
        
    
    def sortArrayListByEdgeCount(allNodeSimilarityList):
        allNodeDict = defaultdict()
        for node in allNodeSimilarityList:
            allNodeDict[node] = len(node.edgeList)

        sortedList = sorted(allNodeDict.items(), key=lambda k: k[1], reverse=True)

        return list([k[0] for k in sortedList])