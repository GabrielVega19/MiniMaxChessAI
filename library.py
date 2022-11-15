#utility function for the board s
def utilityFunction(boardState):
    bs = boardState["board"]
    count = 0
    
    for row in bs:
        for piece in row:
            if piece == 2:
                count += 9
            elif piece == -2:
                count -= 9
            elif piece == 3:
                count += 5
            elif piece == -3:
                count -= 5
            elif piece == 4:
                count += 3
            elif piece == -4:
                count -= 3
            elif piece == 5:
                count += 3
            elif piece == -5:
                count -= 3
            elif piece == 6:
                count += 1
            elif piece == -6:
                count -= 1
            
    return count