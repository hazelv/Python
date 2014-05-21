
def main():
    n= int(raw_input())
    overlap=[]
    words=[]

    for i in range(0,n):
        a= str(raw_input())
        b= str(raw_input())
        for i in range (0,a):
            if not b[i] in a:
                this= 
                a.replace(b," 333 ")
                b=""
            overlap.append(a + b)
        
    for v in overlap:
        print v
main()
