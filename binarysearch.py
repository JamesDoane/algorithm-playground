import math
import time
def bsearch(list, v):
    i = math.floor(len(list)/2)
    j = len(list)-1
    if len(list)<2:
        answer = list
        return answer
    if list[i] == v:
        answer = list[i]
        return answer
    if list[i] < v:
        b_list = list[i:j]
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
test_list = seed_values(56786786)
time2 = time.perf_counter()
time3 = time.perf_counter()
appropriate_value = bsearch(test_list, 49000000)
time4 = time.perf_counter()
time5 = time.perf_counter()
linear_search_result = linear_search(test_list, 49000000)
time6 = time.perf_counter()

print(f"Test list created in {time2-time1:0.4f} seconds.")
print(f"{appropriate_value} found by binary search in {time4-time3:0.4f} seconds.")
print(f"{linear_search_result} found by linear search in {time6-time5:0.4f} seconds")

