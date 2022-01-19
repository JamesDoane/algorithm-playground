# There are 5 major sorting algorithms: Bubble, Insertion, Merge, Quicksort, and Timsort

# Quicksort, true to it's name is generally the fastest, but Timsort is also rather quick and can beat quicksort for small inputs.
# Merge is also pretty quick (O(logn)) like quicksort, but in practice it is outperformed by Quicksort and Timsort


# Bubble Sort:
# values bubble their way to the top by doing a comparison of each value with it's adjacent values. Not very efficient. O(n**2) unsorted,
#  O(n) if already sorted.


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

# Insertion Sort
# also generally pretty slow due to potentially having O(n**2)

# Loop from the second element of the array until
    # the last element
 # This is the element we want to position in its
        # correct place
# Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`

# Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
# Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
# When you finish shifting the elements, you can position
        # `key_item` in its correct location            

def insertion_sort(array):
    
    for i in range(1, len(array)):
    
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
            
        array[j + 1] = key_item

    return array


# Merge Sort
# Usually very quick due to the divide and conquer approach. Avg time complexity of O(log n).
# Requires two separate functions that work in tandem, the first sorts values from two separate lists. 


def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

# The second recursively runs the merge() function until the list is sorted.

def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))



# Quicksort, again, true to it's name, is generally very quick but could potentially run slower if the random pivot points are dog water.
# It uses a similar divide and conquer/recursion method to merge sort, but with a random pivot point instead of a midpoint.
# the quicksort algorithm can be optimized to avoid the pitfalls of random selection for the pivot point that could lead to a worst case
# of O(n**2) by instead selecting a median value using a median finding algorithm which runs in O(n), and pivoting from there.
from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

# Timsort is a combination of merge and insertion sort that takes advantage of insertion sort's efficiency on small datasets.
# It uses a run length, called min_run typically, to keep the size of the arrays at a manageable level for the insertion sort half.
# This value is typically a power of 2 (I.e. 32, 64) 