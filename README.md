Enigma Machine Simulator

This application simulates the historical Enigma machine, originally developed for secure communication during World War II. 
The desktop application is designed using Python and tkinter, enabling users to encode and decode messages. This README provides 
details on installation, usage, and specific input requirements for the rotor and plugboard settings.

------------------------------------------------------------------------------------------------------------
Features:
1. Rotor Encoding: Five rotors are available, each with configurable starting positions.
2. Connections: Allows custom plugboard, rings, and reflector settings for additional encoding complexity.
3. GUI: A user-friendly interface built with tkinter for encoding and decoding messages in real time.

Installation:
1. Install Python: Ensure you have Python 3.7 or higher installed.
2. Install tkinter: tkinter is generally included with Python by default, but if not, you can install it based on your system (e.g., sudo apt-get install python3-tk on Ubuntu).
3. Clone or Download the Project:
     - git clone https://github.com/username/enigma-simulator.git
     - cd enigma-simulator
4. Run the Application: python main.py

Usage:
1. Start the Program: Run main.py to open the GUI interface.
2. Configure settings:
    - Choose any 3 rotors from the drop down list
    - Enter the rotor starting positions in the designated field (must be exactly 3 letters).
    - Select any 3 rings (the numbers correspond to alphabetical letters such as 1 is A, 2 is B etc.)
    - Define plugboard connections in the format "AB CD EF", where each pair represents a switch of letters.
    - Choose a Reflector from the 3 possible options
3. Encode a Message:
   - Type the message you want to encode into the message box.
   - Press "Encode" to view the encoded message.
4. Decode a Message: 
    - To decode, set the rotors and plugboard to the exact same configuration used for encoding. 
    - Type the encoded message into the message box and press "Encode" to decode it back to the original text.

------------------------------------------------------------------------------------------------------------

Acknowledgments:
This project was inspired by the historical Enigma machine and its impact on cryptography.
Special thanks to cryptography experts for insights into Enigma's mechanics.
