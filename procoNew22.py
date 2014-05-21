#directions

def main():
    directions=["N","NE","E","SE","S","SW","W","NW"]
    n=int(raw_input())

    masterList=[]

    for i in range(0,n):
        dirs= raw_input().split(" ")
        masterList.append(dirs)

    for item in masterList:
        for single in item:
            if single in directions:
                print "check*"

main()
