import time


try:
    1/0
except Exception:
    print('e')

def causeError():
    start = time.time()
    try:
        time.sleep(0.5)
        1/0
    except Exception:
        print('e')
    finally:
        print(f'ran for {(time.time()-start)}')
    
causeError()