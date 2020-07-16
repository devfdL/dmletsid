from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path("register/", views.register, name="register"),
    path('',views.index, name='home'),
    path('post/<slugInput>', views.singlePost),
    path('berita/',views.berita, name='berita'),
    path('berita/<slugInput>', views.brtsinglePost),
    path('kultur/',views.kultur, name='kultur'),
    path('kultur/<slugInput>', views.kltrsinglePost),
]
