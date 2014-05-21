#program takes binary nums & turns into reg nums

def main():
    placeHolder=0
    sum=0

    binary= raw_input("Please enter number: ")

    for x in reversed(binary):
        sum= sum + (int(x)*2**placeHolder)
        placeHolder= placeHolder +1
       
    print "The num is:" + str(sum)

if __name__ == '__main__':
    main()
