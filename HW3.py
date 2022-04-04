# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
def below_the_arithmetical_mean(ary):
  mean = sum(ary) / len(ary)
  ans = []
  for i in ary:
    if i < mean:
      ans.append(i)

  return ans

# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3

def two_lowest_elements(ary):
  ans = []  

  for i in range(0, len(ary)):
    lowest = ary[0]
    index = 0
    for j in range(1, len(ary)):
      #print(f"comparing {lowest} with {ary[j]}")
      if ary[j] <= lowest:
        #print(f"{ary[j]} is smaller")
        lowest = ary[j]
        index = j
        #print(f"new lowest: {lowest}, in index: {index}")
    ans.append(lowest)
    del ary[index]
    # print(f"ans ary: {ans}")
    # print(f"OG ary: {ary}")
    
        

  return ans[:2]

q1 = [1, 3, 5, 6, 4, 10, 2, 3]

print(f"Q1 ans: {below_the_arithmetical_mean(q1)}")

q2 = [198, 3, 4, 9, 10, 9, 2]

print(f"Q2 ans: {two_lowest_elements(q2)}")