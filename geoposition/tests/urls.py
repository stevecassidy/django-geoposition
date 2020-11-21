from django.urls import include, path
from django.contrib import admin
import example 

admin.autodiscover()

urlpatterns = [
    #path('', example.views.poi_list),
    path('admin/', admin.site.urls),
]
