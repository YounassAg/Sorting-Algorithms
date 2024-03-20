def selection_sort(data):
  """Sorts a list of data in ascending order using selection sort.

  Args:
    data: A list of sortable elements.

  Returns:
    The sorted list.
  """
  for i in range(len(data)):
    # Set the current element as the minimum (index-wise)
    min_index = i
    for j in range(i + 1, len(data)):
      # Find the actual minimum element within the unsorted part
      if data[j] < data[min_index]:
        min_index = j
    # Swap the found minimum element with the first element of unsorted part
    if i != min_index:
      data[i], data[min_index] = data[min_index], data[i]
  return data

# Example usage
unsorted_data = [5, -2, 7, 3, 9, 6, -5, -3, 10, -4, 4, 0, 2, 1, -1, 8]
print("Unsorted:", unsorted_data)
sorted_data = selection_sort(unsorted_data)
print("Sorted:", sorted_data)
