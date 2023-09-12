# Nama  : Rizvanu Satrio Nugroho
# NPM   : 2206823682
# Kelas : PBP - F
---
# Tautan aplikasi Adaptable: https://gudanggame7.adaptable.app 
-- 

# 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, saya membuat lokal direktori yang telah saya tentukan. Kemudian saya membuat Repository di Github dengan nama yang sama dan menghubungkannya dengan local repository tersebut. Lalu, saya mengaktifkan virtual enviorentment, menginstall semua yang di dalam requirements.txt, dan  membuat proyek Django baru dengan nama "GudangGame" dengan kode :
~~~
django-admin startporject GudangGame
~~~

Kedua, saya membuat aplikasi 'main' pada direktori GudangGame dengan menjalankan kode : (menjadi python3 karena menggunakan Macbook)
~~~
python3 manage.py startapp main
~~~

Kemudian, saya membuat direktori di dalam 'main' dengan nama 'templates' dan membuat file 'main.html' sebagai file yang dapat dilihat oleh user. Kemudian saya melakukan routing pada proyek dengan menambahkan aplikasi 'main' pada 'settings.py' pada bagian INSTALLED_APPS

Lalu, 'models.py' yang ada pada direktori 'main' saya lakukan perubahan yaitu :
~~~
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=256)
    developer = models.CharField(max_length=255)
    price = models.IntegerField()
    genre = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
~~~
Saya membuat class atau model dengan nama Item yang memiliki atribut berupa :
- 'name' (CharField) yang merupakan nama dari model (pada konteks ini Judul dari Game)
- 'developer' (CharField) yang merupakan nama dari developer/pembuat dari game tersebut
- 'price' (IntegerField) yang merupakan representasi harga dari game tersebut
- 'genre' (CharField) yang merupakan tipe dari game tersebut
- 'amount' (IntegerField) yang merupakan representasi berapa banyak stock game yang tersedia
- 'description' (TextField) yang merupakan penjelasan singkat tentang sinopsi game

Kemudian saya melakukan migration agar model beserta atributesnya tersimpan di dalam database

Kemudian saya mengubah isi dari 'views.py' akan membuat fungsi show_main yang menunjukan data kepada 'main.html' sebagai berikut :
~~~
from django.shortcuts import render

def show_main(request):
    context = {
        'name' : "Rizvanu Satrio Nugroho",
        'class' : "Pemrogaman Berbasis Platform - F"
    }
    return render(request, "main.html", context)
~~~
Pada fungsi ini, ketika user menggunakan variabel berupa 'name' atau 'class' pada 'main.html' akan diubah menjadi value dari keys tersebut yang ada di dictionary context. Model dan atribut - atribut yang saya buat belum saya implementasikan pada show_main karena belum dibutuhkan datanya.

Selanjutnya, saya membuat 'urls.py' pada direktori 'main' sehingga dapat memetakan fungsi pada 'views.py' 

# 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img src="/READMEIMG/BaganRequestClient.png" alt="Bagan Request Cleint">

- 'urls.py' = Request kepada wesbite dari user akan dikirim menuju fungsi yang sesuai pada halaman tersebut. Pada konteks aplikasi ini, fungsi yang dijalankan adalah 'show_main' pada 'views.py'
- 'views.py' = Pada file ini, terdapat fungsi 'show_main' yang menerima parameter 'request' dari user. Di fungsi tersebut, juga terdapat dictionary 'context' yang akan memberikan data sesuai pemanggilan keys pada 'main.html' yang akan ditampilkan kepada user.
- 'models.py' = Models.py menyimpan class 'Item' dengan berbagai atribut seperti 'name', 'developer', 'price', 'genre', 'amount', dan 'description' yang akan digunakan untuk menunjukan data Item (Game) 
- 'main.html' = 'views.py' akan mengirim data kepada 'main.html' dan dapat dilihat oleh user

# 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual Environment digunakan pada proyek Django agar memiliki environtment yang stable, reproducible, dan portable. Berikut adalah penjelasan dari kelebihannya :
- Stable environments : Virtual environment dapat melakukan isolasi dependencies proyek (instalasi package) dari sistem. Dengan ini, perubahan sistem maupun proyek lain pada sistem tidak akan berpengaruh terhadap proyek Django kita.
- Reproducible environments : Dengan virtual environments, environment dapat dengan mudah dibuat ulang di sistem lain dalam waktu berbeda. Dengan ini, proyek Django akan berjalan secara konsisten tanpa kendala environment yang digunakan.
- Portable environment : Dengan virtual environment, proyek dapat dengan mudah dibagikan keluar sistem tanpa batasan dependencies atau proyek lain pada sistem.

Aplikasi berbasis Django masih dapat digunakan tanpa menggunakan virtual environment. Akan tetapi, dapat memiliki resiko terjadi konflik dengan proyek lokal di sistem jika melakukan installasi package. Dan juga, sistem akan tidak terorganisir dan tidak menjalankan best-practice dalam pemrograman.

# 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC, MVT, dan MVVM adalah pola arsitektur yang digunakan dalam software development untuk mengorganisir struktur dari suatu aplikasi. Adapun penjelasan dari masing - masing pola yaitu :

- MVC (Model-View-Controller) :
Pada MVC, terdapat batasan yang jelas antar komponen yang memmudahkan developer dalam menjaga dan melakukan testing dari tiap komponen. Perubahan pada model atau view tidak akan berdampak satu sama lain karena perubahannya akan menuju controller. MVC biasanya digunakan pada aplikasi web dan desktop.
    - Model : Merepresentasikan data  dan logika bisnis aplikasi. Bertanggung jawab dalam mengambil, mengelolah, dan menyimpan data
    - View : Menjadi User Interface dan bagian yang akan menunjukan data dari model dan menerima input user.
    - Controller : Komponen yang menghubungkan model dan view. Berfungsi untuk menangani input, memprosesnya, dan melakukan update terhadap model dan view.

- MVT (Model-View-Template) :
Pada MVT, terhadap pemisah yang jelas antara logika bisnis (Model), User Interface (View), dan logika presentasi (Template). Digunakan dalam web framework seperti Django
    - Model :  Merepresentasikan data  dan logika bisnis aplikasi.
    - View : Menjadi User Interface dan bagian presentasi.
    - Template : Bagian ini adalah bagian yang membedakan dari MVC. Template digunakan untuk mengontrol penyajian dalam tampilan dari Model ke View.

- MVVM (Model-View-ViewModel) :
MVVM bertujuan untuk melakukan simplifikasi hubungan antara Model dan View sehingga hasil aplikasinya memiliki User Interface yang lebih responsif dan dinamis seperti pada aplikasi handphone dan aplikasi desktop.
    - Model : Merepresentasikan data  dan logika bisnis aplikasi.
    - View : Menjadi User Interface dan bagian presentasi.
    - ViewModel : Menjadi penghubung antara Model dan View. ViewModel dapat mengubah data dari model sesuai dengan format/ketentuan yang akan ditampilkan di view.

Adapun perbedaan dari ketiga tipe arsitektur tersebut yaitu : 
- MVT menggunakan Template untuk melakukan rendering file HTML. Sedangkan, MVC dan MVVM menggunakan View untuk melakukan rendering.
- MVVM pada umumnya diasosiasikan dengan User Interface Framework yang lebih modern dan interaktif. MVC dan MVT lebih dapat digunakan dalam berbagi tipe aplikasi