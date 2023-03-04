import torch

class Hitung:
    perhitungan = 12
    def __init__(self, a=None, b=None, flat1=None, flat2=None):
        self.a = a
        self.b = b
        self.flat1 = flat1
        self.flat2 = flat2
        
    def hasil(self):
        """
            input2 x alpha + input1 
        """
        self.mt_a = torch.randint(self.a, self.b, (5,))
        self.mt_b = torch.randint(self.a, self.b, (5,))
        self.hasil = torch.add(self.mt_a, self.mt_b)

        return self.mt_a, self.mt_b, self.hasil
    
    @property
    def meratakan(self):
        flat1 = torch.tensor(self.flat1).view(1,-1,1)
        flat2 = torch.tensor(self.flat2).view(1,-1,1)

        hasil2 = flat1.squeeze()
        return flat1, flat2, hasil2

    def __str__(self):
        mt_a, mt_b, mt_hasil = self.hasil()
        flat1, flat2, hasil2 = self.meratakan

        # return f"Matrix A adalah mt_a {mt_a}\n\
        #          Matrix B adalah mt_b {mt_b}\n\
        #          Hasil Matirx adalah {mt_hasil}"
        return f"flat1 = {flat1} \n flat2 = {flat2} \n Hasil = {hasil2}"
    
# class Hitung2(Hitung):
#     def __init__(self, a=None):
#         super(Hitung2).__init__()

#         def hitung2(self):
#             a = torch.tensor(self.a)

#             return a

#         def __str__(self):

hasil = Hitung(1, 2, flat1=[[1,2,3], [4,5,6]], flat2=[4, 5, 6])
print(hasil)