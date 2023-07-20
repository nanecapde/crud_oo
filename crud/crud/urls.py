from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    path('',views.admin, name="admin"),
    path('cadastro/',views.cadastro,name="cadastro"),
    path('deletar/', views.deletar, name="deletar_usuario"),
    path('aviso/', views.aviso, name="aviso_usuario"),
    path('listagem/',views.listagem, name="lista_usuarios"),
    path('atualizar/',views.atualiza, name="atualiza_usuario"),
    path('confirmacao/',views.confirma, name="tela_confirma"),
    #path('erro/',views.erro, name="erro_usuario"),
    path('usuarios/',views.usuarios,name="listagem_usuarios")
]
