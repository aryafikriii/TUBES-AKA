from tkinter import *
from tkinter import ttk
import random
from colors import *
import time

# Importing algorithms 
from algorithms.insertionSort import insertion_sort
from algorithms.selectionSort import selection_sort

# Main window 
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
algo_list = ['Insertion Sort','Selection Sort']

speed_name = StringVar()
speed_list = ['Secepat Kilat', 'Sedang', 'Santai']

array_name = StringVar()
array_list = ['10', '50', '100', '500', '1000']

data = []

# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y1, anchor=SW, text=str(data[i]))

    window.update_idletasks()

# This function will generate array with random values every time we hit the generate button
def generate():
    global data

    data = []
    if array_menu.get() == '10':
        for i in range(0, 10):
            random_value = random.randint(1, 150)
            data.append(random_value)

        drawData(data, [BLUE for x in range(len(data))])
    elif array_menu.get() == '50':
        for i in range(0, 50):
            random_value = random.randint(1, 60)
            data.append(random_value)

        drawData(data, [BLUE for x in range(len(data))])
    elif array_menu.get() == '100':
        for i in range(0, 100):
            random_value = random.randint(1, 150)
            data.append(random_value)

        drawData(data, [BLUE for x in range(len(data))])
    elif array_menu.get() == '500':
        for i in range(0, 500):
            random_value = random.randint(1, 150)
            data.append(random_value)

        drawData(data, [BLUE for x in range(len(data))])
    elif array_menu.get() == '1000':
        for i in range(0, 1000):
            random_value = random.randint(1, 150)
            data.append(random_value)

        drawData(data, [BLUE for x in range(len(data))])
    

# This function will set sorting speed
def set_speed():
    if speed_menu.get() == 'Santai':
        return 0.1
    elif speed_menu.get() == 'Sedang':
        return 0.001
    else:
        return 0.0000000000000000000000000000000000000000000

# This funciton will trigger a selected algorithm and start sorting
def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Insertion Sort':
        start_time = time.time()
        insertion_sort(data, drawData, timeTick)
        end_time = time.time()
    elif algo_menu.get() == 'Selection Sort':
        start_time = time.time()
        selection_sort(data, drawData, timeTick)
        end_time = time.time()

    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Execution Time = {0} jam {1} menit {2} detik".format(int(hours),int(mins),sec))

### User interface here ###
UI_frame = Frame(window, width= 900, height=400, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm 
l1 = Label(UI_frame, text="Algoritma: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed 
l2 = Label(UI_frame, text="Kecepatan Sorting: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

l3 = Label(UI_frame, text="Jumlah Element Array: ", bg=WHITE)
l3.grid(row=2, column=0, padx=10, pady=5, sticky=W)
array_menu = ttk.Combobox(UI_frame, textvariable=array_name, values=array_list)
array_menu.grid(row=2, column=1, padx=5, pady=5)
array_menu.current(0)


# sort button 
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=4, column=1, padx=5, pady=5)

# button for generating array 
b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=4, column=0, padx=5, pady=5)

# canvas to draw our array 
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()