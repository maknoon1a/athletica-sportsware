**Step-step dalam mengimplementasikan checklist tugas:**

1. Membuat direktori utama bernama athletica_sportsware yang akan menjadi root folder projek
2. Membuat file bernama requirements.txt yang berisikan library dan dependency yang akan digunakan dalam pengembangan web
3. Membuat virtual environment di dalam root folder tersebut agar seluruh library dan dependency terisolasi (terpisah dari sistem) dengan perintah **python -m venv env**
4. Mengaktifkan virtual environment di root folder dengan perintah **env/Scripts/activate**
5. Menginstall dependency dengan perintah pip install **-r requirements.txt**
6. Menjalankan perintah django-admin **startproject athletica_sportsware .** untuk membuat projek django di root folder
7. Membuat file **.env** yang berisikan environment variabel PRODUCTION dan di set False agar menggunakan database lokal
8. Membuat file **.env.prod** yang berisikan environment variabel kredensial database dan PRODUCTION di set True agar menggunakan database sesuai kredensial saat web di deploy
9. Konfigurasi file settings.py yang ada di project django
      1. Menambahkan **from dotenv import load_dotenv** untuk membaca file .env
      2. Menambahkan **import os** untuk mengakses nilai environment variable yang ada di file .env
      3. Mengonfigurasi database sesuai dengan nilai PRODUCTION
      4. Menambahkan **"localhost" dan "127.0.0.1"** ke ALLOWED_HOSTS
      5. Menambahkan **PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true'** di atas DEBUG untuk konfigurasi nilai PRODUCTION
      6. Mengonfigurasi database berdasarkan nilai database dengan kredensial yang diambil dari .env.prod
         
10. Menambahkan file .gitignore yang berisikan nilai-nilai yang diambil dari tutorial 0
11. Membuat aplikasi bernama main dengan perintah **django-admin startapp main**
12. Menambahkan 'main' pada INSTALLED_APPS yang ada di settings.py
13. Menambahkan folder template dan membuat main.html di dalamnya untuk template html yang menampilkan nama, npm, nama project, dan kelas
14. Membuat model yang berisika atribut-atribut yang ditetapkan
15. Menjalankan perintah **python manage.py makemigrations** lalu diikuti dengan **python manage.py migrate** untuk migrasi database sesuai dengan model yang sudah dibuat
18. Menambah **from django.shortcuts import render** di views.py untuk render template html yang digunakan
19. Membuat fungsi show_main yang mereturn render dari main.html yang contextnya berisikan data diri
20. Membuat file urls.py di aplikasi main, lalu menambahkan **from django.urls import path** dan menambahkan path '' untuk menampilkan fungsi show_main dengan nama path "show_main"
21. Menambahkan **from django.urls import path, include** pada urls.py yang ada di **project** lalu meng-include prefix lokasi '' agar diroute ke main.urls
22. Menjalankan perintah **git init** di root folder untuk menginisialisasi folder kosong .git (repo lokal)
23. Membuat repository baru di github bernama athletica-sportsware
24. Mengubungkan repository lokal (root folder) ke repository github dengan perintah **git remote add origin https://github.com/maknoon1a/athletica-sportsware**
25. Membuat branch baru pada repository github bernama master dengan perintah **git branch -M master**
26. Menjalankan perintah add, commit, dan push ke github dengan branch master
27. Membuat project di PWS bernama athleticasportsware, lalu menambahkan isi dari .env.prod ke environment variablesnya dengan SCHEMA = tugas_individu
28. Menambahkan URL project ke ALLOWED_HOSTS yang ada di settings.py
29. Menambahkan remote di root folder ke PWS dengan menjalankan perintah yang ada di "builds" dan memasukkan kredensial projet
30. Melakukan add, commit, dan push ke github

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Bagan alur kerja request client ke web server dan kaitannya dengan urls.py, views.py, models.py, dan templates (berkas html)

<img width="1494" height="981" alt="image" src="https://github.com/user-attachments/assets/b437cf2e-c5b9-4c72-8786-08de50d63c88" />
referensi: https://learnbatta.com/blog/understanding-request-response-lifecycle-in-django-29/      


1. Awal mulanya, pengguna mengetik alamat website, contohnya host/products/ di browser, dan permintaan ini dikirim ke server web (Nginx).
2. Nginx menerima permintaan dan meneruskannya ke server aplikasi (Gunicorn) yang menjalankan kode Django.
3. Di Django, permintaan pertama kali diperiksa oleh berbagai komponen keamanan dan utility (Middleware) untuk memastikan segala sesuatunya valid dan aman.
4. Sistem kemudian mencari di daftar URL (urls.py) untuk menentukan fungsi View yang bertanggung jawab menangani halaman yang diminta.
5. Fungsi View yang ditunjuk kemudian bekerja. Fungsi View mengambil data dari database jika diperlukan dan menyiapkannya untuk ditampilkan.
      - Jika mengikuti alur merah, View mengambil data utama dari database menggunakan ORM. Contohnya, Product.objects.all() untuk menampilkan daftar produk.
      - Jika mengikuti alur biru, View hanya menyiapkan data inti secukupnya, sementara data tambahan (misalnya daftar kategori produk) nanti langsung diambil oleh template menggunakan template tags.
6. Django secara otomatis menambahkan data umum yang hampir selalu dibutuhkan (seperti info user yang login) ke dalam data yang akan ditampilkan.
7. Data yang sudah disiapkan dimasukkan ke dalam template HTML untuk menghasilkan halaman web yang utuh.
      - Pada alur merah, template sudah menerima data lengkap dari View (misalnya daftar produk, harga, stok), jadi template hanya perlu menampilkan.
      - Pada alur biru, template mungkin masih melakukan query tambahan lewat template tags untuk data dekoratif (misalnya sidebar kategori atau jumlah komentar).
8. Sebelum dikirim, halaman yang sudah jadi sekali lagi diperiksa dan mungkin ditambahi header keamanan tertentu.
9. Django mengirimkan hasil akhirnya kembali ke Gunicorn
10. Lalu dari Gunicorn diteruskan ke Nginx.
11. Nginx mengirimkan halaman web tersebut kembali ke browser pengguna, yang akhirnya ditampilkan tampilan html yang lengkap.

models.py adalah "cetak biru" yang menghubungkan kode Python dengan database, dimana kita mendefinisikan struktur tabel dan kolom-kolomnya. Ketika View memproses request, dia menggunakan ORM untuk mengambil data berdasarkan model ini (misalnya Product.objects.all()), baik secara langsung maupun melalui template tags yang juga merujuk ke models.py. Saat template dirender dan ditampilkan ke user, semua data yang muncul seperti {{ product.name }} sebenarnya tetap berasal dari struktur model yang sudah kita definisikan di models.py. Jadi, mau data diambil lewat View langsung atau melalui template tags, semuanya bergantung pada "aturan main" yang ditetapkan di models.py sebagai fondasi utama struktur data aplikasi kita.

disunting dengan bantuan chatgpt.com

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

settings.py adalah inti dari konfigurasi Django yang mengatur seluruh aspek aplikasi. File ini berisi pengaturan database (SQLite atau PostgreSQL), daftar aplikasi yang digunakan (INSTALLED_APPS), middleware untuk memproses request/response, lokasi template dan file statis, pengaturan keamanan seperti SECRET_KEY dan ALLOWED_HOSTS, serta konfigurasi bahasa dan zona waktu. Singkatnya, settings.py adalah "remote control" proyek Django dimana developer mengontrol semua perilaku aplikasi dari satu tempat.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Migrasi adalah sistem Django untuk menyinkronkan perubahan model dengan database secara otomatis. Prosesnya dimulai ketika developer membuat atau mengubah model di models.py, lalu menjalankan python manage.py makemigrations agar Django membaca perubahan dan membuat file instruksi migrasi (seperti CREATE TABLE atau ALTER TABLE) di folder migrations. Setelah itu, python manage.py migrate mengeksekusi instruksi tersebut ke database, dan Django mencatat setiap migrasi yang sudah dijalankan di tabel django_migrations. Dengan sistem ini, developer tidak perlu repot menulis SQL manual karena ORM dan migrasi otomatis memastikan struktur database selalu sinkron dengan model Python.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
