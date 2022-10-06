# Tugas 4 PBP

Deployment ke Heroku [di sini](https://mengdjango.herokuapp.com/todolist/)

### Kegunaan {% csrf_token %} pada elemen <form>
CSRF token berguna untuk mencegah serangan CSRF (Cross Site Request Foreign). Token akan digunakan untuk melakukan autentikasi pengguna dan selalu diperbarui saat memuat halaman web. Jika {{% csrf_token %}} tidak disertakan pada elemen <form>, maka Django akan memberikan pesan error berisi situs tersebut memerlukan cookie CSRF saat mengirim formulir.

### Membuat elemen <form> secara manual
Kita tetap dapat membuat form tanpa menggunakan {{form.as_table}}. Pertama, kita buat semua field yang diperlukan dengan tag `<input>`. Di dalam tag, isi attribut `type= ` sesuai kebutuhan beserta text fieldnya. Jika sudah membuat semua input, tambahkan `<input type="submit"/>` untuk melalukan submit form tersebut

### Proses alur data
Ketika pengguna melakukan submisi form, maka hal tersebut melalukan sebuah _request_ dengan method HTTP POST ke server. Setelah itu, server akan mengecek request valid atau tidak. Jika valid, dilakukan penyimpanan data tersebut ke _database_ server sehingga  data yang telah disimpan bisa ditampilkan ke template HTML.

### Langkah implementasi Tugas 4
1. Membuat aplikasi baru bernama todolist dengan melakukan perintah di terminal `python manage.py startapp todolist` serta mendaftarkannya dengan menambah `todolist` ke dalam variable `INSTALLED_APPS` pada folder `project_django`.
2. Menambahkan path aplikasi todolist sehingga dapat diakses di localhost dengan cara menambah `path("todolist/", include("todolist.urls")),` ke `urls.py` pada folder `project_django`.
3. Membuat sebuah model dengan class bernama `Task` pada berkas `models.py`. Setelah itu, menambah fields sesuai dengan ketentuan tugas. Kemudian, melakukan migrasi models yang sudah dibuat dengan perintah `python manage.py makemigrations` lalu `python manage.py migrate`.
4. Membuat fungsi pada `views.py` todolist:
    - show_todolist, fungsi untuk halaman utama yang menampilkan semua task user. Sebelum bisa mengaksesnya, perlu melakukan login terlebih dahulu karena terdapat kode `@login_required(login_url='/todolist/login/')`.
    - register, untuk melakukan registrasi pengguna baru
    - login_user, melakukan autentikasi pengguna dengan username dan password
    - logout_user, untuk keluar dari halaman utama
    - create_task, membuat form berdasarkan `forms.py` untuk membuat task baru
    - delete_task, untuk menghapus task
    - update_task, untuk mengubah status task pengguna, selesai atau belum.
5. Memetakan fungsi yang telah dibuat di `views.py` ke `urls.py`
6. Membuat template HTML:
    - todolist, halaman utama
    - login
    - register
    - create-task, membuat task baru.
 7. Melakukan _deployment_ ke Heroku. Karena sudah diatur pada tugas sebelumnya, maka hanya melakukan push ke github.
 8. Membuat dua akun pengguna dan tiga dummy data.
 
 # Tugas 5 PBP
 
 ### Perbedaan Inline, Internal, dan External CSS
    - Inline: kode CSS yang ditulis langsung pada atribut style di tag elemen HTML
    - Internal: kode CSS yang ditulis di dalam tag `<style>` di bagian head dokumen HTML 
    - External: kode CSS yang ditulis terpisah dengan kode HTML. Eksternal CSS ditulis di dalam file khusus yang berekstensi `.css` dan harus ditautkan ke HTML melalui tag `<link>` di bagian HEAD.
    
### Tag HTML5
    - `<div>` merupakan tag yang membagi section yang tidak memiliki arti khusus. Tag ini biasa digunakan sebagai kontainer untuk dapat dikustomisasi dengan CSS
    - `<header>`, tag yang dapat digunakan untuk menandai bagian halaman merupakan header dari halaman web itu
    - `<article>`, tag untuk menandakan bagian artikel dalam sebuah halaman web, seperti _forum post_, blog, dll.
    - `<section>` dapat digunakan untuk membagi setiap bagian konten halaman web
    - `<footer>` tag yang dapat digunakan untuk menandai bagian itu merupakan footer dari halaman web.
    
### CSS Selector
    1. `*`, selector yang bersifat universal sehingga akan diwariskan ke semua elemen HTML
    2. `name-tag`, selector yang hanya berlaku pada tag HTML yang dipilih
    3. `#id-name`, selector yang memilih elemen dengan id yang unik
    4. `.class-name`, selector yang berlaku pada class elemen yang ditujuk
    5. `p:pseudo-name`, selector yang berarti memilih elemen dengan class dengan didefinisikan state khusus.

### Implementasi Tugas 5
    1. Membuat form login, register, dan create-task menjadi di tengah layar dengan cara menjadikan display-nya flex
    2. Kustomisasi halaman todolist dengan cards dari Bootstrap
    3. Membuat file `styles.css` untuk membuat kustomisasi umum
 
 
