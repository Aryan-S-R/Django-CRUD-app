from django.urls import path
from.import views

urlpatterns = [
    path("", views.home, name='home' ),
    path("add-std/", views.add_std, name='add_std'),
    path("delete-std/", views.delete_std, name='delete_std'),
    path("edit-std/", views.edit_std, name='edit_std'),
    path("do-edit-std/", views.do_edit_std, name='do_edit_std'),
]