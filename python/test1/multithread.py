import threading
import time


def square(numbers):
    print('Calculating the square of a number')
    for i in numbers:
        time.sleep(0.2)
        print(f'square {i}: ', i**2)


def cube(numbers):
    print('Calculating the cube of a number')
    for i in numbers:
        time.sleep(0.2)
        print(f'cube {i}: ', i*i*i)


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t = time.time()

# square(num)
# cube(num)
t1 = threading.Thread(target=square, args=(num,))
t2 = threading.Thread(target=cube, args=(num,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f'the duration was: ', time.time()-t)
