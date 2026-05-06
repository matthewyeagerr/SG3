#Authored by Tressa Millering

console_color_opts = ["\033[30m", "\033[31m", "\033[32m", "\033[34m"]

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
ANIMATE IN CONSOLE
FOR TESTING PURPOSES
WILL NOT ANIMATE CORRECTLY IF TKINTER WINDOW IS OPEN

\033[0m - resets color 
\033[H  - moves cursor to 1,1
"""
def console_animate(colors:list[list[int]], N:int):
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
