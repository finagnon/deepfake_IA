"""
URL configuration for projet_IA_Fake_News project.
<<<<<<< HEAD
"""


=======

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
>>>>>>> 1409d30141be0c20f2e435566dfc041b20f24adf
from django.contrib import admin
from django.urls import path
from .  import views

urlpatterns = [
    #path("admin/", admin.site.urls),
    path("", views.fonct, name="Accueil" ),
<<<<<<< HEAD
    path('upload-image/', views.upload_image, name='upload_image')
=======
>>>>>>> 1409d30141be0c20f2e435566dfc041b20f24adf

]
