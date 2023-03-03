import torch

class Hitung:
    perhitungan = 12
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.per = Hitung.perhitungan
        
    def hasil(self):
        """
            input2 x alpha + input1 
        """
        self.mt_a = torch.randint(self.a, self.b, (5,))
        self.mt_b = torch.randint(self.a, self.b, (5,))
        self.hasil = torch.add(self.mt_a, self.mt_b)

        return self.mt_a, self.mt_b, self.hasil
    
    def __str__(self):
        mt_a, mt_b, mt_hasil = self.hasil()
        return f"Matrix A adalah mt_a {mt_a}\n\
                 Matrix B adalah mt_b {mt_b}\n\
                 Hasil Matirx adalah {mt_hasil}"
    
hasil = Hitung(5, 10)
print(hasil)