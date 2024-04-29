from django.urls import path
from .views import ContactView, home


urlpatterns = [
    path('', home, name="home"),
    path('api/contact/', ContactView.as_view(), name='contact-create'),
]
