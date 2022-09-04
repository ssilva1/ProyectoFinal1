from django.contrib import admin
from django.urls import path, include
#from AppLavatres import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppLavatres', include('AppLavatres.urls'))
]

""""
urlpatterns = [
    path('AppLavatres/', include('AppLavatres.urls')),
]
"""

"""path('',views.inicio),
path('vehiculos',views.vehiculos),
path('indumentarias',views.indumentarias),
path('animales',views.animales),"""





