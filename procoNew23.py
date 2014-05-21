#Divide a number by a number

def main():
    n= int(raw_input())
    masterList=[]

    for i in range(0,n):
        nums= raw_input().split(" ")
        masterList.append(nums)

    for nums in masterList:
        divid= float(nums[0])/float(nums[1])
        print ("{0:.2f}".format(round(divid,2)))

main()
