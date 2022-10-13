 
# Tugas 6 PBP

### Perbedaan _Asynchronous Programming_ dan _Synchronous Programming_
Perbedaan dari asynchronous programming dengan synchronous programming adalah bagaimana alur berjalannya dari program-program. Pada synchronous ketika program/kode sedang di jalankan, maka program selanjutnya harus menunggu program sebelumnya selesai untuk bisa dijalankan, permintaan klien akan diblokir untuk memastikan tidak ada program yang berjalan bersamaan. Sedangkan pada asynchronous program tidak perlu menunggu program sebelumnya selesai untuk bisa dijalankan, program-program di asynchronous bisa berjalan secara serentak, sehingga asynchronous lebih cepat dibanding asynchronous.

### Paradigma _Event-Driven Programming_
Teknik pemrograman yang konsep eksekusi programmnya terjadi karena suatu event

### Penerapan _Asynchronous Programming_ pada AJAX
Kita bisa menggunakan library JavaScript, yaitu jQuert dengan menambahkan `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>` ke head HTML. kemudian menambahkan `<script>` tag di dalam badan html. Buat program sesuai yang diminta, seperti $.ajax() ke POST, DELETE, dll. Ajax akan membaca event yang kita request dalam script untuk melakukan tindakan yang inginkan. Respons itu akan diproses secara asinkron di server. Data akan ditampilkan di halaman tanpa perlu refresh.

### Implementasi Tugas 6
1. Membuat views untuk dapat menampilkan seluruh data objek Task dalam bentuk JSON.
2. Data-data tersebut dikirim ke HTML dengan menggunakan request GET dari ajax, sehingga nantinya semua objek Task dapat ditampilkan di halaman web secara _asynchronous_
3. Membuat request POST ajax dari data form pada model Task untuk membuat fitur add task
4. Melakukan request GET kembali setelah melakukan POST untuk mengupdate halaman web setelah task baru ditambahkan
5. Melakukan modifikasi fungsi update dan delete task dengan menambahkan event handler untuk menghapus dan mengubah status task, kedua fungsi ini memerlukan paramater berupa ID objek (pk) task agar dapat mengubah objek yang dipilih user
6. Lakukan request GET tiap pemanggilan fungsi tersebut untuk mengupdate halaman.
