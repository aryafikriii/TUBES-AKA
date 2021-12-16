# We need the time module to create some time difference between each comparison
import time

# Importing colors from colors.py
from colors import *

def selection_sort(data, drawData, timeTick):
    # i indicates how many items were sorted
    for i in range(len(data)-1):
        # To find the minimum value of the unsorted segment
        # We first assume that the first element is the lowest
        min_index = i
        # We then use j to loop through the remaining elements
        for j in range(i+1, len(data)):
            # Update the min_index if the element at j is lower than it
            if data[j] < data[min_index]:
                min_index = j
                drawData(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))] )
                time.sleep(timeTick)
        # After finding the lowest item of the unsorted regions, swap with the first unsorted item
        data[i], data[min_index] = data[min_index], data[i]

    
    drawData(data, [BLUE for x in range(len(data))])
