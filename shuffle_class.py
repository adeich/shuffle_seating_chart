import numpy as np
import random
from sets import Set

def shuffle_class(number_of_groups, max_people_per_group, roster_filename):
	names_array = np.recfromcsv(roster_filename)
	np.random.shuffle(names_array)

	# groups is a dict to look like {1: [brian, laura], 2: [dan]}
	groups = {i: [] for i in range(1, number_of_groups + 1)}

	# this is a list of integers, each representing one of the groups.
	groups_meta_index_set = Set(groups.keys())
	name_list = list(names_array)

	for name in name_list:
		# first figure out what the smallest current group size is.
		min_current_group_size = min([len(i[1]) for i in groups.items()])

		# then walk through the groups until you meet one of this size.
		keys_list = groups.keys(); random.shuffle(keys_list)
		for group_number in keys_list:
			if len(groups[group_number]) == min_current_group_size:
				groups[group_number].append(name)
				break

	return groups


	

# Print to stdout.
def print_groups(groups):
	for i in sorted(groups.keys()):
		print('Group {}:'.format(i))
		for name in groups[i]:
			print('\t{} {}'.format(name[0], name[1]))


# For making sure we don't leave anyone out!
def check_total_students(groups):
	students = Set()
	for i in groups.keys():
		for name in groups[i]:
			students.add(str(name))
	print('total unique students: {}'.format(len(students)))


if __name__ == '__main__':
	groups = shuffle_class(number_of_groups=6, 
		max_people_per_group=5, 
		roster_filename='physics2ASpring2016.txt')
	check_total_students(groups)
	print_groups(groups)
	
		
		
		
