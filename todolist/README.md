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
