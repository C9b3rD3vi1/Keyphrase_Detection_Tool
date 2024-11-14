
import tkinter as tk


# Display the keyboard strokes and phrase on a tkinter interface
class KeystrokeDisplayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Phase Detection Tool")
        self.root.geometry("600x400")

        # Set up label to display keystrokes
        self.keystroke_display = tk.StringVar()
        self.keystroke_display.set("Start typing...")
        self.label = tk.Label(self.root, textvariable=self.keystroke_display, font=("Helvetica", 16))
        self.label.pack(pady=20)

    def update_display(self, text):
        """Method to update the label with the current keystrokes."""
        self.keystroke_display.set(text)
