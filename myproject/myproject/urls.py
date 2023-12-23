from django.urls import path
from replicate_integration import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('predict/', views.run_stable_diffusion, name='predict'),
    path('', views.index, name='index'),
]
