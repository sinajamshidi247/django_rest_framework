
from django.contrib import admin
from django.urls import path , include
from rest_framework.authtoken import views
from .api_urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls',namespace='home')),
    path('api-token-auth/', views.obtain_auth_token),#method must be post
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))

]
