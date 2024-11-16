
import argparse
from pynput.keyboard import Listener, Key
from colorama import Fore, Style
import pyfiglet
import datetime
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
        "-f", "--file",
        type=str,
        help="Path to a file containing keywords to monitor (one per line)."
    )

    parser.add_argument(
        "-l", "--log",
        type=str,
        help="Path to the log file for recording detected keywords."
    )

    args = parser.parse_args()
    keywords = args.keywords
    log_file = args.log

    # Load keywords from arguments
    keywords.extend(args.keywords)


    # Load keywords from file if specified
    if args.file:
        try:
            with open(args.file, "r") as file:
                keywords.extend([line.strip() for line in file if line.strip()])
        except FileNotFoundError:
            print(f"Error: The file '{args.file}' was not found.")
            exit(1)




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
        
        else:
            buffer += f"[{key}]"

     # Check for keywords
    check_for_keywords()

        
    
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


# Function to check for keywords
def check_for_keywords():
    global buffer
    for phrase in keywords:
        if phrase in buffer: # Check for keywords in buffer
            trigger_alert(phrase)




# Trigger alert when a keyword is found
def trigger_alert(phrase):
    print(f"Phrase '{phrase}' detected!")
    # Show a popup alert
    messagebox.showinfo("Keyword Alert", f"Passphrase Detected: {phrase}")


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

    # check for key words
    check_for_keywords()



'''
# Run the tkinter main loop
root.mainloop()
listener.stop()
'''