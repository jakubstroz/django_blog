from django.urls import path
from .views import about_us, contact_view


app_name = 'common'

urlpatterns = [
    path('contact/', contact_view, name='contact_view'),
    path('about/', about_us,name='about_us')
]