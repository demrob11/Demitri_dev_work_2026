# Import the tkinter module for GUI elements
import tkinter as tk

# Define a function that creates the dialog window
def create_dialog():
    # Create the main window object
    root = tk.Tk()

    # Set the window title
    root.title("Simple Dialog")

    # Set the dimensions of the window (Width x Height)
    root.geometry("300x150")

    # Create a label widget with some text to display
    label = tk.Label(root, text="This is a simple dialog window.")

    # Add the label to the window and give it vertical padding
    label.pack(pady=20)

    # Create a button widget labeled "Close" that will close the window when clicked
    close_button = tk.Button(root, text="Close", command=root.destroy)

    # Add the button to the window and position it at the bottom with padding
    close_button.pack(side="bottom", pady=10)

    # Start the GUI event loop (keeps the window open until closed)
    root.mainloop()

# Call the function to display the dialog
create_dialog()
