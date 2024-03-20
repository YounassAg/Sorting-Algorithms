def bubble_sort(data):
  # Loop through the list n-1 times
  for i in range(len(data) - 1):
    swapped = False
    # Compare adjacent elements
    for j in range(len(data) - i - 1):
      if data[j] > data[j + 1]:
        # Swap elements if they are in the wrong order
        data[j], data[j + 1] = data[j + 1], data[j]
        swapped = True
    # If no swaps occurred, the list is already sorted
    if not swapped:
      break
  return data

unsorted_data = [5, -2, 7, 3, 9, 6, -5, -3, 10, -4, 4, 0, 2, 1, -1, 8]
print(f"Unsorted: {unsorted_data}")
sorted_data = bubble_sort(unsorted_data)
print(f"Sorted: {sorted_data}")