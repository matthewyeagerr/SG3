import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import matplotlib.pyplot as plt

# Global constants and shared values

COLORS = ["red", "green", "blue"]
WHITE = "white"
CELL_SIZE_DEFAULT = 20

root = None
canvas = None
status_label = None

def getValidInt(title, prompt, low, high):

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
            messagebox.showerror("Invalid Input", "Please enter digits only. Decimals, letters, and symbols are not allowed.")
            continue

        value = int(value)

        if value < low or value > high:
            messagebox.showerror("Invalid Input", f"Please enter a number from {low} to {high}.")
            continue

        return value


def getValidIncrement(title, prompt):
 
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


def getMenuChoice():
  
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
