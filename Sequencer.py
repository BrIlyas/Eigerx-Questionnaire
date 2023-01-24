import sys

def Sequencer(myStream ,maxElement, maxCount):
    newElement = int(myStream.readline())
    if newElement == 0:
        return (maxElement, maxCount)
    elif newElement > maxElement:
        return Sequencer(myStream ,newElement, 1)
    elif newElement == maxElement:
        return Sequencer(myStream ,maxElement, maxCount+1)
    elif newElement < maxElement:
        return Sequencer(myStream ,maxElement, maxCount)


myFile = open("inStream.txt", "rt")
print (Sequencer(myFile, -sys.maxsize - 1, 0))
