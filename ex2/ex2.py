
#  Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37] 

def reversedArray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap the elements at left and right indices
        arr[left], arr[right] = arr[right], arr[left]
        # Move towards middle
        left += 1
        right -= 1
    return arr

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]

def test_element_presence(arr1, arr2):
    # Convert lists to sets for faster lookup
    set_arr2 = set(arr2)
    presence = [element in set_arr2 for element in arr1]
    return presence

# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]
def find_max_min_indices(arr):
    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))
    return max_index, min_index

# Ex4: Read the entire file story.txt and write a program to print out top 100 words occur most
# frequently and their corresponding appearance. You could ignore all
# punction characters such as comma, dot, semicolon, ...
# Sample output:
# house: 453
# dog: 440
# people: 312
# ...

from collections import Counter
def topWordsOcurrMost(): 
    # Open story
    
 
# Main function
if __name__ == "__main__":
    inputArray = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
    result = reversedArray(inputArray)
    print("Reversed Array:", result)

    array1 = [0, 10, 20, 40, 60]
    array2 = [10, 30, 40]
    presence_result = test_element_presence(array1, array2)
    print("Element Presence:", presence_result)


#  Compile: python ex2.py