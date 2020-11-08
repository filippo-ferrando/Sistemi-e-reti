def bubble_sort(list):

	swap = True

	while(swap):
		swap = False

		for i in range(len(list)-1):
			if list[i] > list[i+1]:
				list[i], list[i+1] = list[i+1], list[i]
				swap = True

list = [3, 7, 5, 9, 1, 2, 0, 8]
bubble_sort(list)
print(list)