"""
Write a Python profram to store second year percentage of students in array. Write function for sorting array of floating point numbers in ascending order using quick sort and display top five scores.
"""

# Function to take student percentage:------------------------------------------------

def createArray(n):
    array = []
    for i in range(n):
        percentage = float(input(f"Enter percentage of student {i+1}: "))
        array.append(percentage)
    return array

# Bubble Sort:------------------------------------------------------------

def bubbleSort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(n-1):
            if array[j]>array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array

# Main program start from here -----------------------------------------------------

n = int(input("Enter total number of students value: "))
array = createArray(n)
mini = len(array)-6
maxi = len(array)-1
index = 1
array = bubbleSort(array)
print("---------------------Top scorer using bubble sort-------------------------\n")
for i in range(maxi, mini, -1):
    if i>=0:
        print(f"Topper No. {index}", array[i],"\n")
    else:
        break
    index+=1   
