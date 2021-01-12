import math
def minimax(currentDepth,nodeIndex,maxTurn,scores,treeDepth):
	if(currentDepth==treeDepth):
		return scores[nodeIndex]
	if(maxTurn):
		return 	max(minimax(currentDepth+1,nodeIndex*2,False,scores,treeDepth),minimax(currentDepth+1,nodeIndex*2+1,False,scores,treeDepth))
	else:
		return min(minimax(currentDepth+1,nodeIndex*2,True,scores,treeDepth),minimax(currentDepth+1,nodeIndex*2+1,True,scores,treeDepth))
		
scores=[3,5,2,9,12,5,23,23]
treeDepth=math.log(len(scores),2)
print("The optimal value is :",minimax(0,0,True,scores,treeDepth))

