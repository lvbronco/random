from __future__ import print_function
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = str(raw_input())

def sort_f(x, y):
    #print("{}: {} and {}: {}".format(x, x.isdigit(), y, y.isdigit()))
    if x.isdigit() and y.isdigit():
        if int(x) % 2 == 1 and int(y) % 2 == 0: 
            return -1
        elif int(y) % 2 == 1 and int(x) % 2 == 0:
            return 1
    elif x.isalpha() and y.isdigit():
        return -1
    elif y.isalpha() and x.isdigit():
        return 1
    elif x.islower() and not y.islower():
        return -1
    elif y.islower() and not x.islower():
        return 1
    
    return ord(x)-ord(y)

L = sorted(s, cmp=sort_f)
print (*L, sep='')
