from unittest import result


def raiseToPower(baseNum, powNum):
    result = 1
    for endex in range(powNum):#every time that the variable enter in the loop multpliply 
        result = result * baseNum
    return result

print(raiseToPower(9, 4))