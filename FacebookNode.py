from collections import defaultdict 

class FacebookNode:
    def __init__(self, nodeNumber, similarityMap, topNMap, edgeList):
        self.nodeNumber = nodeNumber
        self.similarityMap =  similarityMap
        self.topNMap = topNMap
        self.edgeList = edgeList