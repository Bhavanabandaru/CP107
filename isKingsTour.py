# Background:  in Chess, a King can move from any square to
# any adjacent square.  A King’s Tour is a series of legal King
# moves so that every square is visited exactly once. 
# We can represent a Kings Tour in a 2d list where the 
# numbers represent the order the squares are visited, going 
# from 1 to N2.  For example, consider these 2d lists:

#    [ [  3, 2, 1 ],    	[ [  1, 2, 3 ],  	[ [ 3, 2, 1 ],
#  	[  6, 4, 9 ],      	[  7, 4, 8 ],    	[ 6, 4, 0 ],
#  	[  5, 7, 8 ] ]     	[  6, 5, 9 ] ]   	[ 5, 7, 8 ] ]

# The first is a legal Kings Tour but the second is not, 
# because there is no way to legally move from the 7 to the 8, 
# and the third is not, because it contains a 0 which is out
#  of range.  With this in mind, write the function 
# isKingsTour(board) that takes a 2d list of integers, 
# which you may assume is NxN for some N>0, and 
# returns True if it represents a legal Kings Tour 
# and False otherwise.

def legal(board,row,col):
    rows = len(board)
    cols = len(board[0])
    k = board[row][col]
    if col+1<cols:
        c=col+1
        if board[row][c]==k+1:
            return True
    if col-1>=0:
        c=col-1
        if board[row][c]==k+1:
            return True
    if row-1>=0:
        r=row-1
        if board[r][col]==k+1:
            return True
        if col-1>=0:
            c=col-1
            if board[r][c]==k+1:
                return True
        if col+1<cols:
            c=col+1
            if board[r][c]==k+1:
                return True
    if row+1<rows:
        r = row+1
        if board[r][col]==k+1:
            return True
        if col-1>=0:
            c = col-1
            if board[r][c]==k+1:
                return True
        if col+1<cols:
            c = col+1
            if board[r][c]==k+1:
                return True
    return False

def isKingsTour(board):
    # Your code goes here...
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] != (len(board)*(len(board[0]))):
                if not legal(board,x,y):
                    return False
    
    return True


