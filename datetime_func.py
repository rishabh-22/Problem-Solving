# to find the number of seconds between two given dates.


#!/bin/python3

import os
from datetime import datetime
import time


# Complete the time_delta function below.
def time_delta(t1, t2):
    time1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    time2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    elapsed_time = abs(time1-time2)
    total_time = 0
    if hasattr(elapsed_time, 'days'):
        total_time += (elapsed_time.days * 24 * 3600)
    if hasattr(elapsed_time, 'hours'):
        total_time += (elapsed_time.hours * 3600)
    if hasattr(elapsed_time, 'minutes'):
        total_time += (elapsed_time.minutes * 60)
    if hasattr(elapsed_time, 'seconds'):
        total_time += elapsed_time.seconds
    print(total_time)
    return str(total_time)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
