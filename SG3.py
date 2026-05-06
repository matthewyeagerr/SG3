"""
╔═════════════════════════════════════════════════════════════════════════════════════════════╗
║ SG3                                                                   					  ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Language: Python 3.13.12                                               					  ║
║ IDE: Thonny, Pycharm, VSCode                                                                ║
║ Class: CS 4500 - Intro to the Software Profession                 						  ║
║ Program: SG3 - Paint Blobs                                        						  ║
║ Authors:                                                            						  ║
║  - Zane Buchanan                                                     						  ║
║  - Tressa Millering                                                 						  ║
║  - Tori St. John                                                   						  ║
║  - Matthew Yeager                                  			                			  ║
║  - Jacob Young                                                 				    		  ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Program Description																		  ║
╠---------------------------------------------------------------------------------------------╣
║	                                                                                          ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Major Dates        																		  ║
║   - 04/21/2026 (Repository created)														  ║
║	- 04/28/2026 (Basic GUI implemented)            									      ║
║	- 04/29/2026 (Basic simulation implemented)        									      ║
║   - 05/05/2026 (First draft of program complete)     						                  ║
║   - 05/06/2026 (Bug fixing pass and minor changes complete, program finished)               ║
╟─────────────────────────────────────────────────────────────────────────────────────────────╢
║ Packages Used        																		  ║
║	- random																		          ║
║	- tkinter																		          ║
║	- time  																		          ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Outside Sources																			  ║
║     - https://stackoverflow.com/questions/42250235/border-colours-of-canvases-tkinter       ║
║           Used to add border to paint canvas                                                ║
╚═════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import random
import time
import tkinter as tk
from tkinter import simpledialog, messagebox

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Globals
root = None # main Tkinter window
canvas = None # grid drawing canvas
statsBox = None # box for statistics
statusLabel = None # progress/status display label
graphCanvas = None #canvas to draw graphs
rectangles = [] #grid of squares on the canvas

color_opts = ["red", "green", "blue"] #color options

#Defining types for readability
Grid = list[list[int]]
Coord = tuple[int, int]

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
getValidInt()
Prompts user with a pop up box for an integer input. 

	:param title     |   (str) ---> the title of the pop up box
    :param prompt    |   (str) ---> prompt given to user in pop up 
    :param low       |   (int) ---> the minimum legal value  
    :param high      |   (int) ---> the maximum legal value  

	:return: int (the final validated integer)
"""
def getValidInt(title:str, prompt:str, low:int, high:int)->int:
    while True:
        value = simpledialog.askstring(title, prompt, parent=root)

        if value is None:
            messagebox.showerror("Input Required", "You must enter a value to continue.")
            continue

        value = value.strip()

        if value == "":
            messagebox.showerror("Invalid Input", "No value was entered. Please enter a whole number.")
            continue

        if not value.isdigit():
            messagebox.showerror("Invalid Input",
                                 "Please enter digits only. Decimals, letters, and symbols are not allowed.")
            continue

        value = int(value)

        if value < low or value > high:
            messagebox.showerror("Invalid Input", f"Please enter a number from {low} to {high}.")
            continue

        return value
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
getValidN()
Calls getValidInt with values for grabbing N. 

	:return: int (call to getValidInt)
"""
def getValidN()->int:
    return getValidInt(
        "Grid Size",
        "Enter grid size N (2 to 100):",
        2,
        100
    )
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
getValidMaxT()
Calls getValidInt with values for grabbing MaxT. 

	:return: int (call to getValidInt)
"""
def getValidMaxT()->int:
    return getValidInt(
        "Maximum Time / Blobs",
        "Enter MaxT, the number of seconds/blobs to simulate (4 to 1,000,000):",
        4,
        1000000
    )
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
getValidIncrement()
Prompt user with popup box for getting a valid increment. 
    
	:param title     |   (str) ---> the title of the pop up box
    :param prompt    |   (str) ---> prompt given to user in pop up

	:return: int (the final validated increment)
"""
def getValidIncrement(title:str, prompt:str)->int:
    valid_values = [1, 10, 100, 1000]

    while True:
        value = simpledialog.askstring(title, prompt + "\nValid choices: 1, 10, 100, or 1000", parent=root)

        if value is None:
            messagebox.showerror("Input Required", "You must enter an increment to continue.")
            continue

        value = value.strip()

        if value == "":
            messagebox.showerror("Invalid Input", "No value was entered. Please enter an increment.")
            continue

        if not value.isdigit():
            messagebox.showerror("Invalid Input", "Please enter digits only.")
            continue

        value = int(value)

        if value not in valid_values:
            messagebox.showerror("Invalid Input", "The increment must be 1, 10, 100, or 1000.")
            continue

        return value
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
getMenuChoice()
Prompt user with popup box for getting menu choice on 
batch simulations. 

	:return: int (the final validated choice)
"""
def getMenuChoice()->int:
    while True:
        value = simpledialog.askstring(
            "Experiment Choice",
            "Choose the final experiment type:\n\n"
            "1. Hold MaxT constant and change N\n"
            "2. Hold N constant and change MaxT\n\n"
            "Enter 1 or 2:",
            parent=root
        )

        if value is None:
            messagebox.showerror("Input Required", "You must choose option 1 or option 2.")
            continue

        value = value.strip()

        if value not in ["1", "2"]:
            messagebox.showerror("Invalid Choice", "Please enter only 1 or 2.")
            continue

        return int(value)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
run_simulation()
Runs paint blob simulation for given values
Run paint blob simulation on NxN grid for T drops
Tracks:
top visible color on each square
total blobs per square
squares with only one color

	:param N          |   (int) ---> grid size
    :param T          |   (int) ---> ticks per sim 
    :param animate    |   (bool) --> animate sim or not, false by default
    :param anim_time  |   (float) -> target animation length, 0 by default
    :param show_stats |   (bool) --> determines if stats are output, true by default

	:return: tuple[Grid (top layer of colors),
	               Grid (# of blobs dropped on each square),
	               Grid (tracks squares that have only one color)]
"""
def run_simulation(N:int, T:int, animate:bool = False, anim_time:float = 0, show_stats:bool = True)->tuple[Grid, Grid, Grid]:

    anim_step:float = (anim_time / T)                      #sleep time between animation updates
    filled:bool = False                                    #has the grid been filled
    colors:Grid = [[0] * N for _ in range(N)]              #Track current top layer of colors. 0 none, 1 red, 2 green, 3 blue
    blob_counts:Grid = [[0] * N for _ in range(N)]         #Track how many blobs dropped on each square
    monocolor_squares:Grid = [[1] * N for _ in range(N)]   #Track if a square has more than on color dropped

    colorTotals = [0,0,0,0]

    for tick in range(T):
        updateProgress(tick + 1, T)
        new_color, loc = drop_blob(N)
        colorTotals[new_color] += 1
        if colors[loc[0]][loc[1]] not in (new_color, 0):
            monocolor_squares[loc[0]][loc[1]] = 0

        colors[loc[0]][loc[1]] = new_color
        blob_counts[loc[0]][loc[1]] += 1

        if animate:
            colorSquare(new_color, loc[0],loc[1])
            time.sleep(anim_step)


        if all(0 not in row for row in blob_counts) and not filled:
            if show_stats:
                stats = makeStats(blob_counts, monocolor_squares, tick + 1, N, colorTotals)
                printResults(stats)
            filled = True

    #squares that haven't been dropped on aren't monocolor
    for i in range(N):
        for j in range(N):
            if colors[i][j] == 0:
                monocolor_squares[i][j] = 0
        
    if show_stats:
        stats = makeStats(blob_counts, monocolor_squares, tick + 1, N, colorTotals)
        printResults(stats)

    return colors, blob_counts, monocolor_squares

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
drop_blob()
Generates location and color for new blob 

    :param N   |   (int) -> The size of the canvas, NxN

	:return: tuple[int (the color dropped),
	               Coord (the position of the drop)]
"""
def drop_blob(N:int)->tuple[int, Coord]:
    new_color:int = random.randint(1, 3)
    loc:Coord = (random.randint(0, N - 1), random.randint(0, N - 1))
    return new_color, loc

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
getBlobStats()
Computes the lowest, average, and highest blob counts for all squares in grid.

    :param blob_counts  | (Grid) --> 2D list of blob counts per square
    :param N            | (int)  --> grid dimension
    
    :return: tuple[int (lowest blob count),
                   float (average blob count),
                   int (highest blob count)]
"""
def getBlobStats(blob_counts:Grid, N:int)->tuple[int, float, int]:
    # flatten 2D grid into single list for easy min/max/sum
    counts = [blob_counts[r][c] for r in range(N) for c in range(N)]
    
    low  = min(counts)
    high = max(counts)
    avg  = sum(counts) / (N * N)
    
    return low, avg, high
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
makeStats()
builds a statistics dictionary for simulation results
tracks blobs dropped, lowest/avg/highest blob counts, 
total blobs per color, number of monocolor squares

    :param blob_counts        | (Grid) --------> 2D list of blob counts per square
    :param monocolor_squares  | (Grid) --------> 2D list of monocolor_squares
    :param blobsDropped       | (int) ---------> total blobs dropped
    :param N                  | (int) ---------> dimension of grid
    :param colorTotals        | (list[int])  --> list of color totals for all dropped blobs

    :return: dict[str, int | float] (contains stats calculated from params)
"""
def makeStats(blob_counts:Grid, monocolor_squares:Grid, blobsDropped:int, N:int, colorTotals:list[int])-> dict[str, int | float]:
    low, avg, high = getBlobStats(blob_counts, N)

    oneColorSquares = 0
    for row in monocolor_squares:
        for val in row:
            if val == 1:
                oneColorSquares += 1

    return {
        "blobsDropped": blobsDropped,
        "lowest": low,
        "highest": high,
        "average": avg,
        "red": colorTotals[1],
        "green": colorTotals[2],
        "blue": colorTotals[3],
        "oneColorSquares": oneColorSquares
    }

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
runBatchOptionOne()
Runs 10 simulations holding MaxT constant while increasing N
by increment each time. Collects low, avg, high blob counts
per simulation and displays results on graph.

    :param N         | (int) --> starting grid size
    :param MaxT      | (int) --> number of blobs dropped, stays constant
    :param increment | (int) --> how much N grows each simulation (1/10/100/1000)
    
"""
def runBatchOptionOne(N:int, MaxT:int, increment:int):
    results = []

    for i in range(10):
        currentN = N + (i * increment)  # grid grows each simulation

        # run simulation, only need blob_counts for stats
        colors, blob_counts, monocolor = run_simulation(currentN, MaxT, show_stats=False)
        
        low, avg, high = getBlobStats(blob_counts, currentN)
        
        # build result in format plotGraph expects
        results.append({"x": currentN, "lowest": low, "average": avg, "highest": high})
        
        updateProgress(i + 1, 10)  # show user something is happening
    
    plotGraph(results)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
runBatchOptionTwo()
Runs 10 simulations holding N constant while increasing MaxT
by increment each time. Collects low, avg, high blob counts
per simulation and displays results on graph.

    :param N         | (int) --> grid size, stays constant
    :param MaxT      | (int) --> starting number of blobs dropped
    :param increment | (int) --> how much MaxT grows each simulation (1/10/100/1000)
    
"""
def runBatchOptionTwo(N:int, MaxT:int, increment:int):
    results = []

    for i in range(10):
        currentMaxT = MaxT + (i * increment)  # MaxT grows each simulation

        # run simulation, only need blob_counts for stats
        colors, blob_counts, monocolor = run_simulation(N, currentMaxT, show_stats= False)
        
        low, avg, high = getBlobStats(blob_counts, N)
        
        # build result in format plotGraph expects
        results.append({"x": currentMaxT, "lowest": low, "average": avg, "highest": high})
        
        updateProgress(i + 1, 10)  # show user something is happening
    
    plotGraph(results)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
buildWindow()
Builds main TK window that houses program GUI
Uses globals root, canvas, statsbox, statusLabel, and graphCanvas
"""
def buildWindow():
    global root, canvas, statsBox, statusLabel, graphCanvas

    root = tk.Tk()
    root.title("SG3 Paint Blobs")
    root.geometry("1000x725")

    # explanation section
    explanationFrame = tk.Frame(root, borderwidth=2, relief="solid")
    explanationFrame.pack(fill="x", padx=10, pady=5)

    explanationText = (
        "SG3 Paint Blobs Simulation\n"
        "Random red, green, or blue paint blobs drop onto an NxN canvas. "
        "The newest blob is visible on each square."
    )

    explanationLabel = tk.Label(
        explanationFrame,
        text=explanationText,
        wraplength=950,
        justify="left"
    )
    explanationLabel.pack(padx=10, pady=10)

    # stats section
    statsFrame = tk.Frame(root, borderwidth=2, relief="solid")
    statsFrame.pack(fill="x", padx=10, pady=5)

    statsLabel = tk.Label(statsFrame, text="Stats", font=("Arial", 12, "bold"))
    statsLabel.pack()

    statsBox = tk.Text(statsFrame, height=7, width=100)
    statsBox.pack(padx=10, pady=5)

    statusLabel = tk.Label(statsFrame, text="Ready")
    statusLabel.pack(pady=3)

    # bottom section: grid left, graph right
    bottomFrame = tk.Frame(root)
    bottomFrame.pack(fill="both", expand=True, padx=10, pady=5)

    gridFrame = tk.Frame(bottomFrame, borderwidth=2, relief="solid")
    gridFrame.pack(side="left", fill="both", expand=True, padx=5)

    gridLabel = tk.Label(gridFrame, text="Grid", font=("Arial", 12, "bold"))
    gridLabel.pack()

    canvas = tk.Canvas(gridFrame, width=401, height=401, bg="white", highlightthickness=1, highlightbackground="black")
    canvas.pack(padx=10, pady=10)

    graphFrame = tk.Frame(bottomFrame, borderwidth=2, relief="solid")
    graphFrame.pack(side="right", fill="both", expand=True, padx=5)

    graphLabel = tk.Label(graphFrame, text="Graph", font=("Arial", 12, "bold"))
    graphLabel.pack()

    graphCanvas = tk.Canvas(graphFrame, width=550, height=450, bg="white")
    graphCanvas.pack(padx=10, pady=10)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
drawGrid()
Draw an N by N grid on the canvas.
Uses globals rectangles

    :param N   |  (int) --> grid size, stays constant
    
"""
def drawGrid(N:int):

    global rectangles

    canvas.delete("all")
    rectangles = []

    canvasSize = 400
    cellSize = canvasSize // N

    startX = 1
    startY = 1

    for row in range(N):
        rowList = []
        for col in range(N):
            x1 = startX + col * cellSize
            y1 = startY + row * cellSize
            x2 = x1 + cellSize
            y2 = y1 + cellSize

            square = canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="white",
                outline="white"
            )

            rowList.append(square)

        rectangles.append(rowList)

    root.update()

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
colorSquare()
Update one square on the canvas to the given color.
    
    :param color   |  (int) --> what to color square with
    :param row     |  (int) --> row of square to color
    :param col     |  (int) --> column of square to color
    
"""
def colorSquare(color:int, row:int, col:int):
    canvas.itemconfig(rectangles[row][col], fill=color_opts[color-1])
    root.update_idletasks()

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
updateStatus()
Display a message under the canvas.

    :param message   |  (str) --> message to put on canvas

"""
def updateStatus(message):
    statusLabel.config(text=message)
    root.update_idletasks()

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
updateProgress()
Display loading bar while the program runs.

    :param current   |  (int) --> current blob out of total
    :param total     |  (int) --> total blobs that will be dropped

"""
def updateProgress(current:int, total:int):
    bar_length: int = 30
    progress: float = current / total
    filled: int = int(progress * bar_length)
    empty: int = bar_length - filled

    bar: str = "█" * filled + "░" * empty
    percent: float = progress * 100

    updateStatus(f"{bar}  ---  {percent:.2f}%")


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
showFinalCanvas()
Display the final grid using the top color in each square.
    
    :param data   |  (Grid) --> final canvas
    
"""
def showFinalCanvas(data:Grid):

    N = len(data)
    drawGrid(N)

    for row in range(N):
        for col in range(N):
            color = data[row][col]
            if color != 0:
                colorSquare(color, row, col)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
formatStats()
Format the simulation statistics into readable text.

    :param stats  |  (dict[str, int | float]) --> final canvas

    :return: str (formatted stats)
"""
def formatStats(stats:dict[str, int | float])->str:
    text = ""
    text += "Blobs dropped: " + str(stats["blobsDropped"]) + "\n"
    text += "Lowest blobs on a square: " + str(stats["lowest"]) + "\n"
    text += "Highest blobs on a square: " + str(stats["highest"]) + "\n"
    text += "Average blobs per square: " + str(round(stats["average"], 2)) + "\n"
    text += "Red blobs: " + str(stats["red"]) + "\n"
    text += "Green blobs: " + str(stats["green"]) + "\n"
    text += "Blue blobs: " + str(stats["blue"]) + "\n"
    text += "Squares with only one color: " + str(stats["oneColorSquares"]) + "\n"
    return text

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
printResults()
Format the simulation statistics into readable text.

    :param stats  |  (str) --> stats from formatStats

"""
def printResults(stats):
    """Print formatted statistics in the stats box."""
    statsBox.insert(tk.END, formatStats(stats) + "\n")
    statsBox.see(tk.END)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
clearStats()
Empties the stats box
"""
def clearStats():
    statsBox.delete("1.0", tk.END)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
plotGraph()
Display a simple graph of lowest, average, and highest blob counts.
Plot each simulation result as:
Circle = lowest blob count
Square = average blob count
Triangle = highest blob count

    :param results  |  (dic[str, int | float]) --> stats from makeStats
"""
def plotGraph(results):
    """

    Expected results format:
    [
        {"x": 10, "lowest": 0, "average": 3.2, "highest": 8},
        {"x": 20, "lowest": 0, "average": 2.1, "highest": 6}
    ]
    """
    graphCanvas.delete("all")

    if len(results) == 0:
        return

    graphCanvas.create_text(250, 15, text="Batch Simulation Results")

    graphCanvas.create_line(50, 250, 420, 250)
    graphCanvas.create_line(50, 40, 50, 250)

    maxY = max(item["highest"] for item in results)
    if maxY == 0:
        maxY = 1

    minX = min(item["x"] for item in results)
    maxX = max(item["x"] for item in results)

    if minX == maxX:
        maxX += 1

    prevLow = None
    prevAvg = None
    prevHigh = None

    for item in results:
        x = 50 + ((item["x"] - minX) / (maxX - minX)) * 350

        lowY = 250 - (item["lowest"] / maxY) * 200
        avgY = 250 - (item["average"] / maxY) * 200
        highY = 250 - (item["highest"] / maxY) * 200

        if prevLow is not None:
            graphCanvas.create_line(prevLow[0], prevLow[1], x, lowY)
            graphCanvas.create_line(prevAvg[0], prevAvg[1], x, avgY)
            graphCanvas.create_line(prevHigh[0], prevHigh[1], x, highY)

        graphCanvas.create_oval(x - 4, lowY - 4, x + 4, lowY + 4)
        graphCanvas.create_rectangle(x - 4, avgY - 4, x + 4, avgY + 4)
        graphCanvas.create_polygon(x, highY - 5, x - 5, highY + 5, x + 5, highY + 5)

        graphCanvas.create_text(x, 265, text=str(item["x"]), font=("Arial", 8))

        prevLow = (x, lowY)
        prevAvg = (x, avgY)
        prevHigh = (x, highY)
        # axis labels
    graphCanvas.create_text(235, 290, text="Simulation Input")
    graphCanvas.create_text(15, 145, text="Blob Count", angle=90)

    graphCanvas.create_text(440, 55, text="circle = lowest")
    graphCanvas.create_text(440, 75, text="square = average")
    graphCanvas.create_text(440, 95, text="triangle = highest")



#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━




#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
Program flow:
run 10x10 simulation
run user selected simulation
display grid
run second batch experiment
display grid and statistics
"""
def main():
    buildWindow()

    # REQUIRED FIRST SIMULATION
    firstN = 10
    firstMaxT = 300

    drawGrid(firstN)
    root.update()
    time.sleep(1)

    run_simulation(
        firstN,
        firstMaxT,
        animate=True,
        anim_time=10,
    )

    # SECOND USER-CONTROLLED SIMULATION

    N = getValidN()
    MaxT = getValidMaxT()
    anim = (MaxT < 250000)
    drawGrid(N)  #rebuild canvas for new N
    colors, blob_counts, monocolor_squares = run_simulation(
        N,
        MaxT,
        animate=anim,
    )

    showFinalCanvas(colors)

    # EXPERIMENT OPTIONS
    choice = getMenuChoice()

    drawGrid(2)  #clear the canvas


    if choice == 1:
        N = getValidN()
        increment = getValidIncrement("N Increment", "Enter N increment")
        MaxT = getValidMaxT()

        runBatchOptionOne(N, MaxT, increment)

    else:
        MaxT = getValidMaxT()
        increment = getValidIncrement("T Increment", "Enter T increment")
        N = getValidN()

        runBatchOptionTwo(N, MaxT, increment)

    messagebox.showinfo("Finished", "Press OK to finish the program.")
    root.destroy()


if __name__ == "__main__":
    main()