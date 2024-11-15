# Keyphrase_Detection_Tool

Python script for a Keyphrase Detection Tool that uses the pynput library to monitor keyboard input in real time and detect specific key phrases. When the specified phrase is detected, the tool will log the event or trigger an alert.

    Just an Advanced Keylogger tool

 ![Runing code](/runing_code.png)

 ![code](/code.png)

## Usage

clone this repository

    https://github.com/C9b3rD3vi1/Keyphrase_Detection_Tool.git

## Running

### Running with default keyphrase detection

    python passphrase.py

### Running with custom keyphrase detection

    python passphrase.py -k confidential secret "data breach"

### Running with logging enabled

    python passphrase.py -l keyword_log.txt

### Running with logging enabled and custom keyphrase detection

    python passphrase.py -k sensitive admin login -l keyword_log.txt
