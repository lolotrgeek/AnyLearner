import os, signal, argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run an agent with command line args.')
    parser.add_argument('--pid', help='pid of process to kill"')
    args = vars(parser.parse_args())
    # for arg in args:
    #     print(type(arg), arg)
    
    pid = int(args.get("pid"))
    os.kill(pid, signal.SIGTERM) 