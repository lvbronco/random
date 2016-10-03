# data = [('Jervie',12,'M'),('Jaimy',11,'M'),('Tony',23,'M'),('Jaimy',11,'F')]
# # and so define a lambda that returns a tuple that describes priority, for instance

# print sorted(data, key=lambda tup: (tup[1],tup[0]) )
# # print sorted(data, key=lambda tup: tup[1] )
# # print sorted(data)
# # [(1, 1, 4), (1, 2, 1), (1, 2, 3)]

# def f(n):
# 	if n <= 0:
# 		return 0
# 	return n+f(int(n/2))

# print f(4)

x = []
x.append([1,2,3])
x.append([4,5,6])
x.append([7,8,9])

print (x[0][2] + x[2][1])