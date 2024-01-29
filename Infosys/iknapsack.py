# Python3 implementation to print all https://www.geeksforgeeks.org/0-1-knapsack-problem-to-print-all-possible-solutions/?ref=gcse
# the possible solutions of the 
# 0/1 Knapsack problem


INT_MIN=-2147483648
def nextPermutation(nums: list) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		if sorted(nums,reverse=True)==nums:
			return None
		n=len(nums)
		brk_point=-1
		for pos in range(n-1,0,-1):
			if nums[pos]>nums[pos-1]:
				brk_point=pos
				break
		else:
			nums.sort()
			return
		replace_with=-1
		for j in range(brk_point,n):
			if nums[j]>nums[brk_point-1]:
				replace_with=j
			else:
				break
		nums[replace_with],nums[brk_point-1]=nums[brk_point-1],nums[replace_with]
		nums[brk_point:]=sorted(nums[brk_point:])
		return nums

# Function to find the all the
# possible solutions of the
# 0/1 knapSack problem
def knapSack(W, wt, val, n):
	# Mapping weights with Profits
	umap=dict()
	
	set_sol=set()
	# Making Pairs and inserting
	# o the map
	for i in range(n) :
		umap[wt[i]]=val[i]
	

	result = INT_MIN
	remaining_weight=0
	sum = 0
	
	# Loop to iterate over all the
	# possible permutations of array
	while True:
		sum = 0
		
		# Initially bag will be empty
		remaining_weight = W
		possible=[]
		
		# Loop to fill up the bag
		# until there is no weight
		# such which is less than
		# remaining weight of the
		# 0-1 knapSack
		for i in range(n) :
			if (wt[i] <= remaining_weight) :

				remaining_weight -= wt[i]
				sum += (umap[wt[i]])
				possible.append((wt[i],
					umap[wt[i]])
				)
			
		
		possible.sort()
		if (sum > result) :
			result = sum
		
		if (tuple(possible) not in set_sol):
			for sol in possible:
				print(sol[0], ": ", sol[1], ", ",end='')
			
			print()
			set_sol.add(tuple(possible))
		
		
		if not nextPermutation(wt):
			break
	return result


# Driver Code
if __name__ == '__main__':
	val=[60, 100, 120]
	wt=[10, 20, 30]
	W = 50
	n = len(val)
	maximum = knapSack(W, wt, val, n)
	print("Maximum Profit =",maximum)

#This code was contributed by Amartya Ghosh
