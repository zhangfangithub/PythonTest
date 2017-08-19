from socket import *
import threading
import queue
from concurrent.futures import ProcessPoolExecutor, as_completed,ThreadPoolExecutor
import time

q = queue.Queue()

port_List = list(range(10000))
ip = '123.57.143.114'

def portScanner(port):
    global openNum
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((ip,port))
        q.put(port)
        print('[+] %d open' % port)
        s.close()
    except:
        pass

def main():
    setdefaulttimeout(1)
    start = time.time()
    with ThreadPoolExecutor(max_workers=9999) as executor:
        executor.map(portScanner, port_List)

    print('[*] The scan is complete!')

    while not q.empty():
        print(q.get())

    print('COST: {}'.format(time.time() - start))

if __name__ == '__main__':
    main()