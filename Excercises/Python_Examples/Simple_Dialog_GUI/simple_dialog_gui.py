import tkinter as tk

def create_dialog():
    # Create the main window
    root = tk.Tk()
    root.title("Simple Dialog")
    root.geometry("300x150")  # Width x Height

    # Optional: add some text or content
    label = tk.Label(root, text="This is a simple dialog window.")
    label.pack(pady=20)

    # Add a close button at the bottom center
    close_button = tk.Button(root, text="Close", command=root.destroy)
    close_button.pack(side="bottom", pady=10)

    # Start the GUI loop
    root.mainloop()

create_dialog()
