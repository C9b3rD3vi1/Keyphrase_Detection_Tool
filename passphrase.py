from pynput.keyboard import Listener



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
        if key.name ==  " ":
            buffer = buffer[:-1]
        elif key.name == "esc":
            buffer = ""







        # Check if buffer contains target phrases
        if any(phrase in buffer for phrase in TARGET_PHRASES):
            print(f"Target phrase detected: {buffer}")
            buffer = ""