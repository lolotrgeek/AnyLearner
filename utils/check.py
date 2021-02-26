import os
pid = 1684
def check_pid(pid):        
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        print(pid, "does not exist.")
        return False
    else:
        print(pid, "Is running.")
        return True

check_pid(pid)