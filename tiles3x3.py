# tiles3x3.py
#
import re
# Squares are numbered from 0-8   012
#                                 345
#                                 678
#
# When square x is blank, squares that can slide in are:
#
_slides = (      # squares ...
   (1,3     ),  # can slide into square 0
   (0,4,2),     # can slide into square 1
   (1,5),       # can slide into square 2
   (0,4,6),     # can slide into square 3
   (1,3,5,7),   # can slide into square 4
   (2,4,8),     # can slide into square 5
   (3,7),       # can slide into square 6
   (4,6,8),     # can slide into square 7
   (5,7))       # can slide into square 8

Goal = "12345678_"   # the board when  puzzle is done #I MODIFIED THIS CODE

def getMoves(board) :
    empty = board.find('_')
    return empty, _slides[empty]

def makeMove(board, empty, mov) :
    lbrd = list(board)
    lbrd[empty],lbrd[mov] = lbrd[mov],lbrd[empty]
    return "".join(lbrd)

manTable = {}

def manhatten(a,b) :
    # a,b are squares 0-8. 3x3. return manhatten dist
	global manTable
	if not manTable :
		print ("Building table for manhatten distance")
		for aa in range(9) :
			for bb in range(9) :
				arow = aa/3; acol=aa%3
				brow = bb/3; bcol=bb%3
				manTable[(aa,bb)] = abs(arow-brow)+abs(acol-bcol)
	ans = manTable.get((a,b))
	if ans == None : print ("args",a,b,a+b,"->",ans)
	return ans

def hamming(a,b) : #i wrote this	
	distance = 0
	if (a != b):
		distance += 1
	return distance
	
manwlcTable = {}
	
def manhattenwlc(a,b) :
    # a,b are squares 0-8. 3x3. return manhatten dist
	global manwlcTable
	if not manwlcTable :
		print ("Building table for manhatten with linear conflicts distance")
		for aa in range(9) :
			for bb in range(9) :
				arow = aa/3; acol=aa%3 #modified
				brow = bb/3; bcol=bb%3  #modified
				manwlcTable[(aa,bb)] = abs(arow-brow)+abs(acol-bcol)
	ans = manwlcTable.get((a,b))
	if ans == None : print ("args",a,b,a+b,"->",ans)
			
	return ans
	#do that of column. Also cater for the situation where both row and column are 0
	#if ans == None : print ("args",a,b,a+b,"->",ans)
	#return ans
	
	
	
def pretty(squares) :
    return "%s %s %s" % (squares[0:3],squares[3:6],squares[6:9])

def printPuzzle(squares,mesg="") :
    print ("-----------", mesg)
    blankIt = re.sub("0",' ',squares)
    print (blankIt[0:3])
    print (blankIt[3:6])
    print (blankIt[6:9])

