#sort these arrays & print out median
from itertools import cycle

def main():
    shouldEnter=  int(raw_input())
    masterList=[]
    median=[]

    for i in range(0,shouldEnter):
        list=raw_input().split(" ")
        masterList.append(list)

    for i in masterList:
        numList=[]
        for x in i:
            numList.append(int(x))
        sorted(numList,key=int)
        print numList[1]

    
main()
