from django.urls import path, include
from main.views import *


urlpatterns = [
    path('', home, name='home'),
    path('Маҳсулот/', servicer, name='servicer'),
    path('Галлерй/', gallery, name='gallery'),
    path('Контак/ ', contact, name='contact'),
    path('Янглик/', news, name='news'),
    path('venue_pdf/<int:pk>/', venue_pdf, name='venue_pdf')

]
