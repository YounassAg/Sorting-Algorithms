def insertion_sort(data):
  for i in range(1, len(data)):
    # Select the first element from the unsorted part
    key = data[i]

    # Move elements of sorted part that are greater than key
    # to one position ahead of their current position
    j = i - 1
    while j >= 0 and data[j] > key:
      data[j + 1] = data[j]
      j -= 1
    # Insert the key at its correct position in sorted part
    data[j + 1] = key
  return data

unsorted_data = [5, -2, 7, 3, 9, 6, -5, -3, 10, -4, 4, 0, 2, 1, -1, 8]
print("Unsorted:", unsorted_data)
sorted_data = insertion_sort(unsorted_data)
print("Sorted:", sorted_data)