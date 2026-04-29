import tkinter as tk
import random

root = None
canvas = None
statsBox = None
statusLabel = None
graphCanvas = None

rectangles = []
cellSize = 25

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

def buildWindow():
    global root, canvas, statsBox, statusLabel, graphCanvas

    root = tk.Tk()
    root.title("SG3 Paint Blobs")
    root.geometry("1000x700")

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

    canvas = tk.Canvas(gridFrame, width=450, height=350, bg="white")
    canvas.pack(padx=10, pady=10)

    graphFrame = tk.Frame(bottomFrame, borderwidth=2, relief="solid")
    graphFrame.pack(side="right", fill="both", expand=True, padx=5)

    graphLabel = tk.Label(graphFrame, text="Graph", font=("Arial", 12, "bold"))
    graphLabel.pack()

    graphCanvas = tk.Canvas(graphFrame, width=450, height=350, bg="white")
    graphCanvas.pack(padx=10, pady=10)

def drawGrid(N):
    """Draw an N by N grid on the canvas."""
    global rectangles, cellSize

    canvas.delete("all")
    rectangles = []

    canvasSize = 350
    cellSize = canvasSize // N

    startX = 50
    startY = 0

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
                outline="black"
            )

            rowList.append(square)

        rectangles.append(rowList)

    root.update()


def colorSquare(color, row, col):
    """Update one square on the canvas to the given color."""
    canvas.itemconfig(rectangles[row][col], fill=color)
    root.update_idletasks()


def updateStatus(message):
    """Display a message under the canvas."""
    statusLabel.config(text=message)
    root.update_idletasks()


def updateProgress(current, total):
    """Display simulation progress while the program runs."""
    percent = round((current / total) * 100, 1)
    updateStatus("Progress: " + str(current) + "/" + str(total) + " drops (" + str(percent) + "%)")


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


def printResults(stats):
    """Print formatted statistics in the stats box."""
    statsBox.insert(tk.END, formatStats(stats) + "\n")
    statsBox.see(tk.END)


def clearStats():
    """Clear the stats box."""
    statsBox.delete("1.0", tk.END)


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


def main():
    # person 1 flow
    # build window
    # run first
    # run second
    #run choice
    pass

if __name__ == "__main__":
    main()

