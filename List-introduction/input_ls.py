num = int(input("Enter an integer: "))
ls = []
for i in range(num):
	inp_int = int(input())
	if isinstance(inp_int,int):
		ls.append(inp_int)
print(ls)