# This infinite loop code cannot be terminated
# by pressing Ctrl-C.

from time import sleep

seconds = 0

while True:
    try:
        if seconds is 11:
            print("Let\'s stop for now, Hope you have noted that Cntrl - C has no effect in the loop", end = "")
            break
        else:
            print(seconds)
            seconds += 1
            sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")
