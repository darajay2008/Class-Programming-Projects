import time, Queue
from numpy import inf
from   tiles3x3  import Goal, getMoves, makeMove, manhattenwlc, printPuzzle #modified
from   idaStarTilesCost import manhattanwlccost #modified

def IDAStar(START):
	bound = manhattanwlccost(START, Goal)
	global path
	global removed
	removed = 0
	path = []
	#global solLength
	#solLength = 0
	global count
	count = 0
	while (1):
		
		temp = IDASearch(START, 0, bound)
		#print("Heuristic: = ", bound)
		if (temp == -1):
			#solLength = solLength + 1
			print("Solution found....")
			solLength = len (path)
			print(solLength, "is the length of the solution path")
			solLengthS = str(solLength)
			idastaroutputfile2.write(solLengthS) #i wrote this
			idastaroutputfile2.write("\n") #i wrote this
			break
		if (temp == float(inf)): 
			return None
		bound = temp
		#removed = 0
		count =0
		path = []
		#solLength = solLength + 1
	return temp
 
def IDASearch(node, g, bound):
	#solution = None
	#count = count + 1
	#global solLength
	#global removed
	global count
	global path
	f = 0
	f = g + manhattanwlccost(node,Goal)
	if f > bound:
		return f
	if node == Goal:
		path.append(node)
		#solLength = solLength + 1
		return -1
	min = float(inf)
	empty, moves = getMoves(node)
	count = count + 1
	for mov in moves:
		
		child = makeMove(node,empty,mov)
		if child not in path:
			path.append(child)
			#define a counter to count number of nodes expanded
			temp = IDASearch(child, g + manhattanwlccost(node,child), bound)
			if temp == -1 :
				#solLength = solLength + 1
				return temp
				break
			if temp < min : 
				min = temp
			path.remove(child)
				#removed = removed + 1
	return min	
	

			

def main() :
	import sys, re 
	# board is a 9 digit board
	global count
	global idastaroutputfile1 #i wrote this
	global idastaroutputfile2 #i wrote this
	idastaroutputfile1 = open("IDAStarNodesExpanded.txt", "w")#i wrote this
	idastaroutputfile2 = open("IDASolutionLength.txt", "w")#i wrote this	
	#i wrote the following
	
	stateArray = ['8_6547231','_12345678','7245_6831','12356_784','1437_6582','182_43765','12534_678','12_453786','3674_8152','3461_2758','54_618732','12374_865','782356_14','52714368_','2156_8347','287_46153','42168_753','6_1842735','54182_376','63581724_']
	
	for index in range(len(stateArray)):
		board = re.sub("[^_1-9]","",stateArray[index])# i modified this code 
		startTime = time.time()
		result = 0
		result = IDAStar(board) #modified
		endTime = time.time()-startTime
		#print ("idastar.py:", len(idastarpath),"moves")#modified
		print ("took", endTime, "secs")
		#print (idastarpath)#modified
		#idastarpathLen = str(len(idastarpath)) #i wrote this
		#idastaroutputfile2.write(idastarpathLen) #i wrote this
		#idastaroutputfile2.write("\n") #i wrote this
		
		print (count, "entries expanded.")
		countS = str(count)#i wrote this
		idastaroutputfile1.write(countS)#i wrote this
		idastaroutputfile1.write("\n") #i wrote this
		
	idastaroutputfile1.close() #i wrote this
	idastaroutputfile2.close() #i wrote this
		
if __name__ == "__main__" : main()