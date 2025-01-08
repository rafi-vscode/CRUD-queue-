from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout  # Import logout
from .models import Antrian
from .forms import AntrianForm

def signout(request):
    logout(request)  # Logout pengguna
    return redirect('keluar')  # Redirect ke halaman logout-success

# View untuk halaman kosong setelah logout
def logout_success(request):
    return render(request, "puskesmas/keluar.html")

def home(request):
    if request.method == "POST":
        nama = request.POST.get("nama")
        umur = request.POST.get("umur")
        nomor_hp = request.POST.get("nomor_hp")
        poli = request.POST.get("poli")

        # Simpan data ke database
        antrian = Antrian.objects.create(
            nama=nama,
            umur=umur,
            nomor_hp=nomor_hp,
            poli=poli
        )
        antrian.save()

        # Redirect ke halaman poli yang dipilih
        if poli == "anak":
            return redirect("poli-anak")
        else:
            return redirect("poli-umum")

    return render(request, "puskesmas/home.html")  # Tidak mengirimkan daftar antrian


def edit_antrian(request, id):
    antrian = get_object_or_404(Antrian, id=id)
    
    if request.method == "POST":
        # Update data berdasarkan input dari form
        antrian.nama = request.POST.get("nama")
        antrian.umur = request.POST.get("umur")
        antrian.nomor_hp = request.POST.get("nomor_hp")
        antrian.poli = request.POST.get("poli")
        antrian.save()

        # Redirect ke halaman poli yang sesuai
        if antrian.poli == "anak":
            return redirect('poli-anak')
        elif antrian.poli == "umum":
            return redirect('poli-umum')

    # Render form edit dengan data antrian
    return render(request, 'puskesmas/edit_antrian.html', {'antrian': antrian})

# Delete Antrian
def delete_antrian(request, id):
    antrian = get_object_or_404(Antrian, id=id)
    poli = antrian.poli  # Ambil jenis poli untuk redirect yang benar
    antrian.delete()

    # Redirect kembali ke poli masing-masing
    if poli == "anak":
        return redirect('poli-anak')
    else:
        return redirect('poli-umum')

# Eksekusi Antrian
def eksekusi_antrian(request, id):
    antrian = get_object_or_404(Antrian, id=id)
    poli = antrian.poli  # Ambil jenis poli untuk redirect yang benar
    # Menandai antrian sebagai selesai
    antrian.selesai = True
    antrian.save()

    # Redirect kembali ke poli masing-masing
    if poli == "anak":
        return redirect('poli-anak')
    else:
        return redirect('poli-umum')

def poli_anak(request):
    # Menampilkan antrian yang belum selesai dan yang sudah selesai
    antrian_belum_selesai = Antrian.objects.filter(poli="anak", selesai=False)
    antrian_selesai = Antrian.objects.filter(poli="anak", selesai=True)
    return render(request, "puskesmas/poli_anak.html", {
        "antrian_belum_selesai": antrian_belum_selesai,
        "antrian_selesai": antrian_selesai
    })

def poli_umum(request):
    # Menampilkan antrian yang belum selesai dan yang sudah selesai
    antrian_belum_selesai = Antrian.objects.filter(poli="umum", selesai=False)
    antrian_selesai = Antrian.objects.filter(poli="umum", selesai=True)
    return render(request, "puskesmas/poli_umum.html", {
        "antrian_belum_selesai": antrian_belum_selesai,
        "antrian_selesai": antrian_selesai
    })

def semua_antrian(request):
    # Ambil semua data antrian dari database
    semua_antrian = Antrian.objects.all().order_by('poli', 'selesai', 'id')  # Urutkan berdasarkan poli, status selesai, dan id
    return render(request, "puskesmas/semua_antrian.html", {"semua_antrian": semua_antrian})
