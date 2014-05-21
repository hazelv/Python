#The pivot problem

def main():
    completeList=[]
    listBefore=[]
    listAfter=[]
    listIs=[]
    len1= int(raw_input())
    input1= raw_input().split(" ")
    pivot=input1[0]
        
    for i in range (1,len1):
        if input1[i]< pivot:
            listBefore.append(input1[i])
    for i in range (1,len1):
        if input1[i]== pivot:
            listIs.append(input1[i])
    for i in range (1,len1):
        if input1[i]> pivot:
            listAfter.append(input1[i])
    completeList.append(int(listBefore))
    completeList.append(int(input1[0]))
    completeList.append(int(listIs))
    completeList.append(int(listAfter))
    print str(completeList)

if __name__ == '__main__':
    main()
