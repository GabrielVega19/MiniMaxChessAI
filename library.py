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
            
    return count * -1

def inputToTouple(inpStr):
    x = numify(inpStr[0])
    y = 8 - int(inpStr[1])

    tup = (int(y), int(x))
    return tup

def numify(letter):
    if letter == "a":
        return 0
    elif letter == "b":
        return 1
    elif letter == "c":
        return 2
    elif letter == "d":
        return 3
    elif letter == "e":
        return 4
    elif letter == "f":
        return 5
    elif letter == "g":
        return 6
    elif letter == "h":
        return 7

