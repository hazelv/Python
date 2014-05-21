#is this a magic square?

def findingSum(masterList):
    for x in masterList:
        #you have individual lines
        currentSum= currentSum + x[placeHolder]
        placeHolder++
    return currentSum

def main():
    holder= int(raw_input())
    masterList=[]

    placeHolder=0

    for i in range(0,holder):
        line= raw_input().split(" ")
        masterList.append(int(line))
        lineSum=findingSum(masterList)
        if !(lineSum==holder*holder):
            print no
            break
#write main method
