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

# TUGAS 4!!
# 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah sebuah formulir yang disediakan oleh Django pada modul 'django.contrib.auth.forms' dalam membantu proses pembuatan akun pada aplikasi web berbasis Django. Form ini digunakan pada umumnya untuk memberi izin kepada pengguna untuk mendaftar atau membuat akun baru di web berbasis Django.

Kelebihan dari UserCreationForm adalah :
- Keamanan yang terintergasi termasuk validasi input berupa email dan username unik, hashing kata sandi, dan memastikan kata sandi yang dimasukin telah memenuhi kriteria yang kuat
- Mendukung integrasi dengan model User pada Django sehingga dapat mudah dihubungan dengan basis data melalui operasi CRUD (Create, Read, Update, Delete)
- Memiliki fleksibilitas konfigurasi yang dapat dengan mudah melakukan modifikasi formulir sesuai kebutuhan proyek dengan menambahkan/menghapus kolom formulir, dll. 

Kekurangan dari UserCreationForm adalah :
- Memiliki keterbatasan dalam tampilan sehingga diperlukan merancang tampilan atau template yang sesuai untuk halaman pendaftaran, dll.
- Memiliki ketergantungan terhadap model User sehingga perlu menyesuaikan model User atau membuat model User kustom jika ingin ada tambahan.
- Tidak cocok untuk proyek yang kompleks dan membutuhkan persyaratan otentikasi yang khusus.

# 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
| Aspek Perbeedaan | Autentikasi | Otorisasi |
|----------|----------|----------|
| Tujuan | Memverifikasi identitas pengguna sistem | Memastikan apakah pengguna atau sistem memiliki perizinan yang penting untuk melakukan aksi spesifik atau akses suatu data |
| Dalam Django | Memiliki views, forms, dan fungsi backend | Dapat mendefinisikan perizinan dan mengelompokan penggunna ke dalam grup |
| Kepentingan | Mencegah pengguna yang tidak memiliki akses pada suatu data melakukan action | Memastikan pengguna terbatas perizinanannya terhadap role |

Alasan autentikasi dan otorisasi penting :
- Kedua proses ini memastikan keamanan aplikasi dengan autentikasi memstikan hanya pengguna yang terverifikasi yang bisa masuk dan otorisasi memastikan hanya beberapa kelompok pengguna dapat melakukan action tertentu dan mengakses data tertentu.
- Mengikuti kebutuhan legal dan regulasi seperti GDPR, HIPAA, dan PCI DSS yang mewajibkan kontrol strict terhadap akses pengguna terhadap data.
- Memastikan user experience yang baik dengan menunjukan data yang relevan bagi pengguna.

# 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah bagian kecil dari data yang dapat dikirim oleh server web menuju peramban web pengguna dan disimpan secara lokal oleh peramban web. Django menggunakan cookies untuk mengelola data sesi pengguna dengan melakukan :
- Menjadi session management dengan menyimpan user-specific information
- Menyimpan session ID
- Memprovide Cookie-Based Session Middleware
- Menjadi session configuration

# 4.  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Pada pengembangan web, pengggunaan web dianggap aman pada umumnya. Akan tetapi, ada beberapa risiko yang perlu diperhatikan. Cookies dapat mengancam keamanan pengguna karena digunakan untuk menyimpan informasi sensitif dan jika tidak diimplementasikan dengan baik, data pengguna terancam keamanannya. Cookies juga terancam dengan serangan XSS dan CSRF yang dapat mengancam keamanan jika tidak ada langkah - langkah keamanan yang tepat. Cookies juga dapat melacak pengguna tanpa perizinan mereka. 

Dengan itu, web developer harus menerapkan sistem keamanan terbaik dengan menggunakan HTTPS, mengatur flag HttpOnly, dan memberikan informasi yang jelas dan memberi notifikasi dan permintaan persetujuan pengguna saat menggunakan cookies untuk melacak aktivitas mereka.

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
## Menambahkan Halaman Register
- Melakukan import 'redirect', 'UserCreationForm', 'messages' pada 'views.py'
~~~
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
~~~

- Membuat file 'register.html' dan juga menambahckan style block yang sesuai
~~~
<style>

    .daftar_btn {
        font-family:'Courier New', Courier, monospace;
        background-color: #3b5d81;
        color: #fff;
        cursor: pointer;
    }

    .daftar_btn:hover {
        background-color: #0056b3;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family:'Courier New', Courier, monospace;
        margin-bottom: 5px; 
    }

    p, ul, .login {
        font-family:'Courier New', Courier, monospace;
        margin-top: 5px;
    }

</style>



{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input class="daftar_btn" type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
~~~

- Membuat function 'register' dalam menghubungkan html templates dan halaman pendaftaran
~~~
def register(request):
form = UserCreationForm()

if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your account has been successfully created!')
        return redirect('main:login')
context = {'form':form}
return render(request, 'register.html', context)
~~~

- Melakukan import function 'register' dan menambahkan path nya di dalam urls.py 
~~~
from main.views import register
~~~
~~~
...
path('register/', register, name='register'), 
...
~~~

## Menambahkan halaman login
- Melakukan import 'authenticate' dan 'login' pada 'views.py'
~~~
from django.contrib.auth import authenticate, login
~~~

- Membuat function 'login_user' pada 'views.py'
~~~
def login_user(request):
if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main:show_main')
    else:
        messages.info(request, 'Sorry, incorrect username or password. Please try again.')
context = {}
return render(request, 'login.html', context)
~~~

- Membuat function 'login_user' pada 'views,py'
~~~
def login_user(request):
if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('main:show_main')
    else:
        messages.info(request, 'Sorry, incorrect username or password. Please try again.')
context = {}
return render(request, 'login.html', context)
~~~

- Membuat file 'login.html' pada templates dan menambahkan style block yang sesuai
~~~
<style>
    .login_btn {
        font-family:'Courier New', Courier, monospace;
        background-color: #3b5d81;
        color: #fff;
        cursor: pointer;
    }

    .login_btn:hover {
        background-color: #0056b3;
    }

    h1, h2, h3, h4, h5, h6{
        font-family:'Courier New', Courier, monospace;
        margin-bottom: 5px; 
    }

    p, td, tr, a, t {
        font-family:'Courier New', Courier, monospace;
        margin-top: 5px;
        font-weight: bold; 
    }
</style>


{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>GudangGame Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    <t>Don't have an account yet?</t> <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
~~~

- Melakukan import function 'login_user' dan menambahkan path url nya pada 'urls.py'
~~~
from main.views import login_user
~~~
~~~
...
path('login/', login_user, name='login'),
...
~~~

## Menambahkan fitur logout
- Melakukan import 'logout' pada 'views.py'
~~~
from django.contrib.auth import logout
~~~

- Menambahkan function 'logout_user'
~~~
def logout_user(request):
    logout(request)
    return redirect('main:login')
~~

- Membuat button untuk melakukan logout pada 'main.html'
~~~
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a> 
~~~

- Melakukan import function 'logout_user' dan menambahkan path url nya pada 'urls.py'
~~~
from main.views import logout_user
~~~
~~~
...
path('logout/', logout_user, name='logout'),
...
~~~

## Melakukan rekstriksi akses halaman Main
- Melakukan import 'login_required' pada 'views.py'
~~~
from django.contrib.auth.decorators import login_required
~~~

- Menambahkan line berikut di atas function 'show_main' agar halaman main hanya dapat diakses setelah login
~~~
...
@login_required(login_url='/login')
def show_main(request):
...
~~~

## Menggunakan data dari Cookies
- Melakukan import 'datetime' pada 'views.py'
~~~
import datetime
~~~

- Menyesuaikan function 'login_user' pada 'views,py' agar dapat melihat last login
~~~
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
~~~

- Membuat function 'show_main' pada 'views.py' agar dapat memproses 'last_login' dengan menambahkannya pada dictionary 'context'
~~~
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP F', # Kelas PBP kamu
        'products': products,
        'total' : products.__len__(),
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
~~~

- Membuat function 'logout_user' sehingga menghapus cookie saat melakukan logout
~~~
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
~~~

- Menambahkan line di bawah ini pada 'main.html' agar menampilkan last login
~~~
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
~~~

## Melakukan penghubungan Model Product dengan User
- Melakukan import User pada 'models.py'
~~~
from django.contrib.auth.models import User
~~~

- Menambahkan attribute 'User' pada Product
~~~
...
user = models.ForeignKey(User, on_delete=models.CASCADE)
...
~~~

- Menyesuaikan function 'create_prouct' pada 'views.py' 
~~~
def create_product(request):
    form = ProductForm(request.POST or None)

 if form.is_valid() and request.method == "POST":
    product = form.save(commit=False)
    product.user = request.user
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))
~~~

## Implementasi Bonus
- Membuat tiga function baru pada 'views.py' yang akan dijalankan sesuai dengan button nya
~~~
def plus_product_amount(request, id):
    product = Product.objects.get(id=id)
    product.amount += 1
    product.save()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def minus_product_amount(request, id):
    product = Product.objects.get(id=id)
    if (product.amount > 0):
        product.amount -= 1
        product.save()
    else :
        messages.info(request, f'Jumlah {product.name} sudah bernilai 0!')
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response

def remove_product(request, id):
    Product.objects.filter(pk=id).delete()
    response = HttpResponseRedirect(reverse("main:show_main"))
    return response
~~~

- Mengimport function dan menambahkan path url function tersebut pada urls.py
~~~
...
from main.views plus_product_amount, minus_product_amount, remove_product
...
~~~
~~~
...
path('plus_product_amount/<int:id>', plus_product_amount, name='plus_product_amount'),
path('minus_product_amount/<int:id>', minus_product_amount, name='minus_product_amount'),
path('remove_product/<int:id>', remove_product, name='remove_product'),
...
~~~

- Mengatur penempatan button pada 'main.html'
~~~
...
<td>
    <form method="post" action="{% url 'main:plus_product_amount' product.id %}">
        {% csrf_token %}
        <button class="btn_bonus">+</button>
    </form>
    {{ product.amount }}
    <form method="post" action="{% url 'main:minus_product_amount' product.id %}">
        {% csrf_token %}
        <button class="btn_bonus">-</button>
    </form>
    <form method="post" action="{% url 'main:remove_product' product.id %}">
        {% csrf_token %}
        <button class="btn_bonus">Delete</button>
    </form>
</td>
...
~~~
<<<<<<< HEAD
=======

# TUGAS 4!!

# 1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element selector adalah jenis selector pada CSS yang dapat digunakan dalam memilih elemen HTML berdasarkan nama elemennya. Adapun tipe dan manfaat dari tiap element selector :
- Universal Selector ('*'):
Universal selector adalah selector yang dapat digunakan terhadap setiap elemen pada halaman web. Dapat digunakan ketika ingin menerapkan suatu style terhadap setiap elemen pada halaman web. Pada umumnya, selector ini digunakan saat ingin menerapkan global style seperti margin default dan padding menjadi 0 Selector ini dapat menurunkan performa jika digunakan secara berlebihan sehingga pemakaiannya harus diperhatikan dan dibataskan. Universal selector bermanfaat untuk melakukan penerapan style secara global, melakukan reset default, debugging, dan menerapkan baseline yang konsisten. 

- Type Selector:
Type selector adalah selector yang memilih semua elemen dengan HTML tag yang spesifik seperti <p>. Dapat digunakan saat ingin menerapkan suatu style pada semua elemen dengan HTML tag yang spesifik seperti headings, paragraf, lists, links, dll. Type selector bermanfaat untuk menerapkan konsistensi, semantic styling, simplisitas, dan menargetkan semua elemen dari suatu tipe spesifik

- Class Selector:
Class selector adalah selector yang digunakan untuk memilih satu atau lebih elemen dari HTML berdasarkan value 'class' yang telah didefinisikan terhadap elemen masing - masing. Class selector diawali dengan '.' dan diikuti dengan nama class nya. Class selector dapat digunakan ketika ingin melakukan styling terhadap beberapa elemen dengan karakteristik visual yang sama, membuat kustomisasi style untuk individual komponen atau widget pada halaman web, dan ketika ingin menerapkan style kepada elemen - elemen yang memiliki HTML type yang berbeda. Class selector bermanfaat dalam code reusability, spesifikasi, modularitas, dan melakukan override terhadap style default.

- ID Selector :
ID Selector digunakan saat ingin memilih satu HTML elemen berdasarkan attribut ID yang dimilikinya. ID selector diawali dengan '#' dan diikuti dengan nama ID nya. ID Selector dapat digunakan ketika ingin melakukan styling terhadap elemen spesifik, membuat anchors untuk in-page-navigation, dan menerapkan fungsionalitas JavaScript pada elemen spesifik. ID Selector memiliki manfaat berupa keunikan dan tingak spesifikitas yang tinggi.

# 2. Jelaskan HTML5 Tag yang kamu ketahui.
HTML5 adalah kumpulan elemen dan atribut yang meningkatkan efektivitas struktur dan semantik dari dokumen web. Berikut adalah beberapa contoh dari HTML5 tag:
- <header>
Tag ini merepresentasikan suatu kontainer untuk konten pengenalan atau kumpulan link navigasi yang bisasnya berisikan logo utama website, judul website, dan menu utama navigasi. Tag ini biasanya diletakkan pada bagian paling atas dari halaman atau section untuk membantu meningkatkan aksesibilitas dan struktur halaman.
- <nav>
Tag ini digunakan untuk mendefinisikan bagian dari link navigasi seperti menu atau navigasi bar. Tag ini digunakan untuk menu navigasi utama saja. 
- <footer>
Tag ini merepresentasikan footer dari suatu section ataupun dokumen. Pada bagian ini biasanya berisi metadata, informasi copyright, detail kontak, ataupun link lain yang berhubungan dengan dokumen

# 3. Jelaskan perbedaan antara margin dan padding.
| Aspek Perbeedaan | Margin | Padding |
|----------|----------|----------|
| Tujuan | Membuat ruang di luar border dari elemen serta mengatur ruang antar border elemen dan elemen lainnya | Membuat ruang  di dalam elemen di antara konten elemen dan bordernya |
| Pengaruh terhadap ukuruan elemen | Tidak mengubah ukuran elemen, tetapi mengubah posisi terhadap elemen lain | Mengubah ukuran elemen |
| Visibilitas | Pada umumnya margin dapat terlihat dan dapat membuat ruang antar elemen yang terlihat | Terlihat dalam elemennya membuat kontenn nya menjauh dari border |
| Kasus penggunaan | Membuat ruang antar elemen, membuat margin di antara page, melakukan centering dari suatu elemen secara horizontal maupun vertikal, melakukan pengaturan terhadap layout dari elemen block-level | membuat ruang antar konten di dalam elemen, membuat tombol, cards, dan containers dengan internal spacing, serta melakukan pengaturan terhadap layout dari inline dan inline-block elements |

# 4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
| Aspek Perbeedaan | CSS Tailwind | Bootstrap |
|----------|----------|----------|
| Approach | Utility-first approach yang menyediakan kumpulan dari utility classes yang dapat diterapkan pada elemen HTML. Class - class tersebut sudah memiliki style yang terdefinisi untuk beberapa aspek elemen seperti margin dan padding | Component-based yang menyediakan kumpulan komponen UI yang sudah didesain sebelumnya yang dapat digunakan dan diubah sesuai pengguna |
| Kustomisasi | Dapat diubah dengan cukup kompleks sesuai dengan kebutuhan pengguna | Dapat diubah tetapi terdapat batasan |
| Ukuran file | Menghasilkan file CSS yang lebih kecil ukruannya karena hanya berisikan style yang digunakan membuat lebih efisien dalam aspek performa | Menghasilkan file CSS yang lebih besar ukurannya karena berisikan styles untuk semua komponen walaupun tidak digunakan. Hal ini dapat mengaruhi load time  |
| Kasus penggunaan | Proyek yang membutuhkan kustomisasi desain dan  kontrol terhadap style yang digunakan | Proyek yang memiliki desain yang konsisten dan sudah sesuai standar. Bootstrap juga cocok untuk kolaborasi tim dan memastikan semua hasilnya memiliki tampilan yang sama dan sesuai |

# 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
- Pertama saya membuat suatu design dan warna yang univrsal untuk semua tampilan HTML dengan menggunakan warna '#3b5d81' dan font 'Courier New', Courier, monospace'

- Kemudian saya menerapkannya pada HTML masing - masing dengan menggunakan style block dan juga menerapkan placement yang sesuai dengan selector

- Saya juga menaruh berbagai itmem di dalam container agar terlihat rapih dan juga navbar pada main.html
>>>>>>> 36593b9 (Tugas 5 selesai)
