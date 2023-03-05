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
    
class Hitung2(Hitung):
    def __init__(self, a=None, b=None, flat1=None, flat2=None, dot=[10, 11, 12], dot_2=None):
        super().__init__(a=None, b=None, flat1=None, flat2=None)
        self.a = a
        self.b = b
        self.flat1 = flat1
        self.flat2 = flat2
        self.dot = dot
        self.dot_2 = dot_2

    @property
    def perkalian(self):
        self.mt_a_2 = torch.tensor(self.dot)
        self.mt_b_2 = torch.tensor(self.dot_2)

        return self.mt_a_2, self.mt_b_2, torch.matmul(self.mt_a_2, self.mt_b_2)
    
    def hasil2(self):
        mt_a, mt_b, hasil = self.perkalian
        return f"Matrix a adalah {mt_a}\nMatrix b adalah {mt_b}\n \
                 Hasilnya adalah {hasil}"
    # def __str__(self):
    #     mt_a, mt_b, hasil = self.perkalian
    #     return f"Matrix a adalah {mt_a}\nMatrix b adalah {mt_b}\n \
    #              Hasilnya adalah {hasil}"

hasil = Hitung2(a=4, b=10, flat1=[[11, 22, 33]], flat2=[[44, 55, 66]], \
                dot=torch.randint(1, 10, (3,)), dot_2=torch.randint(5, 10, (3,)))
print(hasil.hasil2())
# print(hasil)



# try:
#     a = float(input('Masukkan nilai a: '))
#     b = float(input('Masukkan nilai b: '))

#     if b == 0:
#         raise ZeroDivisionError   # membangkitkan eksepsi
    
#     if b == " ":
#         raise ValueError
    

# except ZeroDivisionError as e:
#     print('Kesalahan: nilai b tidak boleh 0')
# except ValueError as e:
#     print("Harus angka atau tidak boleh menggunakan spasi!")
# else:
#    c = a / b
#    print(f"{a} / {b} = {c}")