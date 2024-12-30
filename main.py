from scipy.fft import fft, fftfreq
import numpy as np
from tkinter import Tk, ttk
import tkinter as tk
import matplotlib.pyplot as plt
import math

# nr puncte
N = 1000
# spatiere puncte
T = 1.0 / 800.0
x = np.linspace(0.0, N * T, N, endpoint=False)

# defineste fig
fig = None


# Evaluare funcție
def evaluate_function(funct_str, x):
    try:
        funct_str = funct_str.strip()
        safe_context = {
            "x": None,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "exp": math.exp,
            "log": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
        }
        return np.array([eval(funct_str, {"__builtins__": None}, {**safe_context, "x": val}) for val in x])
    except Exception as e:
        print(f"Ce e asta? {e}")
        return None


# Afișează graficul
def show_plot():
    global fig
    if play_button["text"] == "Play":
        funct = funct_var.get()

        # Evaluează funcția
        y = evaluate_function(funct, x)
        if y is None:
            return

        # Creare grafic
        fig, ax = plt.subplots()

        # Graficul funcției originale
        ax.plot(x, y, 'b-', label="f(x)")

        # Calcul și afișare transformare Fourier, dacă este bifată
        if fourier_var.get():
            yf = fft(y)  # Transformare Fourier
            xf = fftfreq(N, T)[:N // 2]  # Frecvențe pozitive

            # Graficul spectrului
            ax.plot(xf, 2.0 / N * np.abs(yf[:N // 2]), 'r-', label="Fourier Transform |F(w)|")

        ax.set_title('Function and Fourier Transform')
        ax.set_xlabel('x or Frequency')
        ax.set_ylabel('Amplitude')
        ax.legend()
        ax.grid()

        plt.show(block=False)
        play_button["text"] = "Close"
    elif play_button["text"] == "Close":
        plt.close(fig)
        play_button["text"] = "Play"


# Quit application
def quit_application():
    plt.close('all')
    root.destroy()


# GUI
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# Variabile pentru input
funct_var = tk.StringVar()
fourier_var = tk.BooleanVar()

# Input pentru funcție
label_entry = ttk.Label(frm, text="Introdu funcția f(x):")
label_entry.grid(row=0, column=0, padx=5, pady=5)

funct_entry = ttk.Entry(frm, textvariable=funct_var, font=('calibre', 10, 'normal'))
funct_entry.grid(row=0, column=1, padx=5, pady=5)

# Checkbox pentru Fourier
fourier_check = ttk.Checkbutton(frm, text="Aplica Transformarea Fourier", variable=fourier_var)
fourier_check.grid(row=1, column=0, columnspan=2, pady=5)

# Butoane
play_button = ttk.Button(frm, text="Play", command=show_plot)
play_button.grid(row=2, column=0, padx=5, pady=5)

quit_entry = ttk.Button(frm, text="Quit", command=quit_application)
quit_entry.grid(row=2, column=1, padx=5, pady=5)

# Start GUI
root.mainloop()
