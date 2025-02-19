import random # Mengimpor modul random 

def sapa_acak(): # Mendefinisikan fungsi sapa_acak
    sapaan = ["Assalamualaikum", "Halo", "Selamat pagi"] # Daftar sapaan
    nama = ["teman-teman", "kawan", "rekan-rekan", "sobat"] # Daftar nama

    pilihan_sapaan = random.choice(sapaan) # Memilih satu sapaan 
    pilihan_nama = random.choice(nama) # Memilih satu nama 

    pesan = f"{pilihan_sapaan}, {pilihan_nama}! Semangat belajar Python!"  # Membentuk pesan sapaan
    return pesan  # Mengembalikan pesan 

print(sapa_acak()) # Memanggil fungsi dan mencetak hasilnya
