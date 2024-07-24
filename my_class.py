class Mobil:
    def _init_(self, name, merk, model, tahun):
        self.merk = merk
        self.merk = model
        self.merk = tahun

mobil1 = Mobil('Toyota', 'Corla',2020)
print(mobil1._dict_)
mobil2 = Mobil('Honda', 'Civic',2019)
print(mobil2._dict_)