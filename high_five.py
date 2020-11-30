from collections import defaultdict 

def highFive(items):
	count = dict()
	
	for item in items:
		if item[0] in count:
			count[item[0]].append(item[1])
		else:
			count[item[0]] = [item[1]]



items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
highFive(items)

