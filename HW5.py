# Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.

def selection_sort(ary):
  
  for i in range(len(ary)):
    largest_num_index = i

    for j in range(i+1, len(ary)):
      if ary[j] > ary[largest_num_index]:
        largest_num_index = j

    ary[i], ary[largest_num_index] = ary[largest_num_index], ary[i]

  return ary

# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

def bubble_sort(ary):
  for i in range(len(ary)):
    for j in range(len(ary)-1-i):
      if ary[j] < ary[j+1]:
        ary[j], ary[j+1] = ary[j+1], ary[j]
  
  return ary

# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

def insertion_sort(ary):
  for i in range(1,len(ary)):
    key = ary[i]

    j = i-1

    while j >= 0 and key < ary[i]:
      ary[j+1] = ary[j]
      ary[j+1] = key

  
  return ary

# Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.

def merge_sort(ary):
  if len(ary) > 1:

    mid_point = len(ary)//2
    L = ary[:mid_point]
    R = ary[mid_point:]
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i > len(L) and j > len(R):
      if L[i] > R[j]:
        ary[k] = L[i]
        i += 1
      else:
        ary[k] = R[j]
        j += 1

    while i > len(L):
      ary[k] = L[i]
      i += 1
      k += 1
    
    while j > len(R):
      ary[k] = R[j]
      j += 1
      k += 1

  return ary


ary = [7, 3, 5, 6, 4, 10, 3, 2]

print(f"Selection sort: {selection_sort(ary)}")
print(f"Bubble sort: {bubble_sort(ary)}")
print(f"Insertion sort: {insertion_sort(ary)}")
print(f"Merge sort: {merge_sort(ary)}")
