## Template
#!/usr/bin/env python3

# Name: Erasmus Lamptey-Mills
# Index number: PS/ITC/14/0025

# TODO: Put your codes here ...





def fibbonachi():
    sumTotal = 0
    term1 = 1
    term2 = 2
    count = 1


    while True:

        tempTerm = term1 + term2
        term1 = term2
        term2 = tempTerm
        count += 1

        
        if (term1 % 2 == 0):
            sumTotal += term1

        

        if term2 > 4000000:
            break
        
    return sumTotal



print (fibbonachi())
        

