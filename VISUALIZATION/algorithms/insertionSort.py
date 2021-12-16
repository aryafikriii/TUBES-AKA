# We need the time module to create some time difference between each comparison
import time

# Importing colors from colors.py
from colors import *

def insertion_sort(data, drawData, timeTick):
    # Traverse through 1 to len(data)
    for i in range(1, len(data)):

        key = data[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < data[j] :
                data[j+1] = data[j]
                j -= 1
                drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))])
                time.sleep(timeTick)
        data[j+1] = key

    drawData(data, [BLUE for x in range(len(data))])