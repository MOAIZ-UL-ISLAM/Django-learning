from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('', views.profile_list,name='profilelist'),
    path('<int:profile_id>',views.profile_id,name='profile_id'),
    path('contact',views.contactView,name='contact'),
    path('new_profile',views.NewProfileView,name='new_profile')
]
