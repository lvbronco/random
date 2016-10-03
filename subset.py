def isSubsetSum(a, s):
	n = len(a)
	m = [[0 for x in range(n+1)] for y in range(s+1)]

	for i in range(n+1):
		m[0][i] = True

	for i in range(1, s+1):
		m[i][0] = False

	for i in range(1, s+1):
		for j in range(1, n+1):
			m[i][j] = m[i][j-1]
			if i >= a[j-1]:
				m[i][j] = m[i][j] or m[i - a[j-1]][j-1]

	# print "#  ",
	# print "-  ",
	# for x in a:
	# 	if x < 10:
	# 		print '{}  '.format(x),
	# 	else:
	# 		print '{} '.format(x),
	# print ''

	# print "S/N",
	# for j in range(0, n+1):
	# 	if j < 10:
	# 		print '{}  '.format(j),
	# 	else:
	# 		print '{} '.format(j),

	# print ''
	# for i in range(0, s+1):
	# 	if i < 10:
	# 		print '{}  '.format(i),
	# 	else:
	# 		print '{} '.format(i),
	# 	for j in range(0, n+1):
	# 		print '{}  '.format(boolChar(m[i][j])),
	# 	print ''

	return m[s][n]

def sumSubsetSum(a, s):
    n = len(a)
    m = [[0 for x in range(n+1)] for y in range(s+1)]
    
    for j in range(n+1):
        m[0][j] = 1
    
    for i in range(1, s+1):
        m[i][0] = -1
    
    for i in range(1, s+1):
        for j in range(1, n+1):
            m[i][j] = m[i][j-1]
            t = int(a[j-1])
            if i >= t:
                if m[i][j] < 0:
                    m[i][j] = 1
                else:
                    m[i][j] = m[i - t][j-1] + 1
    
    return m[s][n]


def boolChar(b):
	if b:
		return 'T'
	return 'F'

a = [2,3,6,7,5,5]
s = 15
# a = []
# s = 0
print sumSubsetSum(a, s)