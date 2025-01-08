from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name='home'),
    path('poli-anak/', views.poli_anak, name='poli-anak'),
    path('poli-umum/', views.poli_umum, name='poli-umum'),
    path('eksekusi/<int:id>/', views.eksekusi_antrian, name='eksekusi'),
    path('edit-antrian/<int:id>/', views.edit_antrian, name='edit_antrian'),
    path('delete-antrian/<int:id>/', views.delete_antrian, name='delete_antrian'),
    path('semua-antrian/', views.semua_antrian, name='semua-antrian'),
    path('signout/', views.signout, name='signout'),
    path('keluar/', views.logout_success, name='keluar'),
]

