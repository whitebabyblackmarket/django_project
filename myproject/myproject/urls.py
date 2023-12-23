from django.urls import path
from replicate_integration import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', views.run_stable_diffusion, name='predict'),
    # Remove or comment out the paths that serve HTML templates
    # path('home/', views.home, name='home'),
    # path('', views.index, name='index'),
]

