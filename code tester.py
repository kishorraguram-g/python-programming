"""def factorial(n):
    n=int(n)
    print(n)
    count=1
    while(n):
        print(n)
        count*=n
        n-=1
    return count;

j=int(input())
j=factorial(j)
print(j)
"""

"""
#function to check if the character is vowel or not
def isVowel(x):
    if(x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'):
        return True
    else:
        return False
#function returns the updated string
def updateSandwichedVowels(a):
    n = len(a)
#string to store updated string 
    updatedString = " "
#traverse the str
    for i in range(0,n,1):
        if(i == 0 or i == n-1):
            updatedString += a[i]
            continue
        if(isVowel(a[i]) == True and isVowel(a[i-1]) == False and isVowel(a[i+1]) ==False):
                   continue
        updatedString += a[i]
    return updatedString
if __name__=='__main__':
    str="poodapaithyam"
    updatedString=updateSandwichedVowels(str)
    print(updatedString)
"""

"""

def elements_with_alphabet(input_list, alphabet):
    result = []
    for element in input_list:
        if alphabet in element[0]:
            result.append(element)
    return result


input_list = ["apple", "banana", "orange", "grape", "kiwi","anna"]
alphabet = input("Enter alphabet to search for: ")
result_list = elements_with_alphabet(input_list, alphabet)
print("Elements containing the alphabet:", result_list)
"""

"""
# Get ASCII value of a character
char = 'fjkd"  # Change this to the character you want to find the ASCII value of
ascii_value = ord(char)
print("The ASCII value of '{}' is: {}".format(char, ascii_value))
"""
"""
x = 5
y = 10
x, y = y, x
print(x)
print(y)"""


import array

test_list = [6, 4, 8, 9, 10]

# Printing list
print("The original list: " + str(test_list))

# Convert list to Python array
# Using array() + data type indicator
res = array.array("i", test_list)

# Printing result
# Convert array to list and then print
print("List after conversion to array:", list(res))
