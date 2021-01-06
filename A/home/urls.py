from django.urls import path
from. import views


app_name = 'home'

urlpatterns = [
    path('one/',views.home,name ='home_app'),
    path('persons/',views.persons,name ='persons'),
    path('person/<str:name>',views.person,name ='singel_person'),
    path('person_create/',views.person_create,name ='person_create'),



]