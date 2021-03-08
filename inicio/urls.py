from django.conf.urls import url
from inicio import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^data/$', views.DataPageView.as_view(), name='data'),
    url(r'^reserva/$', views.ReservarView.as_view(), name='Reserva'),
    url(r'^vercontacto/$', views.ContactoView.as_view(), name='vercontacto'),
]
