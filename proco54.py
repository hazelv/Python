#Grappling With Greeks

def main():
    num= int(raw_input())
    masterList= []
    count=0
    line= []

    for i in range (0,num):
        firstLine= raw_input().split(" ")
        firstLine.remove(firstLine[4])
        secondLine= raw_input().split(" ")
        secondLine.remove(secondLine[4])
        thirdLine= raw_input().split(" ")
        thirdLine.remove(thirdLine[4])

        masterList = firstLine + secondLine + thirdLine


    masterList = sorted(masterList)

    for r in masterList:
        if count<4:
            line.append(r)
            count= count+1
        else:
            print '[%s]' % ', '.join(map(str, line))
            line=[]
            count=1
            line.append(r)
            



main()
