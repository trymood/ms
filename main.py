from scipy.fft import fft, fftfreq
import numpy as np
from tkinter import Tk, ttk
import matplotlib.pyplot as plt

# Number of sample points
N = 1000
# Sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

# Perform FFT
yf = fft(y)
xf = fftfreq(N, T)[:N//2]

# Enable interactive mode
plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 1)  # Create two subplots in a single column layout

# Plot time-domain signal
ax1.plot(x, y, 'r-')
ax1.set_title('Time Domain Signal')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Amplitude')

# Plot frequency-domain signal
ax2.plot(xf, 2.0/N * np.abs(yf[0:N//2]), 'b-')
ax2.set_title('Frequency Domain Signal')
ax2.set_xlabel('Frequency [Hz]')
ax2.set_ylabel('Magnitude')

# Add grids to the plots
ax1.grid()
ax2.grid()

# Function to show or close the plot
def show_plot():
    if play_button["text"] == "Play":
        fig.show()  # Show the plot
        play_button["text"] = "Close"
    else:
        play_button["text"] = "Play"
        plt.close(fig)

# Function to clean up and quit the application
def quit_application():
    plt.close(fig)  # Close the plot if it's open
    root.destroy()  # Destroy the root window

# Set up the GUI
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=quit_application).grid(column=1, row=0)

play_button = ttk.Button(frm, text="Play", command=show_plot)
play_button.grid(column=2, row=0)

root.mainloop()
