'''2)Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
1 2 3 4
program:

# Input: Read the size of the list
size = int(input())

# Initialize an empty list
numbers = []

# Input: Read the elements of the list
for _ in range(size):
    number = int(input())
    numbers.append(number)  # Append each number to the list

# Output: Display the list elements separated by spaces
print(" ".join(map(str, numbers)))
'''
