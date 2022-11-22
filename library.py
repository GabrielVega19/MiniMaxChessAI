#utility function for the board state that is passed in returns the value
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
    #because the utility function gets used for opponent we need to flip the sign of the value  
    return count * -1

#takes in input from the user and turns it into a touple
def inputToTouple(inpStr):
    x = numify(inpStr[0])
    y = 8 - int(inpStr[1])

    tup = (int(y), int(x))
    return tup

#takes in letters from the user input and maps it to a value the library can use
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

