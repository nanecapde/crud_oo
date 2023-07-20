from django.shortcuts import render
from .models import Usuario

def cadastro(request):
    adm = request.POST.get('adm')
    senha = request.POST.get('senha')
    
    if senha == 'admin' and adm == 'admin':
        return render(request, 'usuarios/cadastro.html')
    else:
        return render(request, 'usuarios/adimin.html')

def usuarios(request):
    #salva os dados da tela no banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')

    try:
        aux = Usuario.objects.get(nome = novo_usuario.nome)
        return render(request,'usuarios/erro.html')
    except Usuario.DoesNotExist:

        novo_usuario.save()

        #exibir todos os usuarios ja cadasrados em uma nova pagina
        usuarios ={
                'usuarios': Usuario.objects.all()        
            }

        #retorna os dados para a pagina de listagem de usuarios
        return render(request,'usuarios/usuarios.html',usuarios)

def listagem(request):

    usuarios ={
            'usuarios': Usuario.objects.all()        
        }

    return render(request,'usuarios/listausuarios.html',usuarios)

def deletar(request):
    return render(request,'usuarios/deletar.html')

def aviso(request):
    id_user = request.POST.get('id_usr')

    usuario = Usuario.objects.get(id_usuario = id_user)
    usuario.delete()

    return render(request,'usuarios/aviso.html')

def atualiza(request):
    return render(request,'usuarios/dados.html')

def confirma(request):
    id_user = request.POST.get('id_usr')
    usuario_atualiza = Usuario.objects.get(id_usuario = id_user)

    usuario_atualiza.nome = request.POST.get('novo_nome')
    usuario_atualiza.idade = request.POST.get('nova_idade')
    usuario_atualiza.save()

    return render(request,'usuarios/confirma.html')

def admin(request):
    return render(request,'usuarios/adimin.html')
