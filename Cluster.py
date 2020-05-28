from Circle import *
from UltilityFunctions import *

def calculateConnectionStrength(circle, currentNode, allNodeSimilarityList):
        connectionStrength = 0
        n = len(circle.listNode)
        k = 0
        for m in range(n):
            node = UltilityFunctions.getFBNode(allNodeSimilarityList, circle.listNode[m])
            if currentNode.nodeNumber in node.edgeList:
                k = k + 1
        
        connectionStrength = 1.0 * k/n

        return connectionStrength

class Cluster:
    def clusterData(allNodeSimilarityList):
        topNCount = 0
        topNCountThreshold = 0

        noOfRows = len(allNodeSimilarityList)

        allCircles = []

        threshold = len(allNodeSimilarityList[0].edgeList)
        threshold = threshold/2

        if noOfRows <= 100:
            topNCountThreshold = 3
        elif noOfRows > 100 and noOfRows <= 300:
            topNCountThreshold = 6
        elif noOfRows > 300 and noOfRows < 500:
            topNCountThreshold = 10
        else:
            topNCountThreshold = 15
        
        for s in range(len(allNodeSimilarityList) - 1):
            if len(allNodeSimilarityList[s].edgeList) >= threshold:
                circle = Circle('Circle' + str(s+1), [])
                circle.listNode.append(allNodeSimilarityList[s].nodeNumber)
                
                for i in range(s+1, len(allNodeSimilarityList) - 1, 1):
                    currentNode = allNodeSimilarityList[i]
                    
                    connectionStrength = calculateConnectionStrength(circle, currentNode, allNodeSimilarityList)
                    if connectionStrength >= 0.5:
                        for k in range(len(circle.listNode)):
                            compareNode = UltilityFunctions.getFBNode(allNodeSimilarityList, circle.listNode[k])

                            for nodeNumber in currentNode.topNMap.keys():
                                if nodeNumber in compareNode.topNMap.keys():
                                    topNCount = topNCount + 1
                            
                            if topNCount < topNCountThreshold:
                                break

                            if k == len(circle.listNode) - 1:
                                circle.listNode.append(currentNode.nodeNumber)
                                break

                            topNCount = 0
                
                allCircles.append(circle)
        
        return allCircles
    
    