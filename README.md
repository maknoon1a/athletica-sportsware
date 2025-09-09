Step-step dalam mengimplementasikan checklist tugas:
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
22. Menjalankan perintah **git init** di root folder untuk menginisialisasi folder kosong .git
23. Membuat repository baru di github bernama athletica-sportsware
24. Mengubungkan repository lokal (root folder) ke repository github dengan perintah **git remote add origin https://github.com/maknoon1a/athletica-sportsware**
25. Membuat branch baru pada repository github bernama master dengan perintah **git branch -M master**
26. Menjalankan perintah add, commit, dan push ke github dengan branch master
27. Membuat project di PWS bernama athleticasportsware, lalu menambahkan isi dari .env.prod ke environment variablesnya dengan SCHEMA = tugas_individu
28. Menambahkan URL project ke ALLOWED_HOSTS yang ada di settings.py
29. Menambahkan remote di root folder ke PWS dengan menjalankan perintah yang ada di "builds" dan memasukkan kredensial projet
30. Melakukan add, commit, dan push ke github
