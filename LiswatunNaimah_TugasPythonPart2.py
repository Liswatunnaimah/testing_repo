# Perpustakaan Liswatun Naimah
# Ucapan Selamat Datang
def kata_sambutan():
    print("="*150)
    print("Selamat datang di Perpustakaan Liswatun Naimah!")
    print("Kami siap membantu Anda menemukan buku terbaik untuk dibaca.")
    print("Jangan ragu untuk mengeksplor koleksi kami!")
    print("="*150)

daftar_buku_diperpustakaan_Liswatun_Naimah = [
    {"judul": "Mimpi Sejuta Dolar", "penulis": "Merry Riana", "penerbit": "Gramedia", "tahun": 2011, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 9, "status": "available"},
    {"judul": "Kisah Sukses dari Nol", "penulis": "Chairul Tanjung", "penerbit": "Gramedia", "tahun": 2012, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 6, "status": "available"},
    {"judul": "Manusia Setengah Salmon", "penulis": "Raditya Dika", "penerbit": "GagasMedia", "tahun": 2011, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 7, "status": "not available"},
    {"judul": "Hidup Sederhana", "penulis": "Desi Anwar", "penerbit": "Gramedia", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 4, "status": "available"},
    {"judul": "Nanti Kita Cerita Tentang Hari Ini", "penulis": "Marchella FP", "penerbit": "KPG", "tahun": 2018, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 5, "status": "available"},
    {"judul": "You Do You", "penulis": "Fellexandro Ruby", "penerbit": "Bentang Pustaka", "tahun": 2020, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 6, "status": "available"},
    {"judul": "Esok Lebih Baik", "penulis": "Rhenald Kasali", "penerbit": "Bentang Pustaka", "tahun": 2015, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 5, "status": "available"},
    {"judul": "Stop Overthinking", "penulis": "Nick Trenton", "penerbit": "Independently Published", "tahun": 2021, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 4, "status": "not available"},
    {"judul": "Mindset: The New Psychology of Success", "penulis": "Carol Dweck", "penerbit": "Ballantine Books", "tahun": 2006, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 6, "status": "available"},
    {"judul": "Grit", "penulis": "Angela Duckworth", "penerbit": "Scribner", "tahun": 2016, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 7, "status": "available"},
    {"judul": "How To Think Like Sherlock Holmes", "penulis": "Maria Konnikova", "penerbit": "Viking", "tahun": 2013, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "available"},
    {"judul": "Awaken the Giant Within", "penulis": "Tony Robbins", "penerbit": "Free Press", "tahun": 1991, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "available"},
    {"judul": "Outliers", "penulis": "Malcolm Gladwell", "penerbit": "Little, Brown and Company", "tahun": 2008, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 10, "status": "available"},
    {"judul": "Kamu Gak Sendirian", "penulis": "Pidi Baiq", "penerbit": "Pastel Books", "tahun": 2019, "kota penerbitan": "Bandung", "negara penerbitan": "Indonesia", "dipinjam": 9, "status": "not available"},
    {"judul": "Menjadi Manusia Kuat", "penulis": "Yudi Latif", "penerbit": "Kompas", "tahun": 2015, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 8, "status": "not available"},
    {"judul": "Sapiens", "penulis": "Yuval Noah Harari", "penerbit": "Gramedia", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 4, "status": "available"},
    {"judul": "Atomic Habits", "penulis": "James Clear", "penerbit": "Penguin", "tahun": 2018, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 8, "status": "available"},
    {"judul": "Rich Dad Poor Dad", "penulis": "Robert T. Kiyosaki", "penerbit": "Warner Books", "tahun": 1997, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 8, "status": "not available"},
    {"judul": "Think and Grow Rich", "penulis": "Napoleon Hill", "penerbit": "Tribute Books", "tahun": 1937, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 6, "status": "available"},
    {"judul": "Laskar Pelangi", "penulis": "Andrea Hirata", "penerbit": "Bentang Pustaka", "tahun": 2005, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 8, "status": "available"},
    {"judul": "Bumi", "penulis": "Tere Liye", "penerbit": "Gramedia", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 5, "status": "not available"},
    {"judul": "Hujan", "penulis": "Tere Liye", "penerbit": "Gramedia", "tahun": 2016, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 7, "status": "available"},
    {"judul": "Dilan: Dia adalah Dilanku Tahun 1990", "penulis": "Pidi Baiq", "penerbit": "Pastel Books", "tahun": 2014, "kota penerbitan": "Bandung", "negara penerbitan": "Indonesia", "dipinjam": 6, "status": "available"},
    {"judul": "Filosofi Kopi", "penulis": "Dee Lestari", "penerbit": "Bentang Pustaka", "tahun": 2006, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 4, "status": "available"},
    {"judul": "Perahu Kertas", "penulis": "Dee Lestari", "penerbit": "Bentang Pustaka", "tahun": 2009, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 7, "status": "not available"},
    {"judul": "Sabtu Bersama Bapak", "penulis": "Adhitya Mulya", "penerbit": "GagasMedia", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 5, "status": "available"},
    {"judul": "Rindu", "penulis": "Tere Liye", "penerbit": "Republika", "tahun": 2014, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 3, "status": "available"},
    {"judul": "Negeri 5 Menara", "penulis": "A. Fuadi", "penerbit": "Gramedia", "tahun": 2009, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 8, "status": "available"},
    {"judul": "Bidadari-Bidadari Surga", "penulis": "Tere Liye", "penerbit": "Republika", "tahun": 2008, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 6, "status": "not available"},
    {"judul": "Harry Potter and the Philosopher's Stone", "penulis": "J.K. Rowling", "penerbit": "Bloomsbury", "tahun": 1997, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 10, "status": "available"},
    {"judul": "The Lord of the Rings", "penulis": "J.R.R. Tolkien", "penerbit": "Allen & Unwin", "tahun": 1954, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 9, "status": "available"},
    {"judul": "The Catcher in the Rye", "penulis": "J.D. Salinger", "penerbit": "Little, Brown and Company", "tahun": 1951, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 8, "status": "available"},
    {"judul": "Pride and Prejudice", "penulis": "Jane Austen", "penerbit": "T. Egerton", "tahun": 1813, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 7, "status": "available"},
    {"judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "penerbit": "J.B. Lippincott & Co.", "tahun": 1960, "kota penerbitan": "Philadelphia", "negara penerbitan": "USA", "dipinjam": 6, "status": "available"},
    {"judul": "Hujan Bulan Juni", "penulis": "Sapardi Djoko Damono", "penerbit": "Gramedia", "tahun": 1994, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 10, "status": "not available"},
    {"judul": "Surat Kecil untuk Tuhan", "penulis": "Agnes Davonar", "penerbit": "Inandra Published", "tahun": 2008, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 6, "status": "available"},
    {"judul": "Orang-orang Biasa", "penulis": "Andrea Hirata", "penerbit": "Bentang Pustaka", "tahun": 2019, "kota penerbitan": "Yogyakarta", "negara penerbitan": "Indonesia", "dipinjam": 7, "status": "available"},
    {"judul": "Mariposa", "penulis": "Luluk HF", "penerbit": "Coconut Books", "tahun": 2020, "kota penerbitan": "Jakarta", "negara penerbitan": "Indonesia", "dipinjam": 4, "status": "not available"},
    {"judul": "The Da Vinci Code", "penulis": "Dan Brown", "penerbit": "Doubleday", "tahun": 2003, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 4, "status": "available"},
    {"judul": "Angels and Demons", "penulis": "Dan Brown", "penerbit": "Pocket Books", "tahun": 2000, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 10, "status": "not available"},
    {"judul": "Inferno", "penulis": "Dan Brown", "penerbit": "Doubleday", "tahun": 2013, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "not available"},
    {"judul": "Gone Girl", "penulis": "Gillian Flynn", "penerbit": "Crown Publishing", "tahun": 2012, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 3, "status": "available"},
    {"judul": "Twilight", "penulis": "Stephenie Meyer", "penerbit": "Little, Brown and Company", "tahun": 2005, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "not available"},
    {"judul": "The Fault in Our Stars", "penulis": "John Green", "penerbit": "Dutton Books", "tahun": 2012, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 10, "status": "not available"},
    {"judul": "Looking for Alaska", "penulis": "John Green", "penerbit": "Dutton Books", "tahun": 2005, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 5, "status": "available"},
    {"judul": "A Thousand Splendid Suns", "penulis": "Khaled Hosseini", "penerbit": "Riverhead Books", "tahun": 2007, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 10, "status": "not available"},
    {"judul": "Eleanor Oliphant Is Completely Fine", "penulis": "Gail Honeyman", "penerbit": "HarperCollins", "tahun": 2017, "kota penerbitan": "London", "negara penerbitan": "UK", "dipinjam": 7, "status": "available"},
    {"judul": "The Girl on the Train", "penulis": "Paula Hawkins", "penerbit": "Riverhead Books", "tahun": 2015, "kota penerbitan": "New York", "negara penerbitan": "USA", "dipinjam": 3, "status": "available"} 
]

# Menampilkan semua buku yang tersedia
def tampilkan_buku():
    print("\nDaftar Buku di Perpustakaan:")
    for i, buku in enumerate(daftar_buku_diperpustakaan_Liswatun_Naimah):
        print(f"{i + 1}. {buku['judul']} - {buku['penulis']} - {buku['penerbit']} ({buku['tahun']}), {buku['kota penerbitan']}, {buku['negara penerbitan']} - Status: {buku['status']} - Dipinjam {buku['dipinjam']} kali")

    # Menawarkan filter pencarian dengan guard
    while True:
        cari_dengan_filter = input("\nApakah Anda ingin mencari buku dengan filter? (y/n): ").strip().lower()
        if cari_dengan_filter == 'y':
            filter_buku()
            break
        elif cari_dengan_filter == 'n':
            print("Anda memilih untuk tidak mencari dengan filter. \nKembali ke menu utama.")
            break
        else:
            print("Input tidak valid. \nSilakan masukkan 'y' untuk ya atau 'n' untuk tidak.")

# Filter buku berdasarkan kriteria
def filter_buku():
    print("\nPilih filter:")
    print("1. Berdasarkan judul")
    print("2. Berdasarkan penulis")
    print("3. Berdasarkan penerbit")
    print("4. Berdasarkan tahun diterbitkan")
    print("5. Berdasarkan kota penerbitan")
    print("6. Berdasarkan negara penerbitan")
    print("7. Berdasarkan status")
    print("8. Kembali ke menu utama")

    try:
        pilihan = int(input("Masukkan pilihan filter (1-8): "))
        if pilihan == 1:
            judul = input("Masukkan judul buku: ")
            hasil = [buku for buku in daftar_buku_diperpustakaan_Liswatun_Naimah if judul.lower() in buku["judul"].lower()]
        elif pilihan == 2:
            penulis = input("Masukkan nama penulis: ")
            hasil = [buku for buku in daftar_buku_diperpustakaan_Liswatun_Naimah if penulis.lower() in buku["penulis"].lower()]
        elif pilihan == 3:
            penerbit = input("Masukkan nama penerbit: ")
            hasil = [buku for buku in daftar_buku_diperpustakaan_Liswatun_Naimah if penerbit.lower() in buku["penerbit"].lower()]
        elif pilihan == 4:
            try:
                tahun = int(input("Masukkan tahun: "))
                hasil = [buku for buku in daftar_buku_diperpustakaan_Liswatun_Naimah if buku["tahun"] == tahun]
            except ValueError:
                print("Tahun harus berupa angka!")
                return
        elif pilihan == 5:
            kota = input("Masukkan kota penerbitan: ")
            hasil = [buku for buku in daftar_buku_diperpustakaan_Liswatun_Naimah if kota.lower() in buku["kota penerbitan"].lower()]
        elif pilihan == 6:
            negara = input("Masukkan negara penerbitan: ")
            hasil = [buku for buku in daftar_buku_diperpustakaan_Liswatun_Naimah if negara.lower() in buku["negara penerbitan"].lower()]
        elif pilihan == 7:
            status = input("Masukkan status (available/not available): ")
            hasil = [buku for buku in daftar_buku_diperpustakaan_Liswatun_Naimah if buku["status"].lower() == status.lower()]
        elif pilihan == 8:
            print("Kembali ke menu utama.")
            return
        else:
            print("Pilihan tidak valid.")
            return

        if hasil:
            print("\nBuku yang ditemukan:")
            for buku in hasil:
                print(f"- {buku['judul']} - {buku['penulis']} - {buku['penerbit']} ({buku['tahun']}) - Status: {buku['status']} - Dipinjam {buku['dipinjam']} kali")
        else:
            print("Tidak ada buku yang cocok dengan filter.")
    except ValueError:
        print("Masukkan angka yang valid!")

# Menambahkan buku baru
def tambah_buku():
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis buku: ")
    penerbit = input("Masukkan penerbit buku: ")
    tahun = input("Masukkan tahun diterbitkan: ")
    kota_penerbitan = input("Masukkan kota penerbitan buku: ")
    negara_penerbitan = input("Masukkan negara penerbitan buku: ")

    try:
        tahun = int(tahun)  # Pastikan tahun berupa angka
    except ValueError:
        print("Tahun harus berupa angka!")
        return

    buku_baru = {
        "judul": judul,
        "penulis": penulis,
        "penerbit": penerbit,
        "tahun": tahun,
        "kota penerbitan": kota_penerbitan,
        "negara penerbitan": negara_penerbitan,
        "dipinjam": 0,
        "status": "available"
    }

    daftar_buku_diperpustakaan_Liswatun_Naimah.append(buku_baru)
    print(f"Buku '{judul}' berhasil ditambahkan.")

# Menghapus buku
def hapus_buku():
    tampilkan_buku()
    try:
        index = int(input("Pilih nomor buku yang ingin dihapus: ")) - 1
        if 0 <= index < len(daftar_buku_diperpustakaan_Liswatun_Naimah):
            buku_dihapus = daftar_buku_diperpustakaan_Liswatun_Naimah.pop(index)
            print(f"Buku '{buku_dihapus['judul']}' berhasil dihapus.")
        else:
            print("Nomor tidak valid.")
    except ValueError:
        print("Masukkan angka yang valid!")

# Menu utama
def menu():
    kata_sambutan()
    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tampilkan semua buku")
        print("2. Tambah buku baru")
        print("3. Hapus buku")
        print("4. Keluar")
        try:
            pilihan = int(input("Masukkan pilihan Anda (1-4): "))
            if pilihan == 1:
                tampilkan_buku()
            elif pilihan == 2:
                tambah_buku()
            elif pilihan == 3:
                hapus_buku()
            elif pilihan == 4:
                print("Terima kasih telah menggunakan aplikasi perpustakaan Liswatun Naimah.")
                break
            else:
                print("Pilihan tidak valid. Masukkan angka antara 1-4.")
        except ValueError:
            print("Masukkan angka yang valid!")

menu()
