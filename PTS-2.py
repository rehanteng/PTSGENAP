import random # Mengimpor modul random 

def sapa_acak(): # Mendefinisikan fungsi sapa_acak
    sapaan = ["Assalamualaikum", "Halo", "Selamat pagi"] # Daftar sapaan
    nama = ["teman-teman", "kawan", "rekan-rekan", "sobat"] # Daftar nama

    pilihan_sapaan = random.choice(sapaan) # Memilih satu sapaan 
    pilihan_nama = random.choice(nama) # Memilih satu nama 

    pesan = f"{pilihan_sapaan}, {pilihan_nama}! Semangat belajar Python!"  # Membentuk pesan sapaan
    return pesan  # Mengembalikan pesan 

print(sapa_acak()) # Memanggil fungsi dan mencetak hasilnya

#bagian b
#import random
  # Mengimpor modul random untuk memilih elemen secara acak dari daftar.

# def sapa_acak():
 # Mendefinisikan fungsi bernama sapa_acak yang akan mengembalikan sapaan acak.

# sapaan = ["Assalamualaikum", "Halo", "Selamat pagi"]
# Membuat daftar sapaan yang berisi beberapa pilihan sapaan.

# nama = ["teman-teman", "kawan", "rekan-rekan", "sobat"]
# Membuat daftar nama yang berisi beberapa pilihan nama panggilan.
# pilihan_sapaan = random.choice(sapaan)
# Memilih secara acak satu elemen dari daftar sapaan.
# pilihan_nama = random.choice(nama)
# Memilih secara acak satu elemen dari daftar nama.
# pesan = f"{pilihan_sapaan}, {pilihan_nama}! Semangat belajar Python!"
# Membentuk string sapaan yang dikombinasikan dengan sapaan dan nama yang dipilih secara acak.
# return pesan
# Mengembalikan pesan sapaan tersebut sebagai output dari fungsi.
# print(sapa_acak())
# Memanggil fungsi sapa_acak() dan mencetak hasilnya ke layar.