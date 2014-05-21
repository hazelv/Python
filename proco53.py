#check whether a number is happy or not

def numSum(n):
    first= n%10
    second= n/10

def main():
    input= int(raw_input())
    sum= numSum(input)

    while True:
        if sum>10:
            numSum(sum)
        else:
            if sum==1:
                print "happy"
                break
            if sum >1:
                print "sad"
