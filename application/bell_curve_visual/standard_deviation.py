import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

def create_bell_curve_figure():
    mu = 0
    sigma = 1
    x = np.linspace(-4, 4, 400)
    y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(x, y, label='Normal Distribution')
    ax.axvline(mu, color='black', linestyle='--', label='Mean (μ)')
    ax.annotate('Mean (μ)', xy=(mu, max(y)), xytext=(mu+0.5, max(y)*0.9),
                arrowprops=dict(facecolor='black', arrowstyle='->'))
    ax.annotate('Standard Deviation (σ)', xy=(mu+1, max(y)/2), xytext=(mu+2, max(y)/1.5),
                arrowprops=dict(facecolor='blue', arrowstyle='<->'))
    ax.set_title('Bell Curve - Standard Deviation')
    ax.legend()
    return fig

def main():
    root = tk.Tk()
    root.title("Standard Deviation Visualization")
    root.attributes('-fullscreen', True)
    root.bind('<Escape>', lambda e: root.destroy())

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    text = (
        "📊 Standard Deviation\n\n"
        "Standard deviation measures how spread out values are from the mean.\n"
        "- Low σ: values are close to the mean\n"
        "- High σ: values are spread out\n\n"
        "Formula:\nσ = √(Σ(xᵢ - μ)² / N)\n\n"
        "Example:\nScores close together (88, 89, 90) = Low σ\nScores spread apart (60, 75, 90) = High σ"
    )
    label = ttk.Label(frame, text=text, font=('Helvetica', 14), justify='left', wraplength=600)
    label.pack(side=tk.LEFT, padx=20, pady=20)

    fig = create_bell_curve_figure()
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
