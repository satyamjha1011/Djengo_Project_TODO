from . import views
from django.contrib import admin
from django.urls import path ,include



admin.site.site_header = "TODO Application admin login"
admin.site.site_title = "Welcome to Admin' Login Page"
admin.site.index_title = "Welcome to the Admin Dashboard"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signup),
    path('loginn/', views.loginn),
    path('todopage', views.todo),
    path('delete_todo/<int:srno>', views.delete_todo),
    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),
    path('signout/', views.signout, name='signout'),
    
]
