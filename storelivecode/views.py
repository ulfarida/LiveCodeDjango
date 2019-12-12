from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Barang

# Create your views here.
def index(request):
    barangs = Barang.objects.all()
    var_barangs = {'barangs' : barangs}
    return render(request, 'storelivecode/index.html', var_barangs)

def deskripsi(request, barang_id):
    barang = Barang.objects.get(pk=barang_id)
    var_barang = {'barang' : barang}
    return render(request, 'storelivecode/deskripsi.html', var_barang)

def input_barang(request):
    return render(request, 'storelivecode/form.html', {})

def tambah_barang(request):
    nama = request.POST['nama']
    harga = request.POST['harga']
    deskripsi = request.POST['deskripsi']
    picture = request.POST['picture']

    baranginput = Barang(nama=nama, harga=harga, deskripsi=deskripsi, picture=picture)
    baranginput.save()
    
    return redirect('index')
