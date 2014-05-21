#################Pro Co 2009 Problems#########################



######################2.5#######################
def main_Snupper():
    sent= "we provide great gifts for every occasion"
    print sent.title()

#####################5.2#####################
def main_YaWho():
    original= "stanford proco"
    check="pfd"
    count =0
    
    for i in check:
        if original.find(i) !=-1: #if found
            count=count+1
            if count ==len(check):
                print "yes" 
        else:
            print "no"

#####################2.3######################
def main_AtnTa():
    input= "Go hang a salami I m a lasagna hog"

    input.lower()
    for i in input:
        if i== " ":
            input.replace(i,"")
    if input== input[::-1]:
        print "yes"
    else:
        print "no"
            
        
main_AtnTa()
