from pynput.keyboard import Listener
from colorama import Fore, Style



# Target phrases to be detected
TARGET_PHRASES = "hack passwords"

# buffer to store keystrokes
buffer = ""

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
        print(f'{Fore.RED} Phrase {TARGET_PHRASES} detected!!!')
        buffer = ""  # Reset buffer for next detection

    else: # No Phrase detected
        print(f'{Fore.GREEN} Phrase was detected!!!')