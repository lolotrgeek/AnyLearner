# Tests looping process spawning implementations
from multiprocessing import Process
import os, time

def info(title):
    print('module name:', title, 'parent process:', os.getppid(), 'process id:', os.getpid())

def fun(name):
    while True:
        info(name)
        # print('calling ', name)
        time.sleep(2)


def main():
    try:
        info('main fun')

        names = ["alice", "bob"]
        processes = []

        for name in names:
            processes.append(Process(target=fun, args=(name,)))

        for p in processes:
            p.start()
            # p.join()

            print(f'Process p is alive: {p.is_alive()}')
    except KeyboardInterrupt:
        #ensure killed?
        pass

if __name__ == '__main__':
    main()