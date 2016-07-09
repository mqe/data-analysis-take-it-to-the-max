def NextStepA(steps):
	if all(s == "-" for s in steps):
		return "-"
	else:
		return min(steps) + 1

def NextStepB(steps):
	return min(steps) + 1

def NextStepC(steps):
	if all(s == "-" for s in steps):
		return "-"
	elif all (str(s).isdigit() for s in steps):
		return min(steps) + 1

print NextStepA(["-","-","-"])
print NextStepA([5,"-",2])
print NextStepA(["-"])
print NextStepA([1])
print NextStepA([3,2,4])