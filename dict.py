keys = ['k1', 'k2', 'k3', 'k4']
values = ['v1', 'v2', 'v3', 'v4']
mydict = {}

for i in range(0, len(keys)):
	mydict[keys[i]] = values[i]

print mydict.items()

