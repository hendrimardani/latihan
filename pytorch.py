import torch

class Hitung:
    perhitungan = 12
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.per = Hitung.perhitungan
        
    def hasil(self):
        self.mt_a = torch.randint(self.a, self.b, (5,))
        self.mt_b = torch.randint(self.a, self.b, (5,))
        self.hasil = torch.add(self.mt_a, self.mt_b)

        return self.mt_a, self.mt_b, self.hasil
    
    def hasil2(self):
        a = self.hasil()[0]
        return a
    
hasil = Hitung(5, 10)
print(hasil.hasil2())