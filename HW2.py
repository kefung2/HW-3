# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

def split_in_half(line):
    ans = ""
    p1 = ""
    p2 = ""
    mid = int(len(line)/2)
    if len(line)%2 == 1: #odd
        p1 = line[0:mid+1]
        p2 = line[mid:len(line)+1]
    else:
        p1 = line[0:mid]
        p2 = line[mid:len(line)+1]

    ans = p2 + p1
    
    return ans

# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
# Hint: https://www.w3schools.com/python/python_sets.asp

def unique_chara_in_string(line):
    strset = set()
    for i in line:
        if i in strset:
            return False
        else:
            strset.add(i)
    return True



question1 = input("Enter a string for Split In Half: ")

print(f"Split in Half Result: {split_in_half(question1)}")


question2 = input("Enter a string for Unique Characters in String: ")

print(f"Unique Characters in String Result: {unique_chara_in_string(question2)}")