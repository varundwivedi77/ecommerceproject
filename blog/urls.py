
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='blogindex'),
    path('contact/',views.contact,name='blogcontact')

    
]