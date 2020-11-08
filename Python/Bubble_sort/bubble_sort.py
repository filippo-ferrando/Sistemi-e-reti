def bubble_sort(list):

	for i in range(len(list)):

		for j in range(len(list)-1):

			if list[j] > list[j+1]:

				list[j], list[j+1] = list[j+1],list[j]	


list = [3, 6, 4, 9, 12, 35, 2, 1]
bubble_sort(list)
print(list)