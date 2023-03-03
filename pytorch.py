import torch

a = torch.randint(0, 10, (5,))
b = torch.randint(0, 5, (5,))
hasil = torch.add(a, b)

print(f"Matrix A = {a}")
print(f"Matrix B = {b}")
print(f"Hasil dari A dan B {hasil}")