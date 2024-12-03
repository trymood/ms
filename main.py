# import numpy as np
# import matplotlib.pyplot  as plt
# import math

# a=[]
# b=[]

# y=0
# x=int(input("X egal cu numarul "))
# pnct=int(input("Numarul de puncte este egal cu "))

# fig, ax = plt.subplots()

# for i in range (pnct):
#     if x > 10:
#         y=x**2-6*x-1
#         x = x + 1
#     else:
#         y = y*2 + 1
#         x = x + 1
#     a.append(x)
#     b.append(y)
#     ax.plot(a, b)
#     plt.pause(0.001)

# # testez chestii

# plt.show()



from scipy.fft import fft, fftfreq
import numpy as np
from tkinter import Tk, Button, ttk
#from tkinter import ttk



# Number of sample points
N = 1000
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = fftfreq(N, T)[:N//2]
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
# plt.show()

def show_plot():
    if play_button["text"] == "Play":
        plt.show()
        play_button["text"] = "Close"
    else:
        play_button["text"] = "Play"
        plt.close()



root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
play_button = ttk.Button(frm, text="Play", command=show_plot)
play_button.grid(column=2, row=0)
root.mainloop()
