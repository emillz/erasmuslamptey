## Template
#!/usr/bin/env python3

# Name: Erasmus Lamptey-Mills
# Index number: PS/ITC/14/0025

# TODO: Put your codes here ...


total = 0

for numbers in range(2000):
    if(numbers % 3 == 0) or (numbers % 5 == 0):
        total += numbers

print (total)
