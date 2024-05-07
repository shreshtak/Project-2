# Example file: next_fit.py

# explanations for member functions are provided in requirements.py

def next_fit(items: list[float], assignment: list[int], free_space: list[float]):
	# items: list of items to put in bins, items[i] < 1.0
	# assignment: assignment[i] = item i  -->  assignment[i] 
	# free space: amount of free space in each bin. freespace[i] = assignment[i] --> these are the bins

	# j = counter for bins
	# i = counter for items
	# while j < len(assignment):
	# 		if items[i] < freespace[j]:
	# 			assignment[j] += item[i]
	#			freespace[j] -= item[i]
	#			i += 1
	#		else:
	#			j += 1	--> move onto the next bin and repeat

	#		check if new bin needs to be created
	#		if j >= len(assignment):
	#			assignment.append(0)

	j = 0	# counter for bins
	i = 0	# counter for items

	while j < len(assignment) and i < len(items):

		if j >= len(free_space):					# if bin j not in free_space list, add it
			free_space.append(1.0)		
		
		if items[i] <= free_space[j]:				# if item i fits in bin i, add it to the bin and subtract from free space
			assignment[i] = j						# assign item i to bin j
			free_space[j] -= items[i]
			i += 1									# move to the next item
		else:
			j += 1									# move to the next bin

		if j >= len(assignment):					# add new bin if there are no bins left
			assignment.append(0)		
	
	return
