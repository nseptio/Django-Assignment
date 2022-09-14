# Tugas 2 Assignment PBP/PBD

Link menuju [aplikasi Heroku](https://mengdjango.herokuapp.com/katalog/)

### Bagan _Request Client_ 



### _Virtual Environment_

_Virtual environment_ adalah alat yang berfungsi untuk membuat lingkungan virtual yang terpisah
dan terisolasi. Terisolasi berarti tertutup dan tidak bisa diakses dari luar. Ini diperlukan
setiap ketika kita membuat proyek Django baru agar tidak bentrok dengan proyek yang lain.
_Virtual environment_ dapat mengisolasi _package_ serta _dependencies_ dari setiap proyek
sehingga tidak ada bentrok antar versi yang lain. Misalkan, kita mempunyai proyek aplikasi
menggunakan django 1.1. Lalu, kita ingin meng-_upgrade_ versi Django ke 4.0. Namun, terdapat
proyek lain yang menggunakan versi lama. Akibatnya, aplikasi tersebut tidak bisa dijalankan
karena banyak perubahan dari versi yang lama. Oleh karena itu, setiap proyek Django sebaiknya
menggunakan _virtualenv_-nya sendiri.

### Cara Implementasi

Pada tugas ini, saya banyak melihat prosedur di tutorial 1. Pertama, saya membuat fungsi 
show_katalog di views.py pada folder katalog. Fungsi itu dapat mengambil data dari class
yang ada di models.py dengan mengimport class CatalogItem dan menyimpannya di dalam 
dictionary bernama context. Fungsi show_katalog akan me-return fungsi render yang akan 
mengirimkan data yang ada di context ke template HTML. Tahap selanjutnya melakukan routing
pada urls.py dengan menambahkan path katalog pada list urlpatterns sebagai mapping ke
app katalog. Pada tahap ini, kita sudah dapat melihat tamplian HTML yang berisi data context
melalui localhost. Selanjutnya, saya melakukan deployment ke aplikasi Heroku. Hal pertama yang
saya lakukan adalah menambah dua variabel secret di repositori github HEROKU_API_KEY dan 
HEROKU_APP_NAME. Value HEROKU_API_KEY didapat dari API key yang ada di akun Heroku, sedangkan
HEROKU_APP_NAME adalah nama aplikasi yang telah kita buat di Heroku. Karena file dpl.yml dan
Procfile sudah ada, kita dapat langsung melakukan deployment ke aplikasi Heroku.
