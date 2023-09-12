from django.shortcuts import render
  
def show_main(request):
    context = {
        'name' : "Rizvanu Satrio Nugroho",
        'class' : "Pemrogaman Berbasis Platform - F"
    }
    return render(request, "main.html", context)