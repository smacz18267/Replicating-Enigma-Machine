class Reflector:
    
    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        
    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        if self.left[signal] == letter:
            return signal
        else:
            return signal
