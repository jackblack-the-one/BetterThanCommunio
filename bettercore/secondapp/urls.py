from django.urls import path
from . import views
from .views import CoolUsersAPI


urlpatterns = [
         path('coolusers', CoolUsersAPI.as_view({'get':'list', 'post':'create', 'put':'update', 'delete':'destroy'}), name='cool'),
]
