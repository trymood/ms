from scipy.fft import fft, fftfreq
import numpy as np
from tkinter import Tk, ttk
import tkinter as tk
import matplotlib.pyplot as plt
import math
from cryptography.fernet import Fernet

# nr puncte
N = 1000
# spatiere puncte
T = 1.0 / 800.0
x = np.linspace(0.0, N * T, N, endpoint=False)

# defineste fig
fig = None

# Generare cheie și inițializare Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

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
        encrypted_funct = funct_var.get()

        # Decriptare funcție
        try:
            decrypted_funct = cipher_suite.decrypt(encrypted_funct.encode()).decode()
        except Exception as e:
            print(f"Eroare la decriptare: {e}")
            return

        # Evaluează funcția
        y = evaluate_function(decrypted_funct, x)
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

# Fereastra cu ecuația transformatei Fourier
def show_fourier_equation():
    eq_window = tk.Toplevel(root)
    eq_window.title("Ecuația Transformatei Fourier")
    eq_label = tk.Label(
        eq_window,
        text=(
            "Transformata Fourier a unei funcții f(x) este definită ca:\n"
            "\n"
            "    F(w) = ∫ f(x) * e^(-i * w * x) dx\n"
            "\n"
            "Unde:\n"
            "- w este frecvența unghiulară (în rad/s).\n"
            "- i este unitatea imaginară.\n"
            "- f(x) este semnalul în timp.\n"
        ),
        font=("Arial", 12),
        justify="left",
        padx=10,
        pady=10,
    )
    eq_label.pack()

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
label_entry = ttk.Label(frm, text="Introdu funcția f(x) criptată:")
label_entry.grid(row=0, column=0, padx=5, pady=5)

funct_entry = ttk.Entry(frm, textvariable=funct_var, font=('calibre', 10, 'normal'))
funct_entry.grid(row=0, column=1, padx=5, pady=5)

# Checkbox pentru Fourier
fourier_check = ttk.Checkbutton(frm, text="Aplica Transformarea Fourier", variable=fourier_var)
fourier_check.grid(row=1, column=0, columnspan=2, pady=5)

# Butoane
play_button = ttk.Button(frm, text="Play", command=show_plot)
play_button.grid(row=2, column=0, padx=5, pady=5)

fourier_eq_button = ttk.Button(frm, text="Afișează Ecuația Transformatei", command=show_fourier_equation)
fourier_eq_button.grid(row=2, column=1, padx=5, pady=5)

quit_entry = ttk.Button(frm, text="Quit", command=quit_application)
quit_entry.grid(row=3, column=0, columnspan=2, pady=5)

# Afișare cheie pentru utilizator
key_label = ttk.Label(frm, text=f"Cheie pentru criptare: {key.decode()}")
key_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start GUI
root.mainloop()
