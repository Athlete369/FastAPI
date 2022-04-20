# from threading import Thread
# from time import sleep
# from datetime import datetime

# def fun_square(arr):
#     for n in arr:
#         sleep(2)
#         print(f"Square of n is {n*n}")
# def fun_cube(arr):
#     for n in arr:
#         sleep(2)
#         print(f"Cube of n is {n*n*n}")

# if __name__=="__main__":

#     arr = [5,6,7,8,9,10]
#     startTime = datetime.now()
#     # fun_square(arr)
#     # fun_cube(arr)
#     t1 = Thread(target=fun_square,args=(arr,))
#     t2 = Thread(target=fun_cube,args=(arr,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("Multithreading test ended")
#     print(f"Total time taken = {datetime.now()-startTime}")

'''
import time
import multiprocessing
from datetime import datetime

def fun_square(arr,square_result):
    for i,n in enumerate(arr):
        time.sleep(2)
        #print(f"Square of n is {n*n}")
        square_result[i]=(n*n)
    print(square_result)  
def fun_cube(arr,square_result):
    for n in arr:
        time.sleep(2)
        #print(f"Cube of n is {n*n*n}")
if __name__ == "__main__":
    arr = [5,6,7,8,9,10]
    square_result = multiprocessing.Array('i',len(arr))
    startTime = datetime.now()
    p1 = multiprocessing.Process(target=fun_square,args=(arr,square_result,))
    p2 = multiprocessing.Process(target=fun_cube,args=(arr,square_result,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done")
    for i in (square_result):
        print(i)
    print(f"total time :{datetime.now() - startTime}")
'''

from array import array
from multiprocessing import Pool

def f(n):
    return n*n

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    p = Pool()
    result = p.map(f,arr)
    p.close()
    p.join()
    print(result)