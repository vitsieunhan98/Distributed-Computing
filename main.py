from ReadFile import *
import Circle
import FacebookNode
from Cluster import *
from UltilityFunctions import *
import time
import sys

#value = input('Please enter any one Ego node network number from the following list and say enter:\nYour choice is\n1. 0\n2. 107\n3. 1684\n4. 1912\n5. 3437\n6. 348\n7. 3980\n8. 414\n9. 686\n10. 698\n')
value = sys.argv[1]
value = int(value)

startTime = time.time()
allNodeSimilarityList = []

addjacencyMatrix = ReadFile.getAdjacencyNodeFeatureMatrix(value)
allNodeSimilarityList = UltilityFunctions.calculateJacardCoeffiecient(addjacencyMatrix)
print("Total number of nodes is Ego Network " + str(value) + " are " + str(len(allNodeSimilarityList)))

allNodeSimilarityList = ReadFile.getEdges(allNodeSimilarityList, value)
allNodeSimilarityList = UltilityFunctions.sortArrayListByEdgeCount(allNodeSimilarityList)

allCircles = []
allCircles = Cluster.clusterData(allNodeSimilarityList)
UltilityFunctions.writeCirclesToFile(allCircles)

endTime = time.time()
print('Total execution time: ' + str(endTime - startTime) + 's')