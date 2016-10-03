import sys
t = int(raw_input())
for counter in range(0,t):
    two = 0
    five = 0
    n = int(raw_input())
    #case of 2
    while( n%2 == 0):
        n = n/2
        two = two + 1
    #case of 5
    while( n%5 == 0):
        n = n/5
        five = five +1
    temp = max(two-2,five)
    temp2 = 1
    count = 1
    while temp2 % n != 0:
        temp2= (temp2*10+1) %n
        count = count + 1
    print count*2+temp