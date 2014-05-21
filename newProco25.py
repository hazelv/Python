#finding the volume of a sphere

def main():
    enter= int(raw_input())
    pi= float(22.0/7)
    master= []

    for i in range (0,enter):
        i=int(raw_input())
        volume= (4.0/3) * ((pi) * (i**3))
        master.append(volume)
        
    for i in range (0, len(master)):
        print int(master[i])

main()
        
