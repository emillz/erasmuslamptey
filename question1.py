## Template
#!/usr/bin/env python3

# Name: Erasmus Lamptey-Mills
# Index number: PS/ITC/14/0025

# TODO: Put your codes here ...

line = ""

for number in range(1000, 7001):
    if(number % 7 == 0) and (number % 5 != 0):
        line += str(number) + ", " 

print (line)
