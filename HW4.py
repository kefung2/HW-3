# Even First
# Your input is an array of integers, and you have to reorder its entries so that the even entries appear first. 
# You are required to solve it without allocating additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

def even_first(ary):
  index = 0
  for i in range(0,len(ary)):
    print(f"current index: {index}, in loop {i}, num = {ary[i]}")
    if ary[i] %2 == 0:
      ary[index], ary[i] = ary[i], ary[index]
      print(ary)
      index += 1

  return ary


# Increment a Number
# Write a program that takes as input an array of digits encoding a nonnegative decimal integer D and updates the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def increment_a_num(ary):
  nines_check = 0
  for i in range(0, len(ary)):
    if ary[i] == 9:
      nines_check +=1

  if nines_check == len(ary):
    ary[0] = 1
    for i in range(1, len(ary)):
      ary[i] = 0
    ary.append(0)
    return ary

  ary[-1] += 1
  for i in reversed(range(0, len(ary))):
    if ary[i] == 10:
      ary[i] = 0
      ary[i-1] += 1
  
  return ary


q1 = [7, 3, 5, 6, 4, 10, 3, 2]

print(f"Q1 ans: {even_first(q1)}")

q2 = [9,9,9]

print(f"Q2 ans: {increment_a_num(q2)}")