
def main():
    sum=0
    for i in range(1,1000):
        if i%3 == 0:
            sum=sum + i
        else:
            if i%5 == 0:
                sum=sum + i
        
    print "Answer is: " + str(sum)
    

if __name__ == '__main__':
    main()
