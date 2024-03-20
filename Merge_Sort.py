def merge_sort(data):
  if len(data) <= 1:
    return data

  # Divide the list into two halves
  mid = len(data) // 2
  left_half = data[:mid]
  right_half = data[mid:]

  # Sort the two halves recursively
  left_sorted = merge_sort(left_half)
  right_sorted = merge_sort(right_half)

  # Merge the sorted halves back together
  return merge(left_sorted, right_sorted)

def merge(left, right):
  merged = []
  i = 0
  j = 0
  # Compare elements from both lists and add the smaller one to merged
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  # Add remaining elements from whichever list has them
  merged += left[i:]
  merged += right[j:]
  return merged

unsorted_data = [5, -2, 7, 3, 9, 6, -5, -3, 10, -4, 4, 0, 2, 1, -1, 8]
print("Unsorted:", unsorted_data)
sorted_data = merge_sort(unsorted_data)
print("Sorted:", sorted_data)