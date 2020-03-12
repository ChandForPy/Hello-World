#******************************************************************************************
# py hello.py
#******************************************************************************************
#******************************************************************************************
#print ("Hello World")

#1 Simple Function ******************************************************************************************
#def simpleFunc():
#	print ("Enter an intiger value: ")
#
#Program starts from here
#print ("This program add two intigers")
#simpleFunc()
#val1	= int(input())
#simpleFunc()
#val2	= int(input())
#sum		= val1 + val2
#print ("SUM of two intigers are: ", sum)


lst = [10, 2, 5, 9, 89, 50, 29, 58, 15, 12, 1, 25, 88]
print(lst)
n = len(lst)
m = n//2
for i in range (0, m):
	temp = lst[i]
	lst[i] = lst[n-1]
	lst[n-1] = temp
	n -= 1
print(lst)
	