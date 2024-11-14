from pynput.keyboard import Listener, Key
from colorama import Fore, Style
import pyfiglet



# Target phrases to be detected
TARGET_PHRASES = "hack passwords"

# buffer to store keystrokes
buffer = ""


def logo_banner():
    """Print logo and project details"""
    Author = "C9b3rD3vi1"
    project_name = "Phrase Detection Tool"
    version = "v1.0.0"
    github_link = "https://github.com/C9b3rD3vi1/Keyphrase_Detection_Tool.git"

    print(Style.BRIGHT + pyfiglet.figlet_format({project_name}) + Style.RESET_ALL)
    print(f"Version: {version}")
    print(f"Author: {Author}")
    print(f"GitHub: {github_link}")
    print("Press Ctrl+C to stop the program.")


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
            # Quit and abort the process if ESCAPE is pressed
        elif key.esc:
            print("Exiting...")
            return False
        
    
    # Check if the buffer contains the target phrase
    if TARGET_PHRASES in buffer:
        print(Fore.RED + "Phrase '{TARGET_PHRASES}' detected!!!" + Fore.RESET)
        buffer = ""  # Reset buffer for next detection

    else: # No Phrase detected
        print(Fore.GREEN +'No Phrase was detected!!!'+ Fore.RESET)


    # Keep buffer to a manageable size
    if len(buffer) > len(TARGET_PHRASES) * 2:
        buffer = buffer[-len(TARGET_PHRASES):]


def on_release(key):
    # stop scrpt if ESCAPE is pressed
    if key == Key.esc:
        print("Exiting...")
        return False

    
# main function   
if __name__:
    with Listener(on_press=get_keyboard_press_phrase, on_release=on_release) as listener:
        listener.join()