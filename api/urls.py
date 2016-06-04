from django.conf.urls import url
from api import views
urlpatterns = [
    url(r'^updatelocation/', views.updatelocation),
]