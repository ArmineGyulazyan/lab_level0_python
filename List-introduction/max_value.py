ls = [1,2,2,6,5,7,1,2,3]
tmp = ls[0]
for i in range(len(ls)):
	if ls[i] >= tmp:
		tmp = ls[i]
print(tmp)