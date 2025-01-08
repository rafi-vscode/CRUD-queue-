from django.db import models

class Antrian(models.Model):
    nama = models.CharField(max_length=100)
    umur = models.IntegerField()
    nomor_hp = models.CharField(max_length=20)
    poli = models.CharField(max_length=20)  # Bisa 'anak' atau 'umum'
    status = models.BooleanField(default=False)  # Untuk menandakan apakah antrian sudah selesai
    selesai = models.BooleanField(default=False)  # Untuk menandakan apakah antrian selesai atau belum

    def __str__(self):
        return f"{self.nama} - {self.poli}"


