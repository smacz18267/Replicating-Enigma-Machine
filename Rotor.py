class Rotor:
    
    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notch = notch
        
    def forward_conversion(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
    
    def backward_conversion(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal   
    
    def show(self):
        print(self.left)
        print(self.right)
        print("")
        
    def rotate_positions(self, n = 1, forward_conversion = True):
        for i in range(n):
            if forward_conversion:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]
            else:
                self.left = self.left[25] + self.left[:25]
                self.right = self.right[25] + self.right[:25]
        
    def align_to_letter(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate_positions(n)
        
    def set_ring_setting(self, n):
        self.rotate_positions(n - 1, forward_conversion=False)
        
        n_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch - n) % 26]
        
