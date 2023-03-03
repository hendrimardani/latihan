import torch

class Hitung:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hasil(self):
        a = torch.randint(self.a, self.b, (5,))
        b = torch.randint(self.a, self.b, (5,))
        self.hasil = torch.add(a, b)

        return self.hasil, a, b
        

hasil = Hitung(5, 10)
print(hasil.hasil())