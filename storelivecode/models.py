from django.db import models

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=200)
    harga = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=2000)
    picture = models.CharField(max_length=1000)

    def __str__(self):
        return self.nama