from django.urls import path
from .views import *
from wishlist.views import register
from wishlist.views import login_user
from wishlist.views import logout_user
from wishlist.views import show_wishlist_ajax
from wishlist.views import submit_ajax
app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name= 'show_xml'), 
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('ajax/submit/', submit_ajax, name='submit_ajax'),
]