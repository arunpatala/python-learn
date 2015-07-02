
def quickSort(arr):
	if(len(arr)<=1):
		return arr
	pivot = arr[len(arr)/2]
	left = [x for x in arr if x<pivot]
	right = [x for x in arr if x>pivot]
	middle = [x for x in arr if x==pivot]
	return quickSort(left) + middle + quickSort(right)

print quickSort([5,2,7,6,3,1,8,4,9,0])
