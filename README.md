# Minpro-2-DDP-Sistem-Spesifikasi-Produksi-Aset-Studio-Animasi-Motion-Graphic

Nama: Nila Amelia Nabilla

NIM: 102

Kelas: C

# DESKRIPSI SINGKAT PROGRAM

Studio Animasi & Motion Graphic – Specification System merupakan program berbasis Python yang digunakan untuk mengelola data spesifikasi aset dalam sebuah studio animasi dan motion graphic.

Program ini memiliki sistem login dengan tiga role, yaitu Admin, Editor, dan User. Setiap role memiliki hak akses yang berbeda. Admin memiliki akses CRUD lengkap, Editor dapat menambah, melihat, dan mengubah data, sedangkan User hanya dapat melihat data aset.

Data spesifikasi aset disimpan menggunakan Dictionary sehingga data dapat dikelola dengan lebih mudah. Program juga menggunakan beberapa Function untuk memisahkan setiap proses agar program lebih terstruktur.

# FLOWCHART DAN PENJELASAN ALURNYA
<img width="1834" height="1492" alt="fix2amin2 drawio" src="https://github.com/user-attachments/assets/d6bef8cb-5e64-4ef2-8768-7be2713dc4d4" />


Flowchart menggambarkan alur Studio Animasi & Motion Graphic – Specification System, mulai dari proses login hingga pengguna keluar dari program.

1. Start
 
  Program dimulai dan menampilkan Login System dengan empat pilihan, yaitu Admin, Editor, User, dan Keluar.

2. Input Pilihan

Pengguna memilih role yang ingin digunakan.

- Jika memilih 4 (Keluar), sistem menampilkan pesan "Pilihan tidak tersedia!" sesuai alur pada flowchart lalu kembali ke      utama.
  
- Jika memilih 1, 2, atau 3, pengguna diarahkan ke proses login sesuai role.

3. Login Admin, Editor, atau User
Pengguna memasukkan username dan password. Sistem melakukan pengecekan apakah data login benar.

- Jika salah, sistem menampilkan pesan "Username atau password salah!" dan pengguna kembali ke input username dan password.

- Jika benar, pengguna masuk ke menu sesuai role.

4. Menu Admin

Admin memiliki akses paling lengkap dengan lima pilihan:

1. Tambah Aset
2. Tampilkan Aset
3. Ubah Aset
4. Hapus Aset
5. Logout

Pada Tambah Aset, admin memasukkan ID, nama, tipe, dan resolusi aset. Setelah berhasil ditambahkan, admin dapat memilih apakah ingin menambahkan aset lagi atau kembali ke menu Admin.

Pada Tampilkan Aset, sistem mengambil data dari dictionary dan menampilkannya dalam bentuk tabel.

Pada Ubah Aset, admin memasukkan ID aset terlebih dahulu. Sistem mengecek apakah ID ditemukan.

- Jika tidak ditemukan, sistem menampilkan "ID Aset tidak ditemukan!".
- Jika ditemukan, admin dapat memilih Ubah Data atau Ubah Status.

Pada Hapus Aset, admin memasukkan ID aset. Jika ID ditemukan, data aset dihapus. Jika tidak ditemukan, sistem menampilkan pesan kesalahan.

Pilihan Logout akan membawa pengguna kembali ke alur menu utama.

5. Menu Editor
Editor memiliki empat pilihan:

1. Tambah Aset
2. Tampilkan Aset
3. Ubah Aset
4. Logout

Alur tambah, tampil, dan ubah aset hampir sama dengan Admin. Perbedaannya adalah Editor tidak memiliki fitur Hapus Aset.

6. Menu User

User hanya memiliki dua pilihan:

1. Tampilkan Aset
2. Logout

User hanya dapat melihat data aset yang tersimpan dan tidak dapat menambah, mengubah, ataupun menghapus data.

7. Kembali ke Menu Utama

Setelah proses pada masing-masing role selesai atau pengguna melakukan logout, alur diarahkan ke bagian "Kembali ke menu utama?".
- Jika Ya, program kembali ke Login System sehingga pengguna dapat login kembali.

- Jika Tidak, program menuju End.

8. End
Program selesai ketika pengguna memilih untuk tidak kembali ke menu utama atau memilih keluar dari sistem.

# KODE PROGRAM

# IMPORT LIBRARY

<img width="514" height="133" alt="image" src="https://github.com/user-attachments/assets/48817b0e-e327-4e51-8951-9749d1768ae9" />

Bagian ini digunakan untuk memanggil library yang dibutuhkan program. pwinput digunakan untuk input password, PrettyTable untuk membuat tampilan data dalam bentuk tabel, sedangkan time digunakan untuk memberikan jeda pada program.

# Dictionary Akun

<img width="550" height="505" alt="image" src="https://github.com/user-attachments/assets/5bf2fe83-a42f-4041-b6ee-217a0ce8cff0" />

Dictionary akun digunakan untuk menyimpan data login setiap role. Program memiliki tiga role, yaitu Admin, Editor, dan User.

# Dictionary Data Aset

<img width="502" height="284" alt="image" src="https://github.com/user-attachments/assets/ca39e1d1-543b-4f95-94b4-02fb69d8f714" />

Dictionary data_spesifikasi digunakan untuk menyimpan data spesifikasi aset. Setiap aset memiliki ID, nama, tipe, resolusi, dan status. ini merupakan aset yang pernah saya tambahkan di minpro 1

# Function login

<img width="911" height="873" alt="image" src="https://github.com/user-attachments/assets/b5ace572-fa1c-4d12-ab0a-d3ac1fc8f8f3" />

Function ini digunakan untuk menangani proses login. Pengguna memilih role kemudian memasukkan username dan password. Sistem akan mengecek data tersebut dan memberikan akses sesuai role jika login berhasil.

# CREATE

<img width="401" height="909" alt="image" src="https://github.com/user-attachments/assets/eda04a8e-b1de-41ce-95fb-1c06395a6b89" />

Function ini digunakan untuk menambahkan aset baru. Program melakukan validasi terhadap ID, nama, tipe, dan resolusi sebelum data dimasukkan ke dictionary.

# READ
<img width="717" height="490" alt="image" src="https://github.com/user-attachments/assets/d619e26b-5ee0-4d0f-85ab-2cb175f9ab73" />

Function ini digunakan untuk mengambil seluruh data aset dari dictionary dan menampilkannya menggunakan PrettyTable.

# UPDATE

<img width="456" height="781" alt="image" src="https://github.com/user-attachments/assets/a95bc7d0-19a8-4d78-8250-686131cb9796" />

Function ini digunakan untuk mengubah data aset. Pengguna dapat mengubah nama dan resolusi atau mengubah status aset.

# DELETE

<img width="447" height="334" alt="image" src="https://github.com/user-attachments/assets/02fcef40-149e-45e5-a4e2-26d67c363b3e" />

Function ini digunakan untuk menghapus data aset berdasarkan ID. Fitur ini hanya dapat digunakan oleh Admin.

# MENU ADMIN
<img width="571" height="572" alt="image" src="https://github.com/user-attachments/assets/4e4c8fe6-7d90-4d47-a37a-7376f1c90f9f" />

Function menu_admin  digunakan untuk menampilkan menu khusus Admin. Menu ini memiliki 5 pilihan:

1. Tambah Aset → menjalankan function tambah_data() untuk menambahkan data aset baru.
2. Tampilkan Aset → menjalankan tampilkan_data() untuk melihat seluruh data aset.
3. Ubah Aset → menjalankan ubah_data() untuk mengubah data atau status aset.
4. Hapus Aset → menjalankan hapus_data() untuk menghapus aset berdasarkan ID.
5. Logout → menggunakan break untuk keluar dari Menu Admin dan kembali ke Login System.

Admin memiliki hak akses CRUD lengkap, yaitu tambah, tampil, ubah, dan hapus data.

# MENU EDITOR
<img width="546" height="503" alt="image" src="https://github.com/user-attachments/assets/24b52825-51cc-4182-98c2-89f81d03b430" />

Function menu_editor digunakan untuk menampilkan menu khusus Editor. Menu ini memiliki 4 pilihan:

1. Tambah Aset → menjalankan tambah_data() untuk menambahkan aset.
2. Tampilkan Aset → menjalankan tampilkan_data() untuk melihat data aset.
3. Ubah Aset → menjalankan ubah_data() untuk mengubah data atau status aset.
4. Logout → menggunakan break untuk keluar dari Menu Editor.

Editor tidak memiliki menu Hapus Aset, sehingga hak aksesnya lebih terbatas dibandingkan Admin.

# MENU USER
<img width="531" height="371" alt="image" src="https://github.com/user-attachments/assets/4d887eb2-315a-4b94-a8dd-a788386dd420" />

Function menu_user digunakan untuk menampilkan menu khusus User. Menu ini hanya memiliki 2 pilihan:

1. Tampilkan Aset → menjalankan tampilkan_data() untuk melihat data aset.
2. Logout → menggunakan break untuk keluar dari Menu User.

User hanya memiliki hak untuk melihat data aset dan tidak dapat menambah, mengubah, atau menghapus data.

# Pengarahan Menu Berdasarkan Role
<img width="460" height="302" alt="image" src="https://github.com/user-attachments/assets/8e892f94-9535-49bc-ac40-1b5c1d416168" />

Bagian ini merupakan alur utama program. Setelah login, sistem akan mengarahkan pengguna ke menu berdasarkan role yang dipilih. Jika pengguna memilih keluar, perulangan dihentikan dan program selesai.

# OUTPUT
# Login System
<img width="544" height="237" alt="image" src="https://github.com/user-attachments/assets/f1f78885-f349-4f8e-a9a9-bc3931a111ba" />

Pada tampilan awal, program menampilkan Login System yang terdiri dari tiga role, yaitu Admin, Editor, dan User. Pengguna juga diberikan pilihan Keluar. Pilihan yang dimasukkan akan menentukan proses selanjutnya sesuai dengan role yang dipilih.

# Login Admin Berhasil
<img width="287" height="285" alt="image" src="https://github.com/user-attachments/assets/018017fc-b742-41d9-8550-ee5f36fec569" />

Setelah memilih Admin, pengguna memasukkan username dan password. Sistem melakukan pengecekan dengan data akun yang tersimpan pada dictionary akun. Jika data benar, sistem menampilkan "Login berhasil!" dan pengguna diarahkan ke Menu Admin.

Admin memiliki hak akses paling lengkap, yaitu dapat menambah, menampilkan, mengubah, dan menghapus data aset.

# Login Gagal
<img width="390" height="111" alt="image" src="https://github.com/user-attachments/assets/0794faa7-4e43-413c-8d82-7ba850f8f955" />

Jika username atau password tidak sesuai dengan data yang tersimpan, sistem menampilkan pesan "Username atau password salah!". Pengguna tidak dapat masuk ke menu dan harus melakukan login kembali.

# Menu Admin
<img width="220" height="163" alt="image" src="https://github.com/user-attachments/assets/676e7e80-fbd6-455b-ae8c-671acd87ff0f" />

Menu Admin menyediakan lima pilihan. Admin mempunyai akses CRUD lengkap terhadap data aset, yaitu Create melalui Tambah Aset, Read melalui Tampilkan Aset, Update melalui Ubah Aset, dan Delete melalui Hapus Aset. Pilihan Logout digunakan untuk keluar dari menu Admin dan kembali ke Login System.

# CREATE
<img width="363" height="479" alt="image" src="https://github.com/user-attachments/assets/05597072-45e8-41e3-b0d1-9d03689968d6" />

Pada proses ini pengguna memasukkan informasi aset berupa ID, nama, tipe, dan resolusi. Setelah semua data valid, data disimpan ke dalam dictionary data_spesifikasi.

Status aset secara otomatis diberikan sebagai "Draft Spec". Program juga memberikan pilihan untuk menambahkan aset lainnya.
# Validasi id Aset
<img width="378" height="70" alt="image" src="https://github.com/user-attachments/assets/52827c3a-4658-46c5-9d92-5572a50cd6d9" />

Program melakukan pengecekan terhadap ID aset sebelum data disimpan. Jika ID sudah terdapat dalam dictionary data_spesifikasi, program menampilkan pesan "ID Aset sudah digunakan!" dan meminta pengguna memasukkan ID lain.

# Validasi Input Kosong
<img width="388" height="79" alt="image" src="https://github.com/user-attachments/assets/b4a344da-dde5-4f88-b576-42d23ee7252e" />

Program tidak mengizinkan ID dan nama aset kosong. Jika pengguna tidak memasukkan data, program menampilkan pesan kesalahan dan meminta input kembali.

Validasi ini membuat data yang disimpan menjadi lebih lengkap.

# READ
<img width="651" height="414" alt="image" src="https://github.com/user-attachments/assets/63fa418d-ffad-4b32-b1d9-83879dba3388" />

Program mengambil seluruh data yang tersimpan dalam dictionary data_spesifikasi, kemudian menampilkannya dalam bentuk tabel.

Tampilan tabel dibuat menggunakan library PrettyTable, sehingga data aset lebih rapi dan mudah dibaca.
# UPDATE
<img width="665" height="322" alt="image" src="https://github.com/user-attachments/assets/03f595cf-f728-42ad-a3db-193b7b64efa1" />

Pengguna terlebih dahulu memasukkan ID aset yang ingin diubah. Program kemudian mengecek apakah ID tersebut terdapat dalam dictionary.

Jika ID ditemukan, pengguna dapat memilih:
- Ubah Data untuk mengubah nama dan resolusi.
- Ubah Status untuk mengubah status aset.

DATA ASET

<img width="339" height="197" alt="image" src="https://github.com/user-attachments/assets/d530d609-0442-49c2-ab19-b1692b4f7a2c" />

STATUS ASET

<img width="339" height="274" alt="image" src="https://github.com/user-attachments/assets/cdcc30e4-22ad-4089-b8c3-f51c462e7b24" />

INI TAMPILAN HASIL DARI UPDATE

<img width="798" height="230" alt="image" src="https://github.com/user-attachments/assets/a37a0755-8427-488a-ad27-6f2a5821317a" />

# id Aset Tidak Ditemukan
<img width="262" height="52" alt="image" src="https://github.com/user-attachments/assets/c0805847-faa2-4bfa-b22a-c6e93a8e924c" />

Sebelum melakukan perubahan atau penghapusan, program mengecek keberadaan ID aset. Jika ID tidak ditemukan dalam dictionary, proses tidak dilanjutkan dan program menampilkan pesan "ID Aset tidak ditemukan!".

Hal ini merupakan bentuk validasi untuk mencegah perubahan atau penghapusan data yang tidak tersedia.

# Delete
<img width="797" height="326" alt="image" src="https://github.com/user-attachments/assets/6bc5b27d-745b-4be0-9f12-fed4db113b5a" />

Fitur Hapus Aset hanya tersedia pada Admin. Admin memasukkan ID aset yang ingin dihapus. Jika ID ditemukan, data akan dihapus dari dictionary menggunakan perintah del.

Setelah berhasil, program menampilkan "Data berhasil dihapus!"

INI TAMPILAN KETIKA DATA DIHAPUS
<img width="798" height="217" alt="image" src="https://github.com/user-attachments/assets/f55189cb-053c-4ed6-b78c-ac630f372d1a" />

# Menu Editor
<img width="566" height="821" alt="image" src="https://github.com/user-attachments/assets/af3cde06-230c-44f5-91df-1949086d4f32" />
<img width="844" height="551" alt="image" src="https://github.com/user-attachments/assets/221de2b8-d4dc-490c-af14-ce729a2fb00e" />
<img width="836" height="603" alt="image" src="https://github.com/user-attachments/assets/be0d1b1b-5573-4f3f-8351-d4905f828b32" />
<img width="836" height="689" alt="image" src="https://github.com/user-attachments/assets/589c76c9-03f0-49b7-9ea9-545a3a4693d7" />
<img width="862" height="246" alt="image" src="https://github.com/user-attachments/assets/ffded166-0351-47f9-93cc-f8b6dca02bba" />

Editor memiliki akses yang lebih terbatas dibandingkan Admin. Editor dapat menambah, menampilkan, dan mengubah aset, tetapi tidak dapat menghapus aset.
# Menu User
<img width="851" height="699" alt="image" src="https://github.com/user-attachments/assets/db55a84f-7e94-47db-95ef-19e0cf75633c" />

User memiliki akses paling terbatas. User hanya dapat melihat data aset melalui menu Tampilkan Aset dan melakukan Logout. User tidak dapat menambah, mengubah, ataupun menghapus data.
# Logout
<img width="636" height="357" alt="image" src="https://github.com/user-attachments/assets/22d363a9-1a0e-4949-a35e-403bab84bb11" />

Ketika pengguna memilih Logout, function menu role akan berhenti dan program kembali ke Login System. Pengguna kemudian dapat login kembali menggunakan role yang diinginkan.
# Keluar Dari Program
<img width="535" height="254" alt="image" src="https://github.com/user-attachments/assets/e231de0e-9451-44b7-a096-647660c7a0f3" />

Jika pengguna memilih pilihan 4 (Keluar) pada Login System, function login mengembalikan nilai "keluar". Program kemudian menjalankan perintah break pada perulangan utama sehingga program berhenti dan menampilkan "Program selesai!".

# PENERAPAN NILAI TAMBAH
Program menerapkan nilai tambah dengan menggunakan 3 library Python, yaitu pwinput, PrettyTable, dan time. Library pwinput digunakan untuk menyembunyikan password saat proses login, PrettyTable digunakan untuk menampilkan data aset dalam bentuk tabel agar lebih rapi, sedangkan time digunakan untuk memberikan jeda setelah data berhasil ditambahkan. Program juga menerapkan validasi input menggunakan conditional statement, seperti pengecekan ID aset agar tidak kosong atau duplikat, pilihan menu, tipe aset, dan status.
