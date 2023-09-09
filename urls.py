from django.urls import path
from . views import user_reg,gen_message,message

urlpatterns = [
    path('', message, name='message'),
    path('gen_message/', gen_message, name='message'),
    path('users/', user_reg, name='user_reg'),
]

