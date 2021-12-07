import math
import time

def bsearch(list, v):
    # declare midpoint
    i = len(list)//2
    #declare endpoint
    j = len(list)-1
    #finds items in small list
    if len(list)<5:
        for i in range(len(list)):
            if list[i] == v:
                return list[i]
    # if midpoint is value we seek, return
    if list[i] == v:
        print("found2")
        answer = list[i]
        return answer
    #if midpoint != value we seek, re-search
    if list[i] < v:
        b_list = list[i-1:j]
        return bsearch(b_list, v)
    if list[i] > v:
        b_list = list[0:i+1]
        return bsearch(b_list, v)


def seed_values(number):
    list_of_numbers = []
    for i in range(number):
        list_of_numbers.append(i)
    
    print("List created")

    return list_of_numbers


def linear_search(list, value):
    for i in list:
        if i == value:
            return i


time1 = time.perf_counter()
test_list = seed_values(56786723)
time2 = time.perf_counter()
time3 = time.perf_counter()
appropriate_value = bsearch(test_list, 49000000)
time4 = time.perf_counter()
time5 = time.perf_counter()
linear_search_result = linear_search(test_list, 49000011)
time6 = time.perf_counter()

print(f"Test list created in {time2-time1:0.4f} seconds.")
print(f"{appropriate_value} found by binary search in {time4-time3:0.4f} seconds.")
print(f"{linear_search_result} found by linear search in {time6-time5:0.4f} seconds")

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

time7 = time.perf_counter()
bsearch_results = binary_search(test_list, 0, len(test_list)-1, 49000000)
time8 = time.perf_counter()
print(f"The indentified value was found at an index of {bsearch_results} and was found in {time8-time7:0.4f} seconds.")