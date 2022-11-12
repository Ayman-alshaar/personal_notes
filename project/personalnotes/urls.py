from django.urls import path,include
from . import views
from . import api
urlpatterns = [
    
    path('api/note',api.work_on_note,name='joblistapi')
    #path('', admin.site.urls),
]
