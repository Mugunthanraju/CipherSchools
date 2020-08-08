# Program to determine whether a sequence of brackets is Balanced or Not

openList = ["[","{","("]  # Opening Brackets
closeList = ["]","}",")"] # Closing Brackets

# The Function is to decide whether the sequence of  brackets is Balanced or Not
def balanced(sequence):
    stack= []

    for i in sequence:

        if i in openList:
            stack.append(i)
        
        elif i in closeList:
            pos = closeList.index(i)
            
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "NO"
    
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

 
# How much string(s) is/are need to be tested? 
number = int(input())

list_string = []

# Getting those strings from user which are to be tested
for i in range(number):
    string = input()
    list_string.append(string)

# Result Output
for string in list_string:
    print(balanced(string))
