from django.urls import path
from replicate_integration import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('run_face_swap/', views.run_face_swap, name='run_face_swap'),
    # If you're not using the stable diffusion model anymore, you can comment out or remove the following line
    # path('predict/', views.run_stable_diffusion, name='predict'),
    # Remove or comment out the paths that serve HTML templates
    # path('home/', views.home, name='home'),
    # path('', views.index, name='index'),
]

