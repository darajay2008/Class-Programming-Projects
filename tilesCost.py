#  tilesCost.py
#
#  Compute and return the cost of a board along with its
#  depth (moves so far) and its node number (order of creation)

from tiles3x3 import manhatten, hamming, manhattenwlc, Goal #modified

def manhattancost(board,depth,number) : #modified
    # estimate future cost by sum of tile displacements
    future = 0
    for sq in range(9):
        occupant = board[sq]
        if occupant != '_' :
			shouldbe = Goal.find(occupant)
			future += manhatten(sq,shouldbe)
			

    past = depth     # Simply the moves so far for this path

    return past + future*3   # best heuristic

    return -number   # This will force raw depth first queueing
    return  number   # This will force raw breadth first queueing

    # past cost and future cost. Find correct ratio for best results
    return past + future*0   # mostly depth first - no future
    return past + future*1   # Various ratios of past/future
    return past + future*2   #
    return past + future*3   #
    return past + future*4   #
	
def hammingcost(board,depth,number) : #modified
    # estimate future cost by sum of tile displacements
    future = 0
    for sq in range(9):
        occupant = board[sq]
        if occupant != '_' :
			shouldbe = Goal.find(occupant)
			future += hamming(sq,shouldbe) #modified

    past = depth     # Simply the moves so far for this path

    return past + future*3   # best heuristic

    return -number   # This will force raw depth first queueing
    return  number   # This will force raw breadth first queueing

    # past cost and future cost. Find correct ratio for best results
    return past + future*0   # mostly depth first - no future
    return past + future*1   # Various ratios of past/future
    return past + future*2   #
    return past + future*3   #
    return past + future*4   #

def manhattanwlccost(board,depth,number) : #modified
    # estimate future cost by sum of tile displacements
    future = 0
    for sq in range(9):
        occupant = board[sq]
        if occupant != '_' :
			shouldbe = Goal.find(occupant)
			future += manhattenwlc(sq,shouldbe)
			#arow, brow, acol, bcol, ans= manhattenwlc(sq, shouldbe)
			#future += ans
			#if arow == brow :
			if abs(sq-shouldbe) == 1 or abs(sq-shouldbe) == 2 : #current and goal position on the same row
				targetRow = sq/3
				for tiles in range(targetRow*3, (targetRow*3)+3):
					neighbor = board[tiles]
					if neighbor != occupant and neighbor != '_':
						neighborshouldbe = Goal.find(neighbor)
						#sameRow, sameCol, arow, acol, ans = manhattenwlc1(int(neighbor), neighborshouldbe)
						#if sameRow == 0 and arow == targetRow and ans!=0 :
						if (abs(tiles-neighborshouldbe) == 1 or abs (tiles-neighborshouldbe) == 2) and neighborshouldbe/3==targetRow :
							if (sq-shouldbe > 0 and tiles-neighborshouldbe < 0) or (sq-shouldbe < 0 and tiles-neighborshouldbe > 0):
								future+=2
			if abs(sq-shouldbe) == 3 or abs(sq-shouldbe) == 6: #current and goal position on the same column
				targetCol = sq%3
				for tiles in range(targetCol, targetCol+7, 3):
					neighbor = board[tiles]
					if neighbor != occupant and neighbor != '_':
						neighborshouldbe = Goal.find(neighbor)
						#sameRow, sameCol, arow, acol, ans = manhattenwlc1(int(neighbor), neighborshouldbe)
						#if sameCol == 0 and acol == targetCol and ans!=0 :
						if (abs(tiles-neighborshouldbe) == 3 or  abs(tiles-neighborshouldbe) == 6) and neighborshouldbe%3==targetCol :
							if (sq-shouldbe > 0 and tiles-neighborshouldbe < 0) or (sq-shouldbe < 0 and tiles-neighborshouldbe > 0):
								future+=2
			

    past = depth     # Simply the moves so far for this path

    return past + future*4   # best heuristic

    return -number   # This will force raw depth first queueing
    return  number   # This will force raw breadth first queueing

    # past cost and future cost. Find correct ratio for best results
    return past + future*0   # mostly depth first - no future
    return past + future*1   # Various ratios of past/future
    return past + future*2   #
    return past + future*3   #
    return past + future*4   #
