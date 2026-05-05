"""
╔═════════════════════════════════════════════════════════════════════════════════════════════╗
║ SG3                                                                   					  ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Language: Python 3.13.12                                               					  ║
║ IDE: Thonny, Pycharm, (IF ANYONE USES SOMETHIHNG DIFFERENT, ADD HERE)                       ║
║ Class: CS 4500 - Intro to the Software Profession                 						  ║
║ Program: SG3 - Paint Blobs                                        						  ║
║ Authors:                                                            						  ║
║  - Zane Buchanan     []                                             						  ║
║  - Tressa Millering  [dtmhg6]                                        						  ║
║  - Tori St. John     []                                              						  ║
║  - Matthew Yeager    []                              			                			  ║
║  - Jacob Young       []                                        				    		  ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Program Description																		  ║
╠---------------------------------------------------------------------------------------------╣
║	                                                                                          ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Major Dates        																		  ║
║   - 04/21/2026 (Repository created)														  ║
║	- 04/28/2026 (Basic GUI implemented)            									      ║
║	- 04/29/2026 (Basic simulation implemented)        									      ║
║                                                    						                  ║
╟─────────────────────────────────────────────────────────────────────────────────────────────╢
║ Packages Used        																		  ║
║	- random																		          ║
║	- tkinter																		          ║
║	- time  																		          ║
║                                  							          						  ║
╠━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╣
║ Outside Sources																			  ║
║     - https://stackoverflow.com/questions/42250235/border-colours-of-canvases-tkinter       ║
║           Used to add border to paint canvas                                                ║
╚═════════════════════════════════════════════════════════════════════════════════════════════╝
"""

import random
import time
import tkinter as tk


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Globals  (ADD DOCUMENTATION)
root = None
canvas = None
statsBox = None
statusLabel = None
graphCanvas = None

rectangles = []
#Think this can be removed; its immediately overwritten the one time its used
#cellSize = 25

color_opts = ["red", "green", "blue"]
console_color_opts = ["\033[30m", "\033[31m", "\033[32m", "\033[34m"]

#Defining types for readability
Grid = list[list[int]]
Coord = tuple[int, int]



# -function prototypes ---

# Person 3
# makeGridData(N)
# dropBlob(data)
# runSim(N, MaxT)
# computeStats(data, blobsDropped)
# checkAllSquaresPainted(data)

# Person 2
# getValidN()
# getValidMaxT()
# getValidIncrement()
# getMenuChoice()

# Person 5
# runBatchOptionOne(N, MaxT, increment)
# runBatchOptionTwo(N, MaxT, increment)


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
ANIMATE IN CONSOLE
FOR TESTING PURPOSES
WILL NOT ANIMATE CORRECTLY IF TKINTER WINDOW IS OPEN

\033[0m - resets color 
\033[H  - moves cursor to 1,1
"""
def console_animate(colors:Grid, N:int):
    reset = "\033[0m"
    print("\033[H", end="", flush=True)
    for i in range(N):
        print("[", end="")
        for j in range(N):
            color = console_color_opts[colors[i][j]]
            print(f"{color}●{reset} ", end="")
        print("\b]")
    print()


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
FOR TESTING
Just prints a 2D array in multiple lines. Can give it a label too
"""
def print_array(array, length, label=""):
    print(label + (":" if (label != "") else ""))
    for _ in range(0, length):
        print(array[_])
    print("\n")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
ADD DESCRIPTION
runs simulation, obviously. ill add a better description later
Will remove debug and gui before submission. 
This function declaration is disgustingly long lmao

	:param N         |   (int) ---> grid size
    :param T         |   (int) ---> ticks per sim 
    :param animate   |   (bool) --> animate sim or not, false by default
    :param anim_time |   (float) -> animation length
    :param debug     |   (bool) --> outputs data to console for testing. false by default
    :param gui       |   (bool) --> if gui is open (true), animates it. false by default  

	:return: tuple[Grid (top layer of colors),
	               Grid (# of blobs dropped on each square),
	               Grid (tracks squares that have only one color)]
"""
def run_simulation(N:int, T:int, animate:bool = False, anim_time:float = 0, debug:bool = False, gui:bool = False)->tuple[Grid, Grid, Grid]:

    anim_step:float = (anim_time / T)                      #sleep time between animation updates
    filled:bool = False                                    #has the grid been filled
    colors:Grid = [[0] * N for _ in range(N)]              #Track current top layer of colors. 0 none, 1 red, 2 green, 3 blue
    blob_counts:Grid = [[0] * N for _ in range(N)]         #Track how many blobs dropped on each square
    monocolor_squares:Grid = [[1] * N for _ in range(N)]   #Track if a square has more than on color dropped

    start = 0
    if debug:
        start = time.perf_counter()

    for tick in range(T):
        updateProgress(tick, T)
        new_color, loc = drop_blob(N)
        if colors[loc[0]][loc[1]] not in (new_color, 0):
            monocolor_squares[loc[0]][loc[1]] = 0

        colors[loc[0]][loc[1]] = new_color
        blob_counts[loc[0]][loc[1]] += 1

        if animate:
            if gui:
                colorSquare(new_color, loc[0],loc[1])
            time.sleep(anim_step)
            #if debug:
                #console_animate(colors, N)

        if 0 not in blob_counts and tick != T and not filled:
            #Call whatever the output stats function will be
            filled = True

    #squares that haven't been dropped on aren't monocolor
    for i in range(N):
        for j in range(N):
            if colors[i][j] == 0:
                monocolor_squares[i][j] = 0

    if debug:
        end = time.perf_counter()
        print("TIME:", format(end-start, '.2f'), "seconds" "\n")
        print_array(colors, N, "COLORS")
        print_array(monocolor_squares, N, "MONOCOLOR SQUARES")
        total = 0
        for row in blob_counts:
            for val in row:
                total += val
        print("TOTAL BLOB COUNT: ", total, "\nEXPECTED: ", T)
        print_array(blob_counts, N, "BLOB COUNT")

    return colors, blob_counts, monocolor_squares

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
ADD DOCUMENTATION
"""
def drop_blob(N:int)->tuple[int, Coord]:
    new_color:int = random.randint(1, 3)
    loc:Coord = (random.randint(0, N - 1), random.randint(0, N - 1))
    return new_color, loc

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
Computes the lowest, average, and highest blob counts for all squares in grid.

    :param blob_counts  | (Grid) --> 2D list of blob counts per square
    :param N            | (int)  --> grid dimension
    
    :return: tuple of (lowest, average, highest) blob counts
"""
def getBlobStats(blob_counts:Grid, N:int)->tuple[int, float, int]:
    # flatten 2D grid into single list for easy min/max/sum
    counts = [blob_counts[r][c] for r in range(N) for c in range(N)]
    
    low  = min(counts)
    high = max(counts)
    avg  = sum(counts) / (N * N)
    
    return low, avg, high
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
Runs 10 simulations holding MaxT constant while increasing N
by increment each time. Collects low, avg, high blob counts
per simulation and displays results on graph.

    :param N         | (int) --> starting grid size
    :param MaxT      | (int) --> number of blobs dropped, stays constant
    :param increment | (int) --> how much N grows each simulation (1/10/100/1000)
    
    :return: None
"""
def runBatchOptionOne(N:int, MaxT:int, increment:int):
    results = []
    
    for i in range(10):
        currentN = N + (i * increment)  # grid grows each simulation
        
        # run simulation, only need blob_counts for stats
        colors, blob_counts, monocolor = run_simulation(currentN, MaxT)
        
        low, avg, high = getBlobStats(blob_counts, currentN)
        
        # build result in format plotGraph expects
        results.append({"x": currentN, "lowest": low, "average": avg, "highest": high})
        
        updateProgress(i + 1, 10)  # show user something is happening
    
    plotGraph(results)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
Runs 10 simulations holding N constant while increasing MaxT
by increment each time. Collects low, avg, high blob counts
per simulation and displays results on graph.

    :param N         | (int) --> grid size, stays constant
    :param MaxT      | (int) --> starting number of blobs dropped
    :param increment | (int) --> how much MaxT grows each simulation (1/10/100/1000)
    
    :return: None
"""
def runBatchOptionTwo(N:int, MaxT:int, increment:int):
    results = []
    
    for i in range(10):
        currentMaxT = MaxT + (i * increment)  # MaxT grows each simulation
        
        # run simulation, only need blob_counts for stats
        colors, blob_counts, monocolor = run_simulation(N, currentMaxT)
        
        low, avg, high = getBlobStats(blob_counts, N)
        
        # build result in format plotGraph expects
        results.append({"x": currentMaxT, "lowest": low, "average": avg, "highest": high})
        
        updateProgress(i + 1, 10)  # show user something is happening
    
    plotGraph(results)
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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

    graphCanvas = tk.Canvas(graphFrame, width=450, height=450, bg="white")
    graphCanvas.pack(padx=10, pady=10)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def drawGrid(N:int):
    """Draw an N by N grid on the canvas."""
    global rectangles, cellSize

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
def colorSquare(color, row, col):
    """Update one square on the canvas to the given color."""
    canvas.itemconfig(rectangles[row][col], fill=color_opts[color-1])
    root.update_idletasks()

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def updateStatus(message):
    """Display a message under the canvas."""
    statusLabel.config(text=message)
    root.update_idletasks()

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def updateProgress(current, total):
    """Display simulation progress while the program runs."""
    bar_length: int = 30
    progress: float = current / (total-1)
    filled: int = int(progress * bar_length)
    empty: int = bar_length - filled

    bar: str = "█" * filled + "░" * empty
    percent: float = progress * 100

    updateStatus(f"{bar}  ---  {percent:.2f}%")

  #  percent = round((current / total) * 100, 1)
  #  updateStatus("Progress: " + str(current) + "/" + str(total) + " drops (" + str(percent) + "%)")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def showFinalCanvas(data):
    """
    Display the final grid using the top color in each square.

    Expected data format:
    data[row][col]["topColor"]
    """
    N = len(data)
    drawGrid(N)

    for row in range(N):
        for col in range(N):
            color = data[row][col]["topColor"]
            colorSquare(color, row, col)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def formatStats(stats):
    """Format the simulation statistics into readable text."""
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
def printResults(stats):
    """Print formatted statistics in the stats box."""
    statsBox.insert(tk.END, formatStats(stats) + "\n")
    statsBox.see(tk.END)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def clearStats():
    """Clear the stats box."""
    statsBox.delete("1.0", tk.END)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def plotGraph(results):
    """
    Display a simple graph of lowest, average, and highest blob counts.

    Expected results format:
    [
        {"x": 10, "lowest": 0, "average": 3.2, "highest": 8},
        {"x": 20, "lowest": 0, "average": 2.1, "highest": 6}
    ]
    """
    graphCanvas.delete("all")

    if len(results) == 0:
        return

    graphCanvas.create_text(300, 15, text="Batch Simulation Results")

    graphCanvas.create_line(50, 250, 560, 250)
    graphCanvas.create_line(50, 40, 50, 250)

    maxY = max(item["highest"] for item in results)
    if maxY == 0:
        maxY = 1

    minX = min(item["x"] for item in results)
    maxX = max(item["x"] for item in results)

    if minX == maxX:
        maxX += 1

    for item in results:
        x = 50 + ((item["x"] - minX) / (maxX - minX)) * 500

        lowY = 250 - (item["lowest"] / maxY) * 200
        avgY = 250 - (item["average"] / maxY) * 200
        highY = 250 - (item["highest"] / maxY) * 200

        graphCanvas.create_oval(x - 4, lowY - 4, x + 4, lowY + 4)
        graphCanvas.create_rectangle(x - 4, avgY - 4, x + 4, avgY + 4)
        graphCanvas.create_polygon(x, highY - 5, x - 5, highY + 5, x + 5, highY + 5)

        graphCanvas.create_text(x, 265, text=str(item["x"]), font=("Arial", 8))

    graphCanvas.create_text(475, 55, text="circle = lowest")
    graphCanvas.create_text(475, 75, text="square = average")
    graphCanvas.create_text(475, 95, text="triangle = highest")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━




#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def main():
    # person 1 flow
    # build window
    # run first
    # run second
    #run choice
    buildWindow()
    N = 100
    drawGrid(N)

    # for i in range(N):
    #     colorSquare(3, i, 0)
    #     colorSquare(3, i, N-1)
    #     colorSquare(3, 0, i)
    #     colorSquare(3, N-1, i)

    colors, blob_counts, monocolor_squares = run_simulation(N, 10000, True, 0, gui=True,debug=True)
    root.mainloop()
    pass

if __name__ == "__main__":
    main()
