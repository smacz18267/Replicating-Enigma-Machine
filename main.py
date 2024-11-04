import tkinter
from tkinter import ttk, messagebox

from keyboard import Keyboard
from plugboard import Plugboard
from Rotor import Rotor
from Reflector import Reflector
from Enigma import Enigma

def encode_message():
    # Get values from Tkinter fields
    rotor_1 = Rotors_Entry_1.get()
    rotor_2 = Rotors_Entry_2.get()
    rotor_3 = Rotors_Entry_3.get()
    
    rotor_start = Rotor_Start_Entry.get()
    rings = (Rings_Entry_1.get(), Rings_Entry_2.get(), Rings_Entry_3.get())
    plugboard_pairs = Plugboard_Entry.get().split()  # Expecting pairs like "AR GK OX"
    reflector_choice = Reflector_Entry.get()  # Get the chosen reflector
    message = Message_Entry.get().upper()  # Input message
    
    # Error checking: If any field is empty, show an error message
    if not all([rotor_1, rotor_2, rotor_3, rotor_start, rings[0], rings[1], rings[2], reflector_choice, message]):
        messagebox.showerror("Error", "All fields must be filled in.")
        return

    # Create the rotor objects based on user selection
    rotor_map = {
        "I": Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),  
        "II": Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "V"),
        "III": Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "E"),
        "IV": Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
        "V": Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
    }

    # Reflector options based on user choice
    reflector_map = {
        "A": Reflector("EJMZALYXVBWFCRQUONTSPIKHGD"),
        "B": Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
        "C": Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
    }
    
    reflector = reflector_map[reflector_choice]  # Set the chosen reflector
    
    # Initialize selected rotors
    rotor_1_obj = rotor_map[rotor_1]
    rotor_2_obj = rotor_map[rotor_2]
    rotor_3_obj = rotor_map[rotor_3]

    # Plugboard
    plugboard = Plugboard(plugboard_pairs)
    
    # Keyboard (default, no settings required)
    keyboard = Keyboard()
    
    # Enigma Machine
    enigma_machine = Enigma(reflector, rotor_1_obj, rotor_2_obj, rotor_3_obj, plugboard, keyboard)
    
    # Set ring settings and initial rotor key
    enigma_machine.set_rings(tuple(map(int, rings)))
    enigma_machine.set_key(rotor_start)

    # Encode the message
    cipher_text = ""
    for letter in message:
        cipher_text += enigma_machine.encipher(letter)
    
    # Display encoded message in the output field (read-only)
    Output_Entry.config(state="normal")  # Enable field to insert result
    Output_Entry.delete(0, tkinter.END)
    Output_Entry.insert(0, cipher_text)
    Output_Entry.config(state="readonly")  # Set field back to read-only

# Function to clear all input fields
def clear_fields():
    Rotors_Entry_1.set("")  # Clear rotors
    Rotors_Entry_2.set("")
    Rotors_Entry_3.set("")
    Rotor_Start_Entry.delete(0, tkinter.END)  # Clear rotor start key
    Rings_Entry_1.delete(0, tkinter.END)  # Clear rings
    Rings_Entry_2.delete(0, tkinter.END)
    Rings_Entry_3.delete(0, tkinter.END)
    Plugboard_Entry.delete(0, tkinter.END)  # Clear plugboard settings
    Reflector_Entry.set("")  # Clear reflector choice
    Message_Entry.delete(0, tkinter.END)  # Clear input message
    Output_Entry.config(state="normal")  # Enable output field to clear
    Output_Entry.delete(0, tkinter.END)  # Clear encoded message
    Output_Entry.config(state="readonly")  # Set output field back to read-only

# Initialize GUI
window = tkinter.Tk()
window.title("Enigma Machine Simulator")
frame = tkinter.Frame(window)
frame.pack()

# Input fields
Initial_Settings_Frame = tkinter.LabelFrame(frame, text="Initial Settings")
Initial_Settings_Frame.grid(row=0, column=0, padx=10, pady=10)

# Rotors label and comboboxes
Rotors_Label = tkinter.Label(Initial_Settings_Frame, text="Any 3 Rotors:")
Rotors_Label.grid(row=0, column=0, padx=5, pady=5)

Rotors_Entry_1 = ttk.Combobox(Initial_Settings_Frame, values=["I", "II", "III", "IV", "V"], state="readonly", width=2)
Rotors_Entry_1.grid(row=0, column=1, padx=5, pady=5)

Rotors_Entry_2 = ttk.Combobox(Initial_Settings_Frame, values=["I", "II", "III", "IV", "V"], state="readonly", width=2)
Rotors_Entry_2.grid(row=0, column=2, padx=5, pady=5)

Rotors_Entry_3 = ttk.Combobox(Initial_Settings_Frame, values=["I", "II", "III", "IV", "V"], state="readonly", width=2)
Rotors_Entry_3.grid(row=0, column=3, padx=5, pady=5)

# Rotor Start Label and Entry
Rotor_Start_Label = tkinter.Label(Initial_Settings_Frame, text="Rotor Start (Key):")
Rotor_Start_Label.grid(row=1, column=0, padx=5, pady=5)

Rotor_Start_Entry = tkinter.Entry(Initial_Settings_Frame)
Rotor_Start_Entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

# Rings Label and Entry
Rings_Label = tkinter.Label(Initial_Settings_Frame, text="Rings:")
Rings_Label.grid(row=2, column=0, padx=5, pady=5)

Rings_Entry_1 = tkinter.Spinbox(Initial_Settings_Frame, from_=1, to=26, state="readonly", width=2)
Rings_Entry_1.grid(row=2, column=1, padx=5, pady=5)

Rings_Entry_2 = tkinter.Spinbox(Initial_Settings_Frame, from_=1, to=26, state="readonly", width=2)
Rings_Entry_2.grid(row=2, column=2, padx=5, pady=5)

Rings_Entry_3 = tkinter.Spinbox(Initial_Settings_Frame, from_=1, to=26, state="readonly", width=2)
Rings_Entry_3.grid(row=2, column=3, padx=5, pady=5)

# Plugboard Label and Entry
Plugboard_Label = tkinter.Label(Initial_Settings_Frame, text="Plugboard:")
Plugboard_Label.grid(row=3, column=0, padx=5, pady=5)

Plugboard_Entry = tkinter.Entry(Initial_Settings_Frame)
Plugboard_Entry.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

# Reflector Label and Combobox
Reflector_Label = tkinter.Label(Initial_Settings_Frame, text="Reflector:")
Reflector_Label.grid(row=4, column=0, padx=5, pady=5)

Reflector_Entry = ttk.Combobox(Initial_Settings_Frame, values=["A", "B", "C"], state="readonly", width=3)
Reflector_Entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

Clear_Button = tkinter.Button(Initial_Settings_Frame, text="Clear", command=clear_fields)
Clear_Button.grid(row=5, column=1, padx=5, pady=5)

# Output Frame
Output_Frame = tkinter.LabelFrame(frame, text="Output Message")
Output_Frame.grid(row=5, column=0, padx=10, pady=10)

Message_Label = tkinter.Label(Output_Frame, text="Type your message here:")
Message_Label.grid(row=1, column=0, padx=5, pady=5)
Message_Entry = tkinter.Entry(Output_Frame)
Message_Entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

Output_Label = tkinter.Label(Output_Frame, text="Encoded Message:")
Output_Label.grid(row=4, column=0, padx=5, pady=5)
Output_Entry = tkinter.Entry(Output_Frame, state="readonly")
Output_Entry.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

# Encode Button
Encode_Button = tkinter.Button(frame, text="Encode", command=encode_message)
Encode_Button.grid(row=6, column=0, pady=10)

# Run the application
window.mainloop()


