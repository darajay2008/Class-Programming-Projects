#  tilesSearch.py
#
#  Search for sequence of moves to bring a randomized tile puzzle
#  into order


import time, Queue
from   tiles3x3  import Goal, getMoves, makeMove, manhatten, manhattenwlc, hamming, printPuzzle #modified
from   tilesCost import manhattancost, hammingcost, manhattanwlccost #modified


def hammingsearch(board) :
	global hammingnodeNum #modified
	hammingnodeNum = 1 #modified
	closed  = {}
	queue   = Queue.PriorityQueue()
	orig = (hammingcost(board,0,hammingnodeNum),hammingnodeNum,board,0,None) #modified
	#print("Cost at source", cost(board,0,nodeNum))
	#if orig == Goal : solution = orig
	queue.put(orig)
	closed[orig] = True
	count = 0
	solution = None
	
	while queue and not solution :
		entry = queue.get()   # breadth first if just nodeNum sort
		junk1,junk2,parent,pdepth,grandpa = entry
		count += 1
		empty, moves = getMoves(parent)
		for mov in moves :
			child = makeMove(parent,empty,mov)
			if closed.get(child) : continue
			closed[child] = True
			hammingnodeNum += 1 #modified
			depth = pdepth+1
			priority = hammingcost(child,depth,hammingnodeNum) # low cost = high priority #modified
			newEntry = (priority,hammingnodeNum,child,depth,entry)#modified
			queue.put(newEntry)
			if child == Goal : solution = newEntry
			
	if solution :
		print (count, "entries expanded. Queue still has " , queue.qsize())
		countS = str(count)#i wrote this
		
		hammingoutputfile1.write(countS)#i wrote this
		hammingoutputfile1.write("\n") #i wrote this
		
		# linkage to parents make the path in reverse
		path = []
		while solution :
			path.append(solution[2])
			solution = solution[4]
		path.reverse()
		return path
	else :
		return []
		
def manhattansearch(board) :
	global manhattannodeNum
	manhattannodeNum = 1
	closed  = {}
	queue   = Queue.PriorityQueue()
	orig = (manhattancost(board,0,manhattannodeNum),manhattannodeNum,board,0,None)
	#print("Cost at source", cost(board,0,nodeNum))
	#if orig == Goal : solution = orig
	queue.put(orig)
	closed[orig] = True
	count = 0
	solution = None
	
	while queue and not solution :
		entry = queue.get()   # breadth first if just nodeNum sort
		junk1,junk2,parent,pdepth,grandpa = entry
		count += 1
		empty, moves = getMoves(parent)
		for mov in moves :
			child = makeMove(parent,empty,mov)
			if closed.get(child) : continue
			closed[child] = True
			manhattannodeNum += 1
			depth = pdepth+1
			priority = manhattancost(child,depth,manhattannodeNum) # low cost = high priority
			newEntry = (priority,manhattannodeNum,child,depth,entry)
			queue.put(newEntry)
			if child == Goal : solution = newEntry
			
	if solution :
		print (count, "entries expanded. Queue still has " , queue.qsize())
		countS = str(count)#i wrote this
		
		manhattanoutputfile1.write(countS)#i wrote this
		manhattanoutputfile1.write("\n") #i wrote this
		
		# linkage to parents make the path in reverse
		path = []
		while solution :
			path.append(solution[2])
			solution = solution[4]
		path.reverse()
		return path
	else :
		return []

def manhattanwlcsearch(board) :
	global manhattanwlcnodeNum
	manhattanwlcnodeNum = 1
	closed  = {}
	queue   = Queue.PriorityQueue()
	orig = (manhattanwlccost(board,0,manhattanwlcnodeNum),manhattanwlcnodeNum,board,0,None)
	#print("Cost at source", cost(board,0,nodeNum))
	#if orig == Goal : solution = orig
	queue.put(orig)
	closed[orig] = True
	count = 0
	solution = None
	
	while queue and not solution :
		entry = queue.get()   # breadth first if just nodeNum sort
		junk1,junk2,parent,pdepth,grandpa = entry
		count += 1
		empty, moves = getMoves(parent)
		for mov in moves :
			child = makeMove(parent,empty,mov)
			if closed.get(child) : continue
			closed[child] = True
			manhattanwlcnodeNum += 1
			depth = pdepth+1
			priority = manhattanwlccost(child,depth,manhattanwlcnodeNum) # low cost = high priority
			newEntry = (priority,manhattanwlcnodeNum,child,depth,entry)
			queue.put(newEntry)
			if child == Goal : solution = newEntry
			
	if solution :
		print (count, "entries expanded. Queue still has " , queue.qsize())
		countS = str(count)#i wrote this
		
		manhattanwlcoutputfile1.write(countS)#i wrote this
		manhattanwlcoutputfile1.write("\n") #i wrote this
		
		# linkage to parents make the path in reverse
		path = []
		while solution :
			path.append(solution[2])
			solution = solution[4]
		path.reverse()
		return path
	else :
		return []


		
def main() :
	import sys, re 
	# board is a 9 digit board
	
	global hammingoutputfile1 #i wrote this
	global manhattanoutputfile1 #i wrote this
	global manhattanwlcoutputfile1 #i wrote this
	
	hammingoutputfile1 = open("HammingNodesExpanded.txt", "w")#i wrote this
	hammingoutputfile2 = open("HammingSolutionLength.txt", "w")#i wrote this
	
	manhattanoutputfile1 = open("ManhattanNodesExpanded.txt", "w")#i wrote this
	manhattanoutputfile2 = open("ManhattanSolutionLength.txt", "w")#i wrote this
	
	manhattanwlcoutputfile1 = open("ManhattanwlcNodesExpanded.txt", "w")#i wrote this
	manhattanwlcoutputfile2 = open("ManhattanwlcSolutionLength.txt", "w")#i wrote this
	
	#i wrote the following
	stateArray = ['8_6547231','_12345678','7245_6831','12356_784','1437_6582','182_43765','12534_678','12_453786','3674_8152','3461_2758','54_618732','12374_865','782356_14','52714368_','2156_8347','287_46153','42168_753','6_1842735','54182_376','63581724_']
		
	for index in range(len(stateArray)): # i wrote this
		board = re.sub("[^_1-9]","",stateArray[index])# i modified this code 
		startTime = time.time()
		hammingpath = hammingsearch(board) #modified
		endTime = time.time()-startTime
		print ("tilesSearch.py:", len(hammingpath),"moves")#modified
		print ("took", endTime, "secs")
		print (hammingpath)#modified
		hammingpathLen = str(len(hammingpath)) #i wrote this
		hammingoutputfile2.write(hammingpathLen) #i wrote this
		hammingoutputfile2.write("\n") #i wrote this
		
	
	for index in range(len(stateArray)): # i wrote this
		board = re.sub("[^_1-9]","",stateArray[index])# i modified this code 
		startTime = time.time()
		manhattanpath = manhattansearch(board) #modified
		endTime = time.time()-startTime
		print ("tilesSearch.py:", len(manhattanpath),"moves")#modified
		print ("took", endTime, "secs")
		print (manhattanpath)#modified
		manhattanpathLen = str(len(manhattanpath)) #i wrote this
		manhattanoutputfile2.write(manhattanpathLen) #i wrote this
		manhattanoutputfile2.write("\n") #i wrote this
	
	
	for index in range(len(stateArray)): # i wrote this
		board = re.sub("[^_1-9]","",stateArray[index])# i modified this code 
		startTime = time.time()
		manhattanwlcpath = manhattanwlcsearch(board) #modified
		endTime = time.time()-startTime
		print ("tilesSearch.py:", len(manhattanwlcpath),"moves")#modified
		print ("took", endTime, "secs")
		print (manhattanwlcpath)#modified
		manhattanwlcpathLen = str(len(manhattanwlcpath)) #i wrote this
		manhattanwlcoutputfile2.write(manhattanwlcpathLen) #i wrote this
		manhattanwlcoutputfile2.write("\n") #i wrote this
	
	
	hammingoutputfile1.close() #i wrote this
	hammingoutputfile2.close() #i wrote this
	
	manhattanoutputfile1.close() #i wrote this
	manhattanoutputfile2.close() #i wrote this
	
	manhattanwlcoutputfile1.close() #i wrote this
	manhattanwlcoutputfile2.close() #i wrote this


if __name__ == "__main__" : main()
