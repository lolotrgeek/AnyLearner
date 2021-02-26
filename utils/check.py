import os, signal, argparse

def check_pid(pid):        
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except:
        print(pid, "does not exist.")
        return False
    else:
        print(pid, "Is running.")
        return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run an agent with command line args.')
    parser.add_argument('--pid', help='pid of process to check"')
    args = vars(parser.parse_args())
    # for arg in args:
    #     print(type(arg), arg)
    
    pid = int(args.get("pid"))
    check_pid(pid)
