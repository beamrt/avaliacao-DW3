from django.urls import path

from core.views import (
    login,
    logout,
    home,

    criar_link,
    listar_links,
    editar_link,
    deletar_link
)


urlpatterns = [

    path('login/', login, name='login'),

    path('logout/', logout, name='logout'),

    path('index/', home, name='index'),

    path('', home, name='home'),



    path(
        'links/',
        listar_links,
        name='listar_links'
    ),

    path(
        'links/criar/',
        criar_link,
        name='criar_link'
    ),

    path(
        'links/editar/<int:id>/',
        editar_link,
        name='editar_link'
    ),

    path(
        'links/deletar/<int:id>/',
        deletar_link,
        name='deletar_link'
    ),
]