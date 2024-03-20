def quicksort(data):
  # Base case: If the list has 0 or 1 element, it's already sorted
  if len(data) <= 1:
    return data

  # Choose a pivot element (here, the last element)
  pivot = data[-1]

  # Partition the list around the pivot
  left, right = partition(data, pivot)

  # Sort the left and right sub-arrays recursively
  left_sorted = quicksort(left)
  right_sorted = quicksort(right)

  # Combine the sorted sub-arrays with the pivot in the middle
  return left_sorted + [pivot] + right_sorted

def partition(data, pivot):
  left = []
  right = []
  for element in data[:-1]:  # exclude the pivot itself
    if element < pivot:
      left.append(element)
    else:
      right.append(element)
  return left, right

unsorted_data = [5, -2, 7, 3, 9, 6, -5, -3, 10, -4, 4, 0, 2, 1, -1, 8]
print("Unsorted:", unsorted_data)
sorted_data = quicksort(unsorted_data)
print("Sorted:", sorted_data)