class Enigma:
    
    def __init__(self, re, r1, r2, r3, pb, kb):
        self.re = re
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.pb = pb
        self.kb = kb
        
    def set_rings(self, rings):
        self.r1.set_ring_setting(rings[0])
        self.r2.set_ring_setting(rings[1])
        self.r3.set_ring_setting(rings[2])
    
    def set_key(self, key):
        self.r1.align_to_letter(key[0])
        self.r2.align_to_letter(key[1])
        self.r3.align_to_letter(key[2])
    
    def encipher(self, letter):
        
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.rotate_positions()
            self.r2.rotate_positions()
            self.r3.rotate_positions()
        elif self.r2.left[0] == self.r2.notch:
            self.r1.rotate_positions()
            self.r2.rotate_positions()
            self.r3.rotate_positions()
        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate_positions()
            self.r3.rotate_positions()
        else:
            self.r3.rotate_positions()
        
        signal = self.kb.forward_conversion(letter)
        signal = self.pb.forward_conversion(signal)
        signal = self.r3.forward_conversion(signal)
        signal = self.r2.forward_conversion(signal)
        signal = self.r1.forward_conversion(signal)
        signal = self.re.reflect(signal)
        signal = self.r1.backward_conversion(signal)
        signal = self.r2.backward_conversion(signal)
        signal = self.r3.backward_conversion(signal)
        signal = self.pb.backward_conversion(signal)
        letter = self.kb.backward_conversion(signal)
        return letter
        
        