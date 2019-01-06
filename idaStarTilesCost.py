from tiles3x3 import manhattenwlc, Goal #modified

def manhattanwlccost(board, target) : #modified
    # estimate future cost by sum of tile displacements
    future = 0
    for sq in range(9):
        occupant = board[sq]
        if occupant != '_' :
			shouldbe = target.find(occupant)
			future += manhattenwlc(sq,shouldbe)
			#arow, brow, acol, bcol, ans= manhattenwlc(sq, shouldbe)
			#future += ans
			#if arow == brow :
			if abs(sq-shouldbe) == 1 or abs(sq-shouldbe) == 2 : #current and goal position on the same row
				targetRow = sq/3
				for tiles in range(targetRow*3, (targetRow*3)+3):
					neighbor = board[tiles]
					if neighbor != occupant and neighbor != '_':
						neighborshouldbe = target.find(neighbor)
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
						neighborshouldbe = target.find(neighbor)
						#sameRow, sameCol, arow, acol, ans = manhattenwlc1(int(neighbor), neighborshouldbe)
						#if sameCol == 0 and acol == targetCol and ans!=0 :
						if (abs(tiles-neighborshouldbe) == 3 or  abs(tiles-neighborshouldbe) == 6) and neighborshouldbe%3==targetCol :
							if (sq-shouldbe > 0 and tiles-neighborshouldbe < 0) or (sq-shouldbe < 0 and tiles-neighborshouldbe > 0):
								future+=2
			

    #past = depth     # Simply the moves so far for this path

    return future   # best heuristic