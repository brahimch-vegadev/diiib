import csv
import json
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import random
import time


def draw_wolf(output_text):
    # ASCII art representation of a wolf
    wolf_ascii = [
        "    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⡁",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⢿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⢹⣿⡿⠁⠈⠛⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠟⠁⠀⢻⣿⣿⠉⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠈⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠋⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⢀⡾⠀⠀⠀⢿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠃⠀⠀⠸⣄⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⠀⣼⡇⠀⠀⠀⠈⣿⣿⣷⡄⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⢿⠏⠀⠀⠀⠀⣿⡄⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣧⣿⡇⠀⠀⠀⠀⠙⠈⠻⣿⣾⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⡿⠋⠘⠀⠀⠀⠀⢀⣿⣷⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠟⠉⣿⡄⠀⠀⠀⠀⠀⠀⠙⢿⡿⣿⣶⣤⣤⣀⣀⣀⣀⣤⣴⣿⡿⣿⠏⠀⠀⠀⠀⠀⠀⠀⣼⡏⠙⢿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠠⠟⢹⣿⣿⠃⠀⠀⠈⠿⣆⡀⠀⠀⠀⠀⠀⠀⠙⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠀⠐⠁⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠈⢻⣿⡏⠙⠳⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠈⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠖⠀⠀⠀⣀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⣄⡀⠀⠀⠀⢾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣧⡖⠀⣠⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⠳⣼⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣤⣾⣿⠟⠀⠀⠀⠀⠀⠀⢀⣠⠀⠀⠀⠀⠀⠀⠀⢠⣿⣷⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣦⣼⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⣠⣶⣿⣭⣤⣤⣴⣾⣆⣤⠀⠀⣾⣿⣿⡄⠀⢠⠀⣿⣷⣤⣬⣬⣽⣷⣤⡀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⡏⠀⠀⠀⢀⣾⣿⠟⠁⠈⠉⠛⠋⠹⣿⠚⣷⣼⣿⣿⣿⣿⣤⡿⣸⡟⠉⠛⠋⠉⠈⠙⢿⣿⣆⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣟⣿⡿⠿⣿⠿⢷⡶⣄⠀⢻⡆⣿⣿⣿⣿⣿⣿⣿⡇⣿⠁⢀⣴⣶⠿⣿⠿⠿⣿⣾⡆⠀⠀⠀⠸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⢀⣼⣿⡿⠛⢱⣿⠃⠀⠀⠀⠀⢸⣿⣤⠀⠻⢷⣌⣉⣸⣧⣀⣧⣿⣿⣿⣿⣿⣿⣿⣧⣇⣠⣿⣈⣹⣶⠿⠃⣤⣽⣿⠻⠀⠀⠀⠀⢻⣧⠙⢿⣿⣿⣆⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⢠⣾⣿⠋⠀⣰⣿⡇⠀⢀⣤⣾⠃⠈⠉⣽⣷⣤⠀⠈⠉⠉⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣉⠉⠉⠁⠤⣶⣿⡉⠉⠀⢻⣦⣀⠀⠈⣿⣧⡀⠘⢿⣿⣆⠀⠀⠀⠀",
        "⠀⠀⠀⢠⣿⡿⠁⢀⣼⣿⣿⣠⣶⣿⣿⡇⠀⠐⠾⠿⠿⢶⣶⣾⠿⣶⣶⣿⡿⢿⣿⣿⣿⣿⣿⣿⠟⣿⣶⣤⠾⢿⣶⣶⠾⠿⠿⠖⠀⠈⣿⣿⣷⣦⣸⣿⣷⡄⠀⠹⣿⣧⠀⠀⠀",
        "⠀⠀⢀⣾⡟⠁⢀⣾⣿⣿⠿⠋⢠⣿⣿⢀⡀⠀⠀⠀⠒⠋⠉⠁⠀⠘⣿⠟⠀⠀⢿⣿⣿⣿⣿⠃⠀⠙⣿⣿⠀⠀⠉⠙⠓⠂⠀⠀⠀⡀⢸⣿⣇⠉⠻⢿⣿⣿⣆⠀⠹⣿⡆⠀⠀",
        "⠀⠀⢸⡟⠁⢀⣾⡿⠋⠁⠀⠀⢸⣿⣿⡟⠁⠀⢀⣀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠈⢿⣿⣿⠁⠀⠀⠀⠙⣿⠀⠀⠀⠀⠀⠀⣀⠀⠀⠹⣾⣿⣿⠀⠀⠀⠉⠻⢿⡆⠀⠹⣷⡀⠀",
        "⠀⠀⡿⠁⠀⡸⠋⠀⠀⠀⠀⠀⢸⣿⣿⢃⣤⣶⣿⠁⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⢿⠃⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠹⣿⣦⡀⢹⣿⣿⠃⠀⠀⠀⠀⠈⢻⡄⠀⢹⡇⠀",
        "⠀⢸⡇⠀⢀⣡⣤⣶⣶⣶⡇⠀⢸⣿⣿⡿⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⣿⣿⢿⣿⣿⡿⠀⠀⢷⣶⣶⣦⣄⡁⠀⠈⣇⠀",
        "⠀⣸⠁⣰⣾⠟⠹⣿⣿⣿⠁⠀⠈⣿⡿⠁⠘⣿⣇⠀⠀⠀⠀⡀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⡀⠀⠀⠀⢀⣿⡟⠀⢹⣿⡇⠀⠀⢸⣿⣿⡟⠙⠿⣶⡀⢸⡀",
        "⢀⣿⣾⠏⠀⠀⠀⢻⣿⣿⡄⠀⠀⢸⡇⠀⠀⠘⣿⣄⠀⠀⣸⡃⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⠀⠀⢀⣾⡟⠀⠀⠀⡿⠁⠀⠀⣸⣿⣿⠇⠀⠀⠈⠳⣾⡇",
        "⣸⠟⠁⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠁⠀⠀⠀⠈⢿⣦⡀⢹⣧⠀⠀⠀⠘⠛⠛⠛⣿⣿⣿⡟⠛⠛⠟⠀⠀⠀⢀⣿⠀⣠⣿⠏⠀⠀⠀⠀⠁⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠙⢷",
        "⠋⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⠀⠀⠀⣀⡀⠀⠀⠀⠀⠙⢿⣦⣿⣄⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⢀⣾⣯⣾⠟⠁⠀⠀⠀⠀⢀⡀⠀⠀⢸⣿⡟⠁⠀⠀⠀⠀⠀⠀⠈",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣇⠀⢰⣿⠻⢦⣄⠀⠀⠀⠀⠙⣿⣿⣦⣀⠀⠀⠀⢈⣿⣿⣿⡋⠀⠀⠀⢀⣠⣾⣿⡟⠁⠀⠀⠀⢀⣴⡾⢻⡇⠀⢠⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣇⢸⣿⠀⠀⠙⢷⣄⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⠛⠛⠉⠙⠛⢻⣿⣿⣿⣿⣿⠋⠀⠀⠀⢀⡴⠛⠁⠀⢸⡇⢠⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⠀⠀⠀⠀⠘⢷⡀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣦⣤⣤⣶⣿⣿⣿⣿⣿⡏⠀⠀⢀⣴⠋⠀⠀⠀⠀⢸⣷⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⡇⠀⠀⠀⠀⠀⠻⣦⠀⠀⠹⡟⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠙⡿⠀⠀⢠⡾⠁⠀⠀⠀⠀⢀⣾⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠹⣧⡀⠀⠁⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⠁⣄⠁⠀⣰⡿⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⣼⣧⠀⢿⠟⣿⣿⣿⡿⣿⠃⢀⣿⠀⣰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠈⣇⢻⣿⣿⠀⡟⠀⢸⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⠟⣿⡄⠀⠹⠘⣿⡿⠘⠀⠀⣿⡟⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⢿⣷⠀⠀⠀⣿⡇⠀⠀⢠⣿⠁⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠈⣿⡄⠀⠀⢿⠀⠀⠀⣾⡏⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠹⣷⠀⠀⠀⠀⠀⣰⡿⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⢀⡄⣄⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠀⣿⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣆⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡟⠀                                    ",
    ]

    # Display the wolf ASCII art in the Tkinter canvas
    y = 100
    for line in wolf_ascii:
        output_text.insert(tk.END, line + "\n")
    output_text.insert(tk.END, "\n")


def add_phone_numbers(leads, country_codes, oprator_codes, output_text):
    for idx, lead in enumerate(leads, start=1):
        country_name = lead["country"]
        if country_name in country_codes:
            country_code = country_codes[country_name]
            oprator_code = random.choice(oprator_codes.get(country_name, ["Oprator Code "]))  # Randomly select an area code
            phone_line = random.randint(10000000, 99999999)
            mobile_number = f"{country_code} {oprator_code} {phone_line}"  # Randomly generate phone number
            lead["phone_number"] = mobile_number
            name = lead["name"]
            email = lead["email"] 
            output_text.insert(
                tk.END,
                f"Phone Number: {mobile_number}  Name: {name}\n",
            )
            output_text.see(tk.END)  # Scroll to the end of the text widget
            output_text.update()  # Update the display
            time.sleep(0.5)  # Add delay between displaying each lead
        else:
            lead["phone_number"] = "Country Code not available"


def export_to_csv(leads):
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['id','name', 'email', 'country', 'project', 'date', 'phone_number']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for lead in leads:
                writer.writerow(lead)
        messagebox.showinfo("Export Successful", "Leads with phone numbers exported successfully!")
    else:
        messagebox.showwarning("Export Failed", "Please select a file path to save the leads.")


def process_leads(data_file, output_text):
    # Load leads from JSON file
    with open(data_file, "r") as file:
        leads = json.load(file)
    oprator_codes = {
        "Russia": ["495","499","812","910", "911", "912", "913", "914", "915", "916", "917", "918", "919","900", "902", "903", "904", "905", "906", "909","920", "921", "922", "923", "924", "925", "926", "927", "928", "929"],
        "Spain": ["6", "7"],
        "France": ["6", "7"],
        "China" : ["199", "197","198", "191", "17", "18", "192","193","194","195","196","181","182","184","185","180","186","187","188","189"],
        "India": ["981", "982", "983", "984", "988", "970", "996", "997", "998", "999"],
        "Indonesia" : ["881", "882", "883", "884", "885", "895", "896", "897", "898", "899", "817", "818", "819", "859", "877", "878", "814", "815", "816", "855", "856", "857", "858", "811", "812", "813", "821", "822", "823", "851", "852", "853"],
        "United Kingdom" : ["7400", "745", "746", "753", "755", "756", "757", "758", "759", "750", "752", "753", "755", "756", "757", "759", "748", "772", "773", "774", "775", "776", "777", "778", "779", "770", "771"],
        "United States" : ["212", "646", "917", "213", "310", "323", "312", "773", "872", "281", "346", "713", "832", "415", "628", "305", "786", "214", "469", "972"],
        "Argentina" : ["351", "341", "261", "221", "223", "387", "264"],
        "Japan" : ["70", "80", "90"],
        "Canada": ["204", "226", "236", "249", "250", "289", "306", "343", "365", "367", "403", "416", "418", "431", "437", "438", "450", "506", "514", "519", "548", "579", "581", "587", "604", "613", "639", "647", "672", "705", "709", "778", "780", "782", "807", "819", "825", "867", "873", "902", "905"],
        "Australia": ["4"],
        "Brazil": ["11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22", "24", "27", "28", "31", "32", "33", "34", "35", "37", "38", "41", "42", "43", "44", "45", "46", "47", "48", "49", "51", "53", "54", "55", "61", "62", "63", "64", "65", "66", "67", "68", "69", "71", "73", "74", "75", "77", "79", "81", "82", "83", "84", "85", "86", "87", "88", "89", "91", "92", "93", "94", "95", "96", "97", "98", "99"],
        "South Africa": ["60", "61", "62", "63", "64", "65", "66", "67", "68", "69"],
        "Egypt": ["10", "11", "12", "15"],
        "Algeria": ["5", "6", "7"],
        "Tunisia": ["20", "21", "22", "23", "24", "25", "29", "50", "52", "58"],
        "Italy": ["320", "322", "323", "324", "327", "328", "329", "330", "331", "333", "334", "335", "336", "338", "339", "340", "341", "342", "343"],
        "Germany": ["15", "16", "17"],
        "Mexico": ["55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74"],
    }    
    country_codes = {
        "Afghanistan": "+93",
        "Aland Islands": "+358",
        "Albania": "+355",
        "Algeria": "+213",
        "AmericanSamoa": "+1684",
        "Andorra": "+376",
        "Angola": "+244",
        "Anguilla": "+1264",
        "Antarctica": "+672",
        "Antigua and Barbuda": "+1268",
        "Argentina": "+54",
        "Armenia": "+374",
        "Aruba": "+297",
        "Australia": "+61",
        "Austria": "+43",
        "Azerbaijan": "+994",
        "Bahamas": "+1242",
        "Bahrain": "+973",
        "Bangladesh": "+880",
        "Barbados": "+1246",
        "Belarus": "+375",
        "Belgium": "+32",
        "Belize": "+501",
        "Benin": "+229",
        "Bermuda": "+1441",
        "Bhutan": "+975",
        "Bolivia, Plurinational State of": "+591",
        "Bosnia and Herzegovina": "+387",
        "Botswana": "+267",
        "Brazil": "+55",
        "British Indian Ocean Territory": "+246",
        "Brunei Darussalam": "+673",
        "Bulgaria": "+359",
        "Burkina Faso": "+226",
        "Burundi": "+257",
        "Cambodia": "+855",
        "Cameroon": "+237",
        "Canada": "+1",
        "Cape Verde": "+238",
        "Cayman Islands": "+ 345",
        "Central African Republic": "+236",
        "Chad": "+235",
        "Chile": "+56",
        "China": "+86",
        "Christmas Island": "+61",
        "Cocos (Keeling) Islands": "+61",
        "Colombia": "+57",
        "Comoros": "+269",
        "Congo": "+242",
        "Congo, The Democratic Republic of the Congo": "+243",
        "Cook Islands": "+682",
        "Costa Rica": "+506",
        "Cote d'Ivoire": "+225",
        "Croatia": "+385",
        "Cuba": "+53",
        "Cyprus": "+357",
        "Czech Republic": "+420",
        "Denmark": "+45",
        "Djibouti": "+253",
        "Dominica": "+1767",
        "Dominican Republic": "+1849",
        "Ecuador": "+593",
        "Egypt": "+20",
        "El Salvador": "+503",
        "Equatorial Guinea": "+240",
        "Eritrea": "+291",
        "Estonia": "+372",
        "Ethiopia": "+251",
        "Falkland Islands (Malvinas)": "+500",
        "Faroe Islands": "+298",
        "Fiji": "+679",
        "Finland": "+358",
        "France": "+33",
        "French Guiana": "+594",
        "French Polynesia": "+689",
        "Gabon": "+241",
        "Gambia": "+220",
        "Georgia": "+995",
        "Germany": "+49",
        "Ghana": "+233",
        "Gibraltar": "+350",
        "Greece": "+30",
        "Greenland": "+299",
        "Grenada": "+1473",
        "Guadeloupe": "+590",
        "Guam": "+1671",
        "Guatemala": "+502",
        "Guernsey": "+44",
        "Guinea": "+224",
        "Guinea-Bissau": "+245",
        "Guyana": "+595",
        "Haiti": "+509",
        "Holy See (Vatican City State)": "+379",
        "Honduras": "+504",
        "Hong Kong": "+852",
        "Hungary": "+36",
        "Iceland": "+354",
        "India": "+91",
        "Indonesia": "+62",
        "Iran, Islamic Republic of Persian Gulf": "+98",
        "Iraq": "+964",
        "Ireland": "+353",
        "Isle of Man": "+44",
        "Israel": "+972",
        "Italy": "+39",
        "Jamaica": "+1876",
        "Japan": "+81",
        "Jersey": "+44",
        "Jordan": "+962",
        "Kazakhstan": "+77",
        "Kenya": "+254",
        "Kiribati": "+686",
        "Korea, Democratic People's Republic of Korea": "+850",
        "Korea, Republic of South Korea": "+82",
        "Kuwait": "+965",
        "Kyrgyzstan": "+996",
        "Laos": "+856",
        "Latvia": "+371",
        "Lebanon": "+961",
        "Lesotho": "+266",
        "Liberia": "+231",
        "Libyan Arab Jamahiriya": "+218",
        "Liechtenstein": "+423",
        "Lithuania": "+370",
        "Luxembourg": "+352",
        "Macao": "+853",
        "Macedonia": "+389",
        "Madagascar": "+261",
        "Malawi": "+265",
        "Malaysia": "+60",
        "Maldives": "+960",
        "Mali": "+223",
        "Malta": "+356",
        "Marshall Islands": "+692",
        "Martinique": "+596",
        "Mauritania": "+222",
        "Mauritius": "+230",
        "Mayotte": "+262",
        "Mexico": "+52",
        "Micronesia, Federated States of Micronesia": "+691",
        "Moldova": "+373",
        "Monaco": "+377",
        "Mongolia": "+976",
        "Montenegro": "+382",
        "Montserrat": "+1664",
        "Morocco": "+212",
        "Mozambique": "+258",
        "Myanmar": "+95",
        "Namibia": "+264",
        "Nauru": "+674",
        "Nepal": "+977",
        "Netherlands": "+31",
        "Netherlands Antilles": "+599",
        "New Caledonia": "+687",
        "New Zealand": "+64",
        "Nicaragua": "+505",
        "Niger": "+227",
        "Nigeria": "+234",
        "Niue": "+683",
        "Norfolk Island": "+672",
        "Northern Mariana Islands": "+1670",
        "Norway": "+47",
        "Oman": "+968",
        "Pakistan": "+92",
        "Palau": "+680",
        "Palestinian Territory, Occupied": "+970",
        "Panama": "+507",
        "Papua New Guinea": "+675",
        "Paraguay": "+595",
        "Peru": "+51",
        "Philippines": "+63",
        "Pitcairn": "+872",
        "Poland": "+48",
        "Portugal": "+351",
        "Puerto Rico": "+1939",
        "Qatar": "+974",
        "Romania": "+40",
        "Russia": "+7",
        "Rwanda": "+250",
        "Reunion": "+262",
        "Saint Barthelemy": "+590",
        "Saint Helena, Ascension and Tristan Da Cunha": "+290",
        "Saint Kitts and Nevis": "+1869",
        "Saint Lucia": "+1758",
        "Saint Martin": "+590",
        "Saint Pierre and Miquelon": "+508",
        "Saint Vincent and the Grenadines": "+1784",
        "Samoa": "+685",
        "San Marino": "+378",
        "Sao Tome and Principe": "+239",
        "Saudi Arabia": "+966",
        "Senegal": "+221",
        "Serbia": "+381",
        "Seychelles": "+248",
        "Sierra Leone": "+232",
        "Singapore": "+65",
        "Slovakia": "+421",
        "Slovenia": "+386",
        "Solomon Islands": "+677",
        "Somalia": "+252",
        "South Africa": "+27",
        "South Sudan": "+211",
        "South Georgia and the South Sandwich Islands": "+500",
        "Spain": "+34",
        "Sri Lanka": "+94",
        "Sudan": "+249",
        "Svalbard and Jan Mayen": "+47",
        "Swaziland": "+268",
        "Sweden": "+46",
        "Switzerland": "+41",
        "Syrian Arab Republic": "+963",
        "Taiwan": "+886",
        "Tajikistan": "+992",
        "Tanzania, United Republic of Tanzania": "+255",
        "Thailand": "+66",
        "Timor-Leste": "+670",
        "Togo": "+228",
        "Tokelau": "+690",
        "Tonga": "+676",
        "Trinidad and Tobago": "+1868",
        "Tunisia": "+216",
        "Turkey": "+90",
        "Turkmenistan": "+993",
        "Turks and Caicos Islands": "+1649",
        "Tuvalu": "+688",
        "Uganda": "+256",
        "Ukraine": "+380",
        "United Arab Emirates": "+971",
        "United Kingdom": "+44",
        "United States": "+1",
        "Uruguay": "+598",
        "Uzbekistan": "+998",
        "Vanuatu": "+678",
        "Venezuela, Bolivarian Republic of Venezuela": "+58",
        "Vietnam": "+84",
        "Virgin Islands, British": "+1284",
        "Virgin Islands, U.S.": "+1340",
        "Wallis and Futuna": "+681",
        "Yemen": "+967",
        "Zambia": "+260",
        "Zimbabwe": "+263",
    }

    draw_wolf(output_text)

    output_text.insert(tk.END, "Starting...\n")
    output_text.see(tk.END)  # Scroll to the end of the text widget
    output_text.update()  # Update the display
    time.sleep(2)

    # Add phone numbers to leads
    add_phone_numbers(leads, country_codes, oprator_codes, output_text)

    # Export leads with phone numbers to Excel
    export_to_csv(leads)


def browse_file(output_text):
    filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if filename:
        process_leads(filename, output_text)


def main():
    root = tk.Tk()
    root.title("DiiiiiiiB Dicreption - MAK")
    root.geometry("800x900")  # Set window size

    # Configure styles
    bg_color = "#000000"  # Background color
    fg_color = "#00FF00"  # Foreground color (text color)
    btn_color = "#FF0000"  # Button color
    lbl_font = ("Courier", 14)  # Label font

    root.configure(bg=bg_color)

    frame = tk.Frame(root, bg=bg_color)
    frame.pack(padx=10, pady=10)

    label = tk.Label(
        frame,
        text="DiiiiiiiB Dicreption",
        fg=fg_color,
        bg=bg_color,
        font=("Courier", 20, "bold"),
    )
    label.pack(pady=10)

    output_text = tk.Text(
        frame,
        width=80,
        height=40,
        bg=bg_color,
        fg=fg_color,
        font=("Courier", 12),
        wrap=tk.WORD,
    )
    output_text.pack(pady=10)

    browse_button = tk.Button(
        frame,
        text="Browse",
        command=lambda: browse_file(output_text),
        bg=btn_color,
        fg=fg_color,
    )
    browse_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()


if __name__ == "__main__":
    main()
