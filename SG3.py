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
║ Program Description                                                                         ║
╠---------------------------------------------------------------------------------------------╣
║ This script simulates dropping red, green, or blue paint blobs onto an empty canvas.        ║
║ Each tick, a blob is dropped at a random location, overwriting any prior paint. Multiple    ║
║ experiments are run using parameters provided by the user.                                  ║
║                                                                                             ║
║ On first run, an example simulation drops 300 blobs onto a 10x10 grid. Stats are shown      ║
║ up to twice: once when every cell has been covered for the first time (if ever), and once   ║
║ after the 300th blob drops.                                                                 ║
║                                                                                             ║
║ After the example, the user is prompted to enter:                                           ║
║   • N — the grid size for the next simulation                                               ║
║   • T — the number of blob drops to simulate                                                ║
║                                                                                             ║
║ A new simulation runs with these constraints, followed by a batch of 10 simulations in      ║
║ which the user chooses to increment either N or T each run. When all 10 are complete,       ║
║ stats across the batch are displayed as a graph, and the program ends.                      ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Major Data Structures Relevant to the Simulation                                            ║
╠---------------------------------------------------------------------------------------------╣
║ The main simulation returns three arrays. Each are a list of lists of integers,             ║
║ representing a grid.                                                                        ║
║   - colors, tracks the current top layer of colors on the canvas:                           ║
║         0 for none, 1 for red, 2 for green, 3 for blue                                      ║
║   - blob_counts, tracks how many blobs dropped on each square                               ║
║   - Monocolor_squares, tracks if a square has more than on color dropped                    ║
║                                                                                             ║
║ These data are processed into a dictionary used to display stats to the user. The key is    ║
║ a string and the value is an integer. The following data are included:                      ║
║   - Total blobs dropped                                                                     ║
║   - Lowest blob count on a square                                                           ║
║   - Average blobs per square                                                                ║
║   - Highest blob count on a square                                                          ║
║   - Count of red blobs                                                                      ║
║   - Count of blue blobs                                                                     ║
║   - Count of green blobs                                                                    ║
║   - Number of squares that have only had one color dropped                                  ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Major Dates        																		  ║
║   - 04/21/2026 (Repository created)														  ║
║	- 04/28/2026 (Basic GUI implemented)            									      ║
║	- 04/29/2026 (Basic simulation implemented)        									      ║
║   - 05/05/2026 (First draft of program complete)     						                  ║
║   - 05/06/2026 (Bug fixing pass and minor changes complete, program finished)               ║
╟─────────────────────────────────────────────────────────────────────────────────────────────╢
║ Packages Used        																		  ║
║	- random: used to generate random paint blob colors and grid locations					  ║
║	- tkinter: used to create GUI including windows, canvas, pop-ups, buttons, and displays   ║
║	- time: used to control animation timing and pausing during simulations                   ║
║	- matplotlib: used to create and display graphs										      ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Outside Sources																			  ║
║     - https://stackoverflow.com/questions/42250235/border-colours-of-canvases-tkinter       ║
║           Used to add border to paint canvas                                                ║
║     - https://www.geeksforgeeks.org/python/how-to-embed-matplotlib-charts-in-tkinter-gui/   ║
║     - https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html     ║
║           Both above used to add matplotlib graph to TK window                              ║
╚═════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import random
import time
import tkinter as tk
from tkinter import simpledialog, messagebox

from matplotlib import style
import matplotlib as plt
plt.style.use('bmh')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Globals
root = None # main Tkinter window
canvas = None # grid drawing canvas
statsBox = None # box for statistics
statusLabel = None # progress/status display label
graphCanvas = None #canvas to draw graphs
fig = None
ax = None
chart = None
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
                messagebox.showinfo("Canvas Filled!", "The canvas has been filled for the first time! Stats are above. Press ok to continue.")
                clearStats()
            filled = True

    #squares that haven't been dropped on aren't monocolor
    for i in range(N):
        for j in range(N):
            if colors[i][j] == 0:
                monocolor_squares[i][j] = 0

    if animate:             #tressa just thinks its a nice touch, its pointless but its satisfying to watch
        showFinalCanvas(colors)  #nothing in the assignment specs said we couldnt,
                                 # and it adds some finality to finishing an animation

    if show_stats:
        stats = makeStats(blob_counts, monocolor_squares, tick + 1, N, colorTotals)
        printResults(stats)
        messagebox.showinfo("Simulation Complete!",
                            "The simulation is complete! Stats are above.\nPress ok to continue.")

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
    
    plotGraph(results, True)

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

    plotGraph(results, False)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
buildWindow()
Builds main TK window that houses program GUI
Uses globals root, canvas, statsbox, statusLabel, and graphCanvas
"""
def buildWindow():
    global root, canvas, statsBox, statusLabel, graphCanvas, ax, fig, chart

    root = tk.Tk()
    root.title("SG3 Paint Blobs")
    root.geometry("1000x725+0+0")

    # explanation section
    explanationFrame = tk.Frame(root, borderwidth=2, relief="solid")
    explanationFrame.pack(fill="x", padx=10, pady=5)

    explanationText = (
        "\t\t\t\t   SG3 Paint Blobs Simulation\n"
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

    graphCanvas = tk.Canvas(graphFrame, width=510, height=400, bg="white", highlightthickness=1, highlightbackground="black")
    graphCanvas.pack(padx=10, pady=10)

    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    chart = FigureCanvasTkAgg(fig, master=graphCanvas)
    chart.get_tk_widget().place(x=5, y=1)

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
    percent: float= progress * 100

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
    sleep_time = 0.5 / N**2
    for row in range(N):
        for col in range(N):
            color = data[row][col]
            if color != 0:
                colorSquare(color, row, col)
                time.sleep(sleep_time)

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
    text += "Blobs dropped: " + str(stats["blobsDropped"]) + "\t\t\t\t\tAverage blobs per square: " + str(round(stats["average"], 2)) + "\n"
    text += "Lowest blobs on a square: " + str(stats["lowest"]) + "\t\t\t\t\tRed blobs: " + str(stats["red"]) + "\n"
    text += "Highest blobs on a square: " + str(stats["highest"]) + "\t\t\t\t\tGreen blobs: " + str(stats["green"]) + "\n"
    text += "Squares with only one color: " + str(stats["oneColorSquares"]) + "\t\t\t\t\tBlue blobs: " + str(stats["blue"])
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
    clearStats()
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

    :param results   |  (dict[str, int | float]) --> stats from makeStats
    :param batch_one |                    (bool) --> is a graph for batch one
"""
def plotGraph(results, batch_one:bool):
    #clear bar
    updateStatus("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
    updateStatus("Loading graph...")

    if len(results) == 0:
        return

    xs = [item["x"] for item in results]
    lows = [item["lowest"] for item in results]
    avgs = [item["average"] for item in results]
    highs = [item["highest"] for item in results]

    ax.plot(xs, lows, marker="o", linestyle="-", color="red", markersize=6, label="Lowest")
    ax.plot(xs, avgs, marker="s", linestyle="-", color="blue", markersize=6, label="Average")
    ax.plot(xs, highs, marker="^", linestyle="-", color="green", markersize=6, label="Highest")

    xAx = None
    if batch_one:
        xAx = "N Per Simulation"
    else:
        xAx = "Blobs Per Simulation"

    ax.set_title("Blobs Per Square versus " + xAx)
    ax.set_xlabel(xAx)
    ax.set_ylabel("Blob Count")
    ax.legend(loc="upper right")

    # Embed the figure in the Tkinter canvas
    chart.draw()
    updateStatus("Graph complete!")

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
    clearStats() #clear stats box
    run_simulation(
        N,
        MaxT,
        animate=anim,
    )


    #EXPERIMENT OPTIONS
    choice = getMenuChoice()

    drawGrid(2)  #clear the canvas
    clearStats() #clear stats box

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

    time.sleep(5)
    messagebox.showinfo("Finished", "Press OK to finish the program.")
    root.destroy()


if __name__ == "__main__":
    main()
