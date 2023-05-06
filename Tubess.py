from tkinter import *
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox

# Definisikan fungsi untuk mencari kata dalam kamus
def binary_search(kata, kamus, mode):
    if mode == "indonesia":
        indeks_kata = 0
        indeks_arti = 1
    elif mode == "inggris":
        indeks_kata = 0
        indeks_arti = 1  
    else:
        return "Mode terjemahan tidak dikenal"
    
    awal = 0
    akhir = len(kamus) - 1
    while awal <= akhir:
        tengah = (awal + akhir) // 2
        if kamus[tengah][indeks_kata] == kata:
            return kamus[tengah][indeks_arti]
        elif kamus[tengah][indeks_kata] < kata:
            awal = tengah + 1
        else:
            akhir = tengah - 1
    return "Kata tidak ditemukan dalam kamus"

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "kelompok3" and password == "tiga":
        messagebox.showinfo("Login Success", "Welcome, {}".format(username))
        #lakukan tindakan setelah login sukses, misalnya menampilkan tampilan utama aplikasi
        window.destroy()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        
# Definisikan kamus bahasa Indonesia-Inggris
kamus_indo = [
    ("Aba-aba", "command"),
("Abadi", "eternal"),
("Abjad", "alphabet"),
("Abu", "ash"),
("Acara", "event"),
("Adil", "fair"),
("Adik", "younger sibling"),
("Agama", "religion"),
("Air", "water"),
("Alam", "nature"),
("Alat", "tool"),
("Aliran", "flow"),
("Ambil", "take"),
("Aman", "safe"),
("Anak", "child"),
("Angin", "wind"),
("Anjing", "dog"),
("Antara", "between"),
("Anting", "earring"),
("Api", "fire"),
("Apotek", "pharmacy"),
("Arang", "charcoal"),
("Asam", "sour"),
("Asap", "smoke"),
("Asli", "original"),
("Aspal", " asphalt"),
("Atas", "above"),
("Aturan", "rule"),
("Ayam", "chicken"),
("Ayunan",  "swing"),
("Azan", "call to prayer"),
("Baca", "read"),
("Badan", "body"),
("Bagian", "part"),
("Bahagia", "happy"),
("Bahasa", "language"),
("Baju", "clothes"),
("Bakar",  "burn"),
("Balap", "race"),
("Balik", "return"),
("Bambu", "bamboo"),
("Bangga", "proud"),
("Banjir", "flood"),
("Bank", "bank"),
("Banyak", "many",),
("Barat", "west"),
("Barang", "goods"),
("Baterai", "battery"),
("Batu", "stone"),
]

# Definisikan kamus bahasa Inggris-Indonesia
kamus_inggris = [
    ("above", "diatas"),
("administration", "administrasi"),
("alphabet", "abjad"),
("ash", "abu"),
("asphalt", "aspal"),
("bamboo", " bambu"),
("bank", " bank"),
("battery", "baterai"),
("between", "diantara"),
("body", "badan"),
("burn", "bakar"),
("call to prayer", "azan"),
("charcoal", "arang"),
("chicken", "ayam"),
("child", "anak"),
("clothes", "baju"),
("command", "aba-aba"),
("dog", "anjing"),
("earring", "anting"),
("eternal", "abadi"),
("event", "acara"),
("fair", "adil"),
("fire", " api"),
("flood", "banjir"),
("flow", "aliran "),
("goods", "barang"),
("happy ", "bahagia"),
("language", "bahasa"),
("many", "banyak"),
("nature", "alam"),
("original", "asli"),
("part", "bagian"),
("pharmacy", "apotek"),
("proud", "bangga"),
("race", "balap"),
("read", "baca"),
("religion", "agama"),
("return", "balik"),
("rule", "aturan"),
("safe", "aman"),
("smoke", "asap"),
("sour", "asam"),
("stone", "batu"),
("swing", "ayunan"),
("take", "ambil"),
("tool", "alat"),
("water", "air"),
("west", "barat"),
("wind", "angin"),
("younger sibling", "adik"),
]

# Membuat fungsi untuk menampilkan hasil pencarian
def cari_kata():
    kata = input_kata.get()
    mode = input_mode.get()
    if mode == "indonesia":
        kamus = kamus_indo
    elif mode == "inggris":
        kamus = kamus_inggris
    else:
        label_hasil.config(text="Mode terjemahan tidak dikenal")
        return
    arti = binary_search(kata, kamus, mode)
    label_hasil.config(text=arti)

window = Tk()
window.geometry("800x600")

# Membaca gambar
img1 = PhotoImage(file="C:\\Users\\ASUS\\ansel\\login.png")

# Mengatur ukuran gambar sesuai dengan ukuran jendela utama
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
img1 = img1.subsample(img1.width() // width, img1.height() // height)

# Membuat objek Label dan mengatur background dengan gambar
bg_label1 = Label(window, image=img1)
bg_label1.place(x=0, y=0, relwidth=1, relheight=1)

Brok = Font(family="Algerian", size=16)
Boli = Font(family="MV Boli", size=13)

#label untuk username
label_username = Label(window, text="Username", font=Brok)
label_username.pack()
label_username.place(relx=0.478, rely=0.36)

#entry untuk username
entry_username = Entry(window, fg="red", font=Boli)
entry_username.pack()
entry_username.place(relwidth=0.09, relheight=0.05, relx=0.470, rely=0.40)

#label untuk password
label_password = Label(window, text="Password", font=Brok)
label_password.pack()
label_password.place(relx=0.478, rely=0.46)

#entry untuk password
entry_password = Entry(window, show="*", fg="RED", font=Boli)
entry_password.pack()
entry_password.place(relwidth=0.09, relheight=0.05, relx=0.470, rely=0.50)

#tombol login
button_login = Button(window, text="Login",bg="yellow", command=login)
button_login.pack()
button_login.place(relwidth=0.04, relheight=0.05, relx=0.495, rely=0.57)

window.mainloop()

root = Tk()
root.geometry("800x600")

# Membaca gambar
img = PhotoImage(file="C:\\Users\\ASUS\\ansel\\background.png")

# Mengatur ukuran gambar sesuai dengan ukuran jendela utama
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
img = img.subsample(img.width() // width, img.height() // height)


# Membuat objek Label dan mengatur background dengan gambar
bg_label = Label(root, image=img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Variabel Jenis Font
Tnr2 = Font(family="Gloucester MT Extra Condensed", size=20)
Tnr = Font(family="Times New Roman", size=12)
STC = Font(family="STXingkai", size=15)
MV = Font(family="MV Boli", size=10)

# Tambahkan label untuk mode terjemahan
label_mode2 = Label(root, text= "''Selamat datang di penerjemah kami, silakan masukkan mode bahasa yang anda inginkan dan kata yang anda cari''",fg="black", font=Tnr2)
label_mode2.place(relx=0.2, rely=0.4)

# Tambahkan label untuk mode terjemahan
label_mode = Label(root, text="Mode terjemahan  :", fg="white", bg="black", font=Tnr)
label_mode.place(relwidth=0.09, relheight=0.05, relx=0.35, rely=0.5)

# Tambahkan input teks untuk mode terjemahan
input_mode = Entry(root, font=MV)
input_mode.place(relwidth=0.15, relheight=0.05, relx=0.46, rely=0.5)

# Tambahkan label untuk kata yang akan dicari
label_kata = Label(root, text="Kata :", fg="white", bg="black", font=Tnr)
label_kata.place(relwidth=0.09, relheight=0.05, relx=0.35, rely=0.59)

#Tambahkan input teks untuk kata yang akan dicari
input_kata = Entry(root, font=MV)
input_kata.place(relwidth=0.15, relheight=0.05, relx=0.46, rely=0.59)

#Tambahkan button untuk mencari kata
button_cari = Button(root, text="Cari", fg="black", bg="yellow",font=STC, command=cari_kata)
button_cari.place(relwidth=0.07, relheight=0.05, relx=0.42, rely=0.68)

# Tambahkan label untuk kata yang akan dicari
label_kata = Label(root, text="Hasil Terjemahan :", fg="white", bg="black", font=Tnr)
label_kata.place(relwidth=0.09, relheight=0.05, relx=0.35, rely=0.75)

#Tambahkan label untuk hasil pencarian
label_hasil = Label(root, text="", fg="yellow", bg="green", font=MV)
label_hasil.place(relwidth=0.15, relheight=0.05, relx=0.46, rely=0.75,  bordermode=OUTSIDE)

#Jalankan main loop
root.mainloop()