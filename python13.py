import random

def cut(list,here):
	

	list2 = [i for i in list if i < here]
	return list2



def maxDistance(list,limit):
	# Sorting input list
	lim=limit
	list.sort(reverse=True)
	print("THIS IS THE LIST: ",list)
	res=0
	temp=0

	print("THIS IS LIST'S LENGTH: ",len(list))

	print("THIS IS THE LIMIT NUMBER: ",limit)
	x="not empty"
	y="move on"
	while limit>0:
		if x=="empty":
			break
		if  y=="stop":
			break
		i=0
		end=len(list) - 1
		while i <=end:
			#print(list[i],i)
			if limit>=list[i]:
				res += list[i]
				limit-=list[i]
				print("FOUND A NUMBER...REMAINING LIMIT: ",limit)
				list2=cut(list,list[i])
				print("NEW LIST: ",list2)
			else:
				i+=1
				continue
			if len(list2)==0:
				x="empty"
				break
			if limit<list2[len(list2)-1]:
				y="stop"
				break

			i+=1
		list=list2

	print("FINAL NUMBER: ",	res)
	print("LIMIT WAS: ",lim)
# Creating a random list of 50 elements with max the 100
myList = random.sample(range(100),50)
# Call the function
maxDistance(myList,random.randint(0,300))
