from multiprocessing import Process, cpu_count
import time



def count_to(x):
    count = 0
    new_list = []
    while count < x:
        new_list.append(count)
        count += 1
    
    
    print(time.perf_counter())

if __name__ == '__main__':
    print(cpu_count())
    a = Process(target=count_to, args=(250000000,))
    b = Process(target=count_to, args=(250000000,))
    

    a.start()
    b.start()
