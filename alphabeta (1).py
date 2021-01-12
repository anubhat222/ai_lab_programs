MAX,MIN=1000,-1000

def minimaxab(depth,nodeIndex,maximizingPlayer,values,alpha,beta):
	if depth==3:
		return values[nodeIndex]
	if maximizingPlayer:
		best=MIN
		for i in range(0,2):
			val=minimaxab(depth+1,nodeIndex*2+i,False,values,alpha,beta)
			best=max(best,val)
			alpha=max(alpha,best)
			if beta<=alpha:
				break
		return best
	else:
		best=MAX
		for i in range(0,2):
			val=minimaxab(depth+1,nodeIndex*2+i,True,values,alpha,beta)
			best=min(best,val)
			beta=max(beta,best)
			if beta<=alpha:
				break
		return best
values=[3,5,6,9,1,2,0,-1]
print("The optimal value is :",minimaxab(0,0,True,values,MIN,MAX))

