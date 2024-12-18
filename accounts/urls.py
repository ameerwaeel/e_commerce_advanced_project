from . import views
from django.urls import path
app_name='accounts'
urlpatterns = [
    path('register',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('activate/<uidb64>/<token>/',views.activate,name="activate"),

]
