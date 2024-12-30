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
x = np.linspace(0.0, N*T, N, endpoint=False)

# defineste fig ig :3
fig = None

# draga cititorule ce am facut mai jos nu este transformata fourier, doar am realizat graficul unei functii in funcite de o alta functie
# pe care o ia drept parametru, in cazul nostru x e parametru initial, apoi y=f(x) devine parametru pt funcita w=f(y)
# si revin la problema pe care am avut o si la inceput si anume ca nu stiu ce face funcita fourier, am sa revin asupra problemei
# pana atunci xoxo gossip girl :P

# verifica daca e ok transformata dpdv sintactic
def evaluate_function(funct_str, x):
    try:
        # Clean the input string
        funct_str = funct_str.strip()
        safe_context = {
            # aici am descoperit eu ca poti sa schimbi numele unei functii built-in (ce frumos e python)
            # pt ca era naspa sa scrii mereu math.sin cand intruduci in gui functia, asa scrii doar sin, cos etc
            "x": None,  
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "exp": math.exp,
            "log": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        }
        # aici sincer nu pot sa va spun cu exactitate cum functioneaza dar merge asa ca nu am mai umblat 
        return np.array([eval(funct_str, {"__builtins__": None}, {**safe_context, "x": val}) for val in x])
    except SyntaxError:
        print(f"Hopaa: Nu ai scris bine functia '{funct_str}'")
        return None
    except Exception as e:
        print(f"Ce e asta? {e}")
        return None

# verifica daca e ok transformata dpdv sintactic
def evaluate_transformation(transformation_str, y):
    try:
        # sterge input string
        transformation_str = transformation_str.strip()
        safe_context = {
            "y": None,  
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "exp": math.exp,
            "log": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        }
        # ca mai sus, in teorie stiu ce face, dar exact linie cu linie nup :P
        return np.array([eval(transformation_str, {"__builtins__": None}, {**safe_context, "y": val}) for val in y])
    except SyntaxError:
        print(f"Hopaa: Nu ai scris bine functia '{transformation_str}'")
        return None
    except Exception as e:
        print(f"Ce e asta? {e}")
        return None

# functie care show/close plot
def show_plot():
    global fig  # asta nu prea sunt sigur, gen verifica ca fig e globala, daca nu o pui are bugs
    if play_button["text"] == "Play":
        # ia funcita din input
        funct = funct_var.get()
        w_transformation = w_var.get()

        # functia in x
        y = evaluate_function(funct, x)
        if y is None:
            return

        # transformata pe w
        w = evaluate_transformation(w_transformation, y)
        if w is None:
            return

        # face plotul efectiv
        fig, ax = plt.subplots()

        # ploteaza functia
        ax.plot(x, w, 'g-', label="Transformed Function")
        ax.set_title('Function Transformation')
        ax.set_xlabel('x')
        ax.set_ylabel('w')
        ax.legend()
        ax.grid()

        # show plot
        plt.show(block=False)
        play_button["text"] = "Close"
    elif play_button["text"] == "Close":
        plt.close(fig)
        play_button["text"] = "Play"

# functia quitapp
def quit_application():
    plt.close('all')  # asta pt plots
    root.destroy()  # asta pt gui 

# gui
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

# var pt input
funct_var = tk.StringVar()
w_var = tk.StringVar()

# input campuri
label_entry = ttk.Label(frm, text="Introdu funcția f(x):")
label_entry.grid(row=0, column=0, padx=5, pady=5)

funct_entry = ttk.Entry(frm, textvariable=funct_var, font=('calibre', 10, 'normal'))
funct_entry.grid(row=0, column=1, padx=5, pady=5)

label_w = ttk.Label(frm, text="Transformare w=f(y):")
label_w.grid(row=1, column=0, padx=5, pady=5)

w_entry = ttk.Entry(frm, textvariable=w_var, font=('calibre', 10, 'normal'))
w_entry.grid(row=1, column=1, padx=5, pady=5)

# butoane
play_button = ttk.Button(frm, text="Play", command=show_plot)
play_button.grid(row=2, column=0, padx=5, pady=5)

quit_entry = ttk.Button(frm, text="Quit", command=quit_application)
quit_entry.grid(row=2, column=1, padx=5, pady=5)

# gui start
root.mainloop()
