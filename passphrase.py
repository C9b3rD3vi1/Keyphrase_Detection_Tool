
import argparse
from pynput.keyboard import Listener, Key
from colorama import Fore, Style
import pyfiglet
import tkinter as tk
from tkinter import messagebox
from interface import KeystrokeDisplayApp



# Target phrases to be detected
TARGET_PHRASES = "passwords"

# buffer to store keystrokes
buffer = ""

log_file = None
keyword = [] # Will be populated by argparse


# Parse command-line arguments
def parse_arguments():
    global keywords, log_file

    parser = argparse.ArgumentParser(description="Passphrase Detection Tool")
    parser.add_argument(
        "-k", "--keywords",
        nargs="+",
        default=["password", "admin", "alert"],
        help="List of keywords to monitor (space-separated)."
    )
    parser.add_argument(
        "-l", "--log",
        type=str,
        help="Path to the log file for recording detected keywords."
    )
    args = parser.parse_args()
    keywords = args.keywords
    log_file = args.log




def logo_banner():
    """Print logo and project details"""

    Author = "C9b3rD3vi1"
    project_name = pyfiglet.figlet_format("Phrase Detection Tool")
    version = "v1.0.0"
    github_link = "https://github.com/C9b3rD3vi1/Keyphrase_Detection_Tool.git"

    print(Fore.CYAN + project_name + Fore.RESET)
    print("\n")
    print(f"Version: {Fore.LIGHTMAGENTA_EX}{version}{Fore.RESET}")

    print(f"Author: {Fore.LIGHTMAGENTA_EX}{Author}{Fore.RESET}")
    print(f"GitHub: {Fore.BLUE}{github_link}{Style.RESET_ALL}")
    print("\n")



def get_keyboard_press_phrase(key):
    global buffer

    try:
        # Convert key to string
        key_str = str(key.char) if key.char else str(key.scan_code)

        # Append key to buffer
        buffer += key_str
    
    except AttributeError:

        # Handle special keys like backspace and ESCAPE keys  
        # Add blank space to buffer if space is pressed  
        if key.space:
            buffer += " "

            # Remove last character if backspace is pressed
        elif key.backspace:
            buffer = buffer[:-1]

        # Add newline character to buffer if ENTER is pressed
        elif key.enter:
            buffer += "\n"
        
            # Quit and abort the process if ESCAPE is pressed
        elif key.esc:
            print("Exiting...")
            return False
        
    
    # Check if the buffer contains the target phrase
    if TARGET_PHRASES in buffer:
        print(Fore.RED + "Phrase {TARGET_PHRASES} detected!!!" + Fore.RESET)
        buffer = ""  # Reset buffer for next detection

    else: # No Phrase detected
        print(Fore.GREEN +'No Phrase was detected!!!'+ Fore.RESET)


    # Keep buffer to a manageable size
    if len(buffer) > len(TARGET_PHRASES) * 2:
        buffer = buffer[-len(TARGET_PHRASES):]


# Create tkinter root window
#root = tk.Tk()

# Create KeystrokeDisplayApp instance
#app = KeystrokeDisplayApp(root)


# Trigger alert when a keyword is found
def trigger_alert(TARGET_PHRASES):
    print(f"Phrase '{TARGET_PHRASES}' detected!")
    # Show a popup alert
    messagebox.showinfo("Keyword Alert", f"Passphrase Detected: {TARGET_PHRASES}")


# Function to handle key press events
def on_release(key):
    # stop scrpt if ESCAPE is pressed
    if key == Key.esc:
        print("Exiting...")
        return False


    
# main function   
if __name__ == '__main__':
    # Parse command-line arguments
    parse_arguments()

    # log the detection if logging is enabled
    if log_file:
        # Open log file
        with open(log_file, "a") as file:
            file.write(f"Started logging at {datetime.datetime.now()}\n")
            file.write(f" Detected: {phrase} \n")

    # Print logo and project details
    logo_banner()

    # alert
    trigger_alert(TARGET_PHRASES)

    # Start listening for keyboard presses and detecting target phrases
    with Listener(on_press=get_keyboard_press_phrase, on_release=on_release) as listener:
        listener.join()


'''
# Run the tkinter main loop
root.mainloop()
listener.stop()
'''