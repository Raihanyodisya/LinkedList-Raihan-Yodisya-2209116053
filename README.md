Nama : Raihan Yodisya NIM : 2209116053 Kelas : Sistem Informasi (B)

"LINKEDLIST"

Linked List merupakan struktur data linier berbentuk rantai simpul di mana setiap simpul menyimpan 2 item,
yaitu nilai data dan pointer ke simpul elemen berikutnya. Berbeda dengan array elemen linked list tidak ditempatkan
dalam alamat memori yang berdekatan melainkan elemen ditautkan menggunakan pointer.

Simpul pertama pada linked list disebut sebagai headh atau simpul kepala. Apabila linked list berisi kosong
, maka nilai pointer dari head menunjuk ke NULL. Begitu juga untuk pointer berikutnya dari simpul terakhir atau simpul
ekor akan menunjuk ke NULL.

Program yang dibuat menggunakan Linked list kali ini sangat simple, yaitu sebuah toko gitar. Program ini
berfungsi cukup sederhana karena dapat melakukan hal - hal seperti menambah, melihat list, menghapus, merubah
dan juga melihat riwayat apa saja yang telah kita lakukan. 

"Cara kerja program" 

Cukup simple yaitu pada bagian awal akan langsung ditampilkan 6 Menu, 1. Menambahkan Merk Gitar
2. Melihat Daftar Gitar Yang Tersedia, 3. Mengedit / Mengubah Daftar Gitar Yang Tersedia, 4. Menghapus Daftar Gitar Yang Tersedia, 
5. Riwayat Daftar Gitar Yang Tersedia, 0. Keluar

Jika user melakukan input "1" pada program, maka akan langsung muncul tampilan "Isi Merk Gitar Baru : ", dan 
user bisa langsung mengisi merk gitar apa yang ingin masuk di Linked list

Jika user melakukan input "2" pada program, maka akan langsung tampil semua barang yang ada.

Jika user melakukan input "3" pada program, maka user akan diarahkan untuk mengisi merk gitar yang sudah ada
dan mengganti dengan nama merk gitar terbaru.

Jika user melakukan input "4" pada program, maka user akan mengisi salah satu nama merk gitar yang 
ingin dihapus. 

Jika user melakukan input "5" pada program, maka akan muncul riwayat / history user selama melakukan 
setiap aktivitas di dalam program. Dan yang terakhir,

Jika user melakukan input "0" pada program, maka akan langsung keluar dari program.

"Penjelasan singkat dari fungsi" yang ada pada program implementasi sederhana dari 
struktur data linked list yang digunakan untuk menyimpan dan mengatur daftar merk gitar :

- Append() adalah sebuah fungsi yang digunakan untuk menambahkan suatu data kedalam list.
- Update() adalah sebuah fungsi yang digunakan untuk mengubah sebuah data pada node tertentu yang ada pada linked list.
- Display_History() berfungsi untuk menampilkan sebuah riwayat operasi yang telah dilakukan oleh Linked list.

"Output Program"

![image](https://user-images.githubusercontent.com/126870046/225969164-b0dc4061-afa6-48b6-b7a2-0b9994735436.png)

![image](https://user-images.githubusercontent.com/126870046/225969187-0e865046-fd49-4fea-a4f1-9eee758f04bd.png)

![image](https://user-images.githubusercontent.com/126870046/225969226-1cca6b68-6fa4-4219-a522-6167bd1136b5.png)

![image](https://user-images.githubusercontent.com/126870046/225969248-7d471862-31dc-46f1-af26-ecaf9844b43d.png)

![image](https://user-images.githubusercontent.com/126870046/225969285-aeb469b5-d691-48d9-b2eb-c990f3395325.png)

![image](https://user-images.githubusercontent.com/126870046/225969316-f6b9bdfc-e050-4a09-bcf0-6d692833087b.png)
