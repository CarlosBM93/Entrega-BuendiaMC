
from django.contrib import admin
from django.urls import include, path
from App_Entrega.urls import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App-Entrega/', include('App_Entrega.urls')),

]
