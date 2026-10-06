import pwinput 
from prettytable import PrettyTable 
import time 
 
akun = { 
    "admin": { 
        "username": "admin", 
        "password": "iniadmin404", 
        "role": "admin" 
    }, 
    "editor": { 
        "username": "editor", 
        "password": "inieditor101", 
        "role": "editor" 
    }, 
    "user": { 
        "username": "user", 
        "password": "iniuser707", 
        "role": "user" 
    } 
} 
 
data_spesifikasi = { 
    "AST-01": { 
        "nama": "Karakter Utama", 
        "tipe": "Karakter", 
        "resolusi": "1080p", 
        "status": "Draft Spec", 
    } 
} 
 
 
def login(): 
    while True: 
        print("\n=======================================================") 
        print(" STUDIO ANIMASI & MOTION GRAPHIC - SPECIFICATION SYSTEM") 
        print("\n                    LOGIN SYSTEM ") 
        print("=======================================================") 
        print("1. Admin") 
        print("2. Editor") 
        print("3. User") 
        print("4. Keluar") 
 
        pilihan = input("Pilih: ") 
 
        if pilihan == "4": 
            return "keluar" 
 
        if pilihan == "1": 
            role = "admin" 
        elif pilihan == "2": 
            role = "editor" 
        elif pilihan == "3": 
            role = "user" 
        else: 
            print("Pilihan tidak tersedia!") 
            continue 
 
        print("\n===== LOGIN", role.upper(), "=====") 
        username = input("Username: ") 
        password = pwinput.pwinput("Password: ") 
 
        if username == akun[role]["username"] and password == akun[role]["password"]: 
            print("Login berhasil!") 
            return role 
        else: 
            print("Username atau password salah!") 
 
 
def tambah_data(): 
    while True: 
        print("\n===== TAMBAH SPESIFIKASI ASET =====") 
 
        while True: 
            id_aset = input("ID Aset: ").strip() 
 
            if id_aset == "": 
                print("ID tidak boleh kosong!") 
            elif id_aset in data_spesifikasi: 
                print("ID Aset sudah digunakan!") 
            else: 
                break 
 
        while True: 
            nama = input("Nama Aset: ").strip() 
 
            if nama != "": 
                break 
 
            print("Nama tidak boleh kosong!") 
 
        print("\nTipe Aset") 
        print("1. Karakter") 
        print("2. Background") 
        print("3. Motion Graphic") 
        print("4. VFX") 
 
        while True: 
            pilihan = input("Pilih tipe: ").strip() 
 
            if pilihan == "1": 
                tipe = "Karakter" 
                break 
            elif pilihan == "2": 
                tipe = "Background" 
                break 
            elif pilihan == "3": 
                tipe = "Motion Graphic" 
                break 
            elif pilihan == "4": 
                tipe = "VFX" 
                break 
            else: 
                print("Pilihan tidak tersedia!") 
 
        while True: 
            resolusi = input("Resolusi: ").strip() 
            if resolusi != "": 
                break 
            print("Resolusi tidak boleh kosong!") 
 
        data_spesifikasi[id_aset] = { 
            "nama": nama, 
            "tipe": tipe, 
            "resolusi": resolusi, 
            "status": "Draft Spec", 
        } 
 
        print("Data aset berhasil ditambahkan!") 
        time.sleep(1) 
 
        lagi = input("Tambah aset lagi? (ya/tidak): ").strip() 
        if lagi != "ya": 
            break 
 
 
def tampilkan_data(): 
    print("\n===== DATA SPESIFIKASI ASET =====") 
 
    if len(data_spesifikasi) == 0: 
        print("Belum ada data aset!") 
        return 
 
    tabel = PrettyTable() 
    tabel.field_names = ["ID", "Nama", "Tipe", "Resolusi", "Status"] 
 
    for id_aset, data in data_spesifikasi.items(): 
        tabel.add_row([ 
            id_aset, 
            data["nama"], 
            data["tipe"], 
            data["resolusi"], 
            data["status"], 
        ]) 
 
    print(tabel) 
 
 
def ubah_data(): 
    print("\n===== UBAH DATA ASET =====") 
 
    if len(data_spesifikasi) == 0: 
        print("Belum ada data aset!") 
        return 
 
    tampilkan_data() 
 
    id_aset = input("Masukkan ID Aset: ").strip() 
 
    if id_aset not in data_spesifikasi: 
        print("ID Aset tidak ditemukan!") 
        return 
 
    print("\n1. Ubah Data") 
    print("2. Ubah Status") 
 
    pilihan = input("Pilih: ").strip() 
 
    if pilihan == "1": 
        nama = input("Nama baru: ").strip() 
        resolusi = input("Resolusi baru: ").strip() 
 
        if nama != "": 
            data_spesifikasi[id_aset]["nama"] = nama 
 
        if resolusi != "": 
            data_spesifikasi[id_aset]["resolusi"] = resolusi 
 
        print("Data berhasil diubah!") 
 
    elif pilihan == "2": 
        print("\n1. Draft Spec") 
        print("2. Ready for Modeling/Anim") 
        print("3. In Rendering") 
        print("4. Approved / Final") 
 
        status = input("Pilih status: ").strip() 
 
        if status == "1": 
            data_spesifikasi[id_aset]["status"] = "Draft Spec" 
        elif status == "2": 
            data_spesifikasi[id_aset]["status"] = "Ready for Modeling/Anim" 
        elif status == "3": 
            data_spesifikasi[id_aset]["status"] = "In Rendering" 
        elif status == "4": 
            data_spesifikasi[id_aset]["status"] = "Approved / Final" 
        else: 
            print("Pilihan tidak tersedia!") 
            return 
 
        print("Status berhasil diubah!") 
 
    else: 
        print("Pilihan tidak tersedia!") 
 
 
def hapus_data(): 
    print("\n===== HAPUS DATA ASET =====") 
 
    if len(data_spesifikasi) == 0: 
        print("Belum ada data aset!") 
        return 
 
    tampilkan_data() 
 
    id_aset = input("Masukkan ID Aset: ").strip() 
 
    if id_aset in data_spesifikasi: 
        del data_spesifikasi[id_aset] 
        print("Data berhasil dihapus!") 
    else: 
        print("ID Aset tidak ditemukan!") 
 
 
def menu_admin(): 
    while True: 
        print("\n===== MENU ADMIN =====") 
        print("1. Tambah Aset") 
        print("2. Tampilkan Aset") 
        print("3. Ubah Aset") 
        print("4. Hapus Aset") 
        print("5. Logout") 
 
        pilihan = input("Pilih menu: ") 
 
        if pilihan == "1": 
            tambah_data() 
        elif pilihan == "2": 
            tampilkan_data() 
        elif pilihan == "3": 
            ubah_data() 
        elif pilihan == "4": 
            hapus_data() 
        elif pilihan == "5": 
            break 
        else: 
            print("Pilihan tidak tersedia!") 
 
 
def menu_editor(): 
    while True: 
        print("\n===== MENU EDITOR =====") 
        print("1. Tambah Aset") 
        print("2. Tampilkan Aset") 
        print("3. Ubah Aset") 
        print("4. Logout") 
 
        pilihan = input("Pilih menu: ") 
 
        if pilihan == "1": 
            tambah_data() 
        elif pilihan == "2": 
            tampilkan_data() 
        elif pilihan == "3": 
            ubah_data() 
        elif pilihan == "4": 
            break 
        else: 
            print("Pilihan tidak tersedia!") 
 
 
def menu_user(): 
    while True: 
        print("\n===== MENU USER =====") 
        print("1. Tampilkan Aset") 
        print("2. Logout") 
 
        pilihan = input("Pilih menu: ") 
 
        if pilihan == "1": 
            tampilkan_data() 
        elif pilihan == "2": 
            break 
        else: 
            print("Pilihan tidak tersedia!") 
 
 
while True: 
    role = login() 
 
    if role == "admin": 
        menu_admin() 
    elif role == "editor": 
        menu_editor() 
    elif role == "user": 
        menu_user() 
    elif role == "keluar": 
        print("Program selesai!") 
        break