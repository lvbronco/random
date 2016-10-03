def longestSub(a, n):
    p = [0]*n
    m = [0]*(n+1)
    l = 0
    for i in range(n):
        lo = 1
        hi = l
        while lo <= hi:
            mid = lo + ((hi - lo)/2)
            if a[m[mid]] < a[i]:
                lo = mid + 1
            else:
                hi = mid - 1
        p[i] = m[lo-1]
        m[lo] = i
        if lo > l:
            l = lo
        print "x-> {}, i -> {}, l -> {}, lo -> {}, hi -> {}, p -> {}, m -> {}".format(a[i], i, l, lo, hi, p, m[1:])
    
    S = [None]*l
    k = m[l]
    for i in range(l-1, -1, -1):
        print "k = {}, a[k] = {}, p[k] = {}".format(k, a[k], p[k])
        S[i] = a[k]
        k = p[k]
    print S
    return l
            
# n = int(raw_input())
# a = []
# for i in range(n):
#     a.append(int(raw_input()))
n = 9
a = [2, 6, 3, 4, 1, 2, 9, 5, 10]

print a
print longestSub(a, n)

#  1st, 3rd, 4th, 8th, 9th
# {2, 3, 4, 5, 8}