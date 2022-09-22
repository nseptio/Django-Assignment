# Tugas 3 PBP

Link menuju [HTML](https://mengdjango.herokuapp.com/mywatchlist/html/) [JSON](https://mengdjango.herokuapp.com/mywatchlist/json/) [XML](https://mengdjango.herokuapp.com/mywatchlist/xml/)

### Perbedaan antara JSON, XML, dan HTML ###

Fungsi utama HTML berbeda dengan JSON dan XML. HTML berfokus pada menampilkan data ke halaman web menggunakan tag, sedangkan JSON dan HTML berfokus pada _data delivery_ dan menyimpan data di database server. Penulisan ketiganya terlihat jelas berbeda. HTML menggunakan tag untuk mendeskripsikan setiap element dan dapat memiliki attribute. JSON menggunakan tipe data yang mirip dengan Map atau Dictionary yang mana setiap element memiliki key dan value. XML mirip dengan HTML, yaitu menggunakan tag sehingga terlihat lebih terstruktur daripada JSON.

### _Data Delivery_ ###

_Data delivery_ diperlukan sebagai alat komunikasi antar database dan pengguna sehingga data yang ada di database kita dapat ditampilkan ke web (platform). Data pengguna dapat diakses sehingga dapat berinteraksi dengan pengguna tersebut. Selain itu, _data delivery_ berguna untuk menyesuaikan data yang diperlukan untuk dikirim ke tampilan pengguna sehingga tidak semua data harus dikirim. Dengan begitu, waktu pengiriman data dapat lebih efesien.

### Langkah Implementasi tugas 3 ###

1. Membuat folder aplikasi mywatchlist dengan perintah `python manage.py startapp mywatchlist`
2. Membuat class models bernama MyWatchListtItem dengan attribut sesuai deskripsi tugas 3
3. Menambah mywatchlist di INSTALLED_APPS di folder project_django dan melakukan migrasi dengan perintah `python manage.py makemigrations` dan `python manage.py migrate`
4. Membuat folder bernama fixtures di dalam folder mywatchlist dan membuat berkas bernama initial_mywatchlist_data.json
5. Mengisi berkas initial_mywatchlist_data.json dengan 10 objek dan load data dengan perintah `python manage.py loaddata initial_mywatclist_data.json`
6. Membuat lima fungsi pada berkas views.py, show_mywatchlist, show_mywatchlist_xml, show_mywatchlist_json, serta akses JSON dan XML dengan id yang masing-masing akan menyajikan data dalam format html, xml, dan json
7. Membuat folder templates dan berkas watchlist.html yang akan menjadi response untuk ditampilkan dalam format html
8. Menambahkan lima fungsi yang telah dibuat ke file urls.py pada folder mywatchlist untuk memetakan fungsi yang akan dipanggil berdasarkan alamat yang dituju. Kemudian menambahkan path file tersebut ke file urls.py di folder proyek django.
9. Menambahkan `release: sh -c 'python manage.py migrate && python manage.py loaddata initial_mywatchlist_data.json'
web: gunicorn project_django.wsgi --log-file -` di berkas Procfile untuk load data ke aplikasi Heroku
10.  Menambahkan unit test pada tests.py dengan membuat class dan tiga fungsi di dalamnya untuk menguji URL yang telah kita buat mengembalikan respon HTTP 200 OK

### Screenshoot Postman ###

## HTML ##
![image](https://user-images.githubusercontent.com/87903309/191660106-54a8254a-cdc0-43d0-9f14-1ed1c628f9ec.png)

## JSON ##
![image](https://user-images.githubusercontent.com/87903309/191660038-1e256ccc-4f2f-469e-a8de-fbeba208dacf.png)

## XML ##
![image](https://user-images.githubusercontent.com/87903309/191659982-848378b7-2ef6-4f09-87b5-fc2fe479b94e.png)
