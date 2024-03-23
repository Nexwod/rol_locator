from django.urls import path
from locator.views import home_view, all_points_view, Rol_register_view, Rol_register_update_view, details_view, search_view, search_items_view

app_name = 'locator'
urlpatterns = [
    path('', home_view, name='home'),
    path('Rol_register', Rol_register_view, name='Rol_register'),
    path('Rol_update/<int:id>', Rol_register_update_view, name='Rol_update'),
    path('all_points', all_points_view, name='all_points'),
    path('search', search_view, name='search'),
    path('search_items', search_items_view, name='search_items'),
    path('details/<int:my_id>', details_view, name='details'),
]

