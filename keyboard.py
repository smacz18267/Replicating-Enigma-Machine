class Keyboard:
    
    def forward_conversion(self, letter):
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward_conversion(self, signal):
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter
    