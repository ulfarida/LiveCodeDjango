from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:barang_id>', views.deskripsi, name='deskripsi'),
    path('input_barang', views.input_barang, name='input_barang'),
    path('tambah_barang', views.tambah_barang, name='tambah_barang'),
]