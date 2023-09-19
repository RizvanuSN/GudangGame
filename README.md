# Nama  : Rizvanu Satrio Nugroho
# NPM   : 2206823682
# Kelas : PBP - F
---
# Tautan aplikasi Adaptable: https://gudanggame7.adaptable.app 
-- 

# TUGAS 2!!

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
<img src="/READMEIMG/BaganRequestClient.png" alt="Bagan Request Client">

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

# TUGAS 3!!

# 1. Apa perbedaan antara form POST dan form GET dalam Django?
POST
- Pada umumnya digunakan untuk mengirim data ke server untuk membuat, mengupdate, dan menghapus resource pada server.
- Lebih aman untuk data sensitif karena data nya berada di request body yang tidak terlihat di URL.
- Tidak ada limitasi ukuran data pengiriman.
- Pelaksanaan request beberapa kali dapat menghasilkan hasil yang berbeda (Non-Idempotent).

GET
- Pada umumnya digunakan untuk mengambil data dari server.
- Kurang aman untuk data sensitif karena data yang disubmit diappend pada URL sebagai query parameter.
- Memiliki limitasi ukuran data pengiriman kepada URL.
- Pelaksanaan request beberapa kali menghasilkan hasil yang sama (Idempotent).

# 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
| Kriteria | XML | JSON | HTML |
|----------|----------|----------|----------|
| Struktur data | Bahasa markup yang fleksibel serta dapat digunakan untuk merepresentasikan berbagai tipe data. Strukturnya kuat dan mendefinsikan aturan dalam mengorganisir data dalam dokumen seperti hierarki elemen dan atribut. | Format data yang compact yang berisi objects dan arrays. Cocok dalam merepresentasikan data yang terstruktur. | Bahasa markup yang digunakan untuk membuat dokumen web. |
| Penggunaan Umum | Pertukaran data antar aplikasi, konfigurasi, dan semi-structured penyimpanan data | Pertukaran data antar aplikasi terutama dalam pengembangan web. Banyak aplikasi dan web service modern yang menerima dan mengirim data dalam format JSON | Membuat web pages yang digunakan spesifik untuk presentasi web dan interaksi user |

# 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Memiliki format yang ringkas dan mudah dibaca oleh manusia karena menggunakan object dan notasi array yang mirip dengan sintaks JavaScript.
- Merupakan format data bahasa-agnostik yang berarti dapat digunakan dengan berbagai bahasa pemrogaman. Dengan itu, aplikasi yang dibuat dengan bahasa pemrogaman lain dapat melakukan komunikasi melalui JSON sebagai format pertukaran data.
- Berbagai bahasa pemrograman memiliki built-in support untuk melakukan parsing dan serializing data dalam format JSON.
- Support cross-domain requests melalui metode seperti JSONP (JSON with Padding) dan CORS (Cross-Origin Resource Sharing) yang dapat membuat aplikasi web untuk mengambil data dengan aman dari berbagai domain.

# 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat input form untuk menambahkan objek model pada app sebelumnya.
Pertama, saya membuat 'base.html' pada direktori templates yang berada pada root directory yang berisikan :
~~~
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
~~~

Kemudian, saya mengedit 'settings.py' pada subdirektori 'GudangGame' atau nama aplikasi dan ubah baris TEMPLATES agar dapat mendeteksi 'base.html' sebagai berkas HTML dengan kode berikut :
~~~
...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
...
~~~

Dan saya juga menambahkan kode dibawah ini pada 'main.html' yang ada pada direktori 'main/templates' agar 'base.html' menjadi template utama :
~~~
{% extends 'base.html' %}
~~~

Lalu, saya membuat 'forms.py' pada direktori main untuk membuat struktur form yang dapat menerima data game baru yang berisikan :
~~~
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "developer", "price", "genre","amount","description"]
~~~
Pada kode tersebut ProductForm dibuat dengan menginherit ModelForm. Kemudian, memberikan properti model dengan model yang telah kita buat (Product) dan memberikan properti fields yaitu 'name, developer, price, genre, amount, description'

Kemudian, saya mengubah function 'show_main' pada 'views.py' yang berada di direktori 'main' menjadi :
~~~
import datetime

def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Rizvanu Satrio Nugroho', # Nama kamu
        'class': 'PBP F', # Kelas PBP kamu
        'products': products,
        'total' : products.__len__(),
        'tanggal' : datetime.date.today().strftime("%d/%m/%Y")
    }

    return render(request, "main.html", context)
~~~
variable 'products' menyimpan semua object Product yang telah diinput kemudian di 'context' saya menambahkan key 'products' untuk memanggil variable tersebut serta 'total' yang akan memanggil banyaknya Product yang diambil dengan method '__len__()' dan juga 'tanggal' yang mengambil tanggal hari ini melalui class date yang telah diimport.

Lalu, saya membuat 'create_product.html' pada direktori '/main/templates' sebagai web document baru saat ingin menambahkan product dengan menambahkan kode berikut :
~~~
<style>
    h1, h2, h3, h4, h5, h6, tr, td {
        font-family:'Courier New', Courier, monospace;
        margin-bottom: 5px; 
        text-align: left;
    }

    input[type="submit"] {
        font-family:'Courier New', Courier, monospace;
        background-color: #3b5d81;
        color: white;
    }

    input[type="submit"]:hover {
        background-color: #0056b3;
    }
</style>   
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Game</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Game"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
~~~
Pada kode ini, kode mengextend dari template, membuat struktur, menambahkan proteksi CSRF, dan melakukan render field form pada tabel HTML di 'main.html'. Ketika user telah melakukan klik 'Add Game', maka data akan dikirim ke server. (style block ditambahkan untuk bentukan tampilan web)

Terakhir, saya juga menambahkan function 'create_product' ke urls.py dan membuat path yang sesuai agar file HTML yang dibuat sebelumnya dapat diakses. Isinya adalah :
~~~
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
~~~

- Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
Saya membuat function yang sesuai yaitu 'show_json' , 'show_xml' , 'show_xml_by_id' ,dan 'show_json_by_id' pada 'urls.py' yang berada pada 'main'. Fungsi masing - masing yaitu :

show_json
~~~
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
~~~

show_xml
~~~
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
~~~

show_json_by_id
~~~
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")    
~~~

show_xml_by_id
~~~
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")    
~~~

Function untuk melihat HTML sudah ditambahkan di step sebelumnya dan juga tugas sebelumnya yaitu 'show_main' dan 'create_product'

Kemudian, saya menambahkan routing URL yang sesuai dari masing - masing function pada 'urls.py' dengan mengubahnya menjadi :
~~~
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]
~~~
function path tersebut akan mengappend routing URL yang sesuai ke address website dan menjalankan fungsi yang sesuai.

- Cara pengerjaan soal bonus
Saya menambahkan key 'total' pada dictionary 'context' pada 'views.py' yang akan menyimpan panjang Products / total Product yang dihasilkan dari fungsi len

Kemudian saya menambahkan 
~~~
<h5 class="total">Anda telah menambahkan game sebanyak {{total}} game</h5>
~~~
pada 'main.html' dan memanggil key 'total'

# 5.Mengakses kelima URL di poin 2 menggunakan Postman
- HTML (url) dan (url)/create_product
<img src="/READMEIMG/create_product(HTML).jpg" alt="create_product(HTML)">
<img src="/READMEIMG/main(HTML).jpg" alt="main(HTML)">

- XML
<img src="/READMEIMG/XML.jpg" alt="XML">

- JSON
<img src="/READMEIMG/JSON.jpg" alt="JSON">

- XML BY ID
<img src="/READMEIMG/XML_BY_ID.jpg" alt="XML BY ID">

- JSON BY ID
<img src="/READMEIMG/XML_BY_ID.jpg" alt="JSON BY ID">