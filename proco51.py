#add numbers w/o carrying the ones

def main():

    a= int(raw_input())
    b= int(raw_input())
    totalSum=''

    for i in range(0,len(str(a))):
        newa= int(a%10)
        newb= int(b%10)
        Sum= str((newa+newb)%10)
        totalSum= Sum+ totalSum
        a=a/10
        b=b/10
        
    print totalSum

if __name__ == '__main__':
    main()
