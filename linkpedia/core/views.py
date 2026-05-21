from django.shortcuts import render, redirect, get_object_or_404

from core.forms import LoginForm, LinkForm
from core.models import LinkModel

from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

def login(request):
    if request.user.id is not None:
        return redirect("home")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            auth_login(request, form.user)
            return redirect("home")
        context = {'acesso_negado': True}
        return render(request, 'login.html', {'form':form})
    return render(request, 'login.html', {'form':LoginForm()})

        
def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return render(request, 'logout.html')
    return redirect("home")


@login_required
def home(request):
    context = {}
    return render(request, 'index.html', context)


@login_required
def criar_link(request):

    form = LinkForm(request.POST or None)

    if form.is_valid():

        form.save()

        return redirect('listar_links')
    
    return render(request, 'criar.html', {
        'form': form
    })


@login_required
def listar_links(request):

    links = LinkModel.objects.all()

    return render(request, 'listar.html', {
        'links': links
    })


@login_required
def editar_link(request, id):

    link = get_object_or_404(
        LinkModel,
        id=id
    )

    form = LinkForm(
        request.POST or None,
        instance=link
    )

    if form.is_valid():

        form.save()

        return redirect('listar_links')

    return render(request, 'editar.html', {
        'form': form
    })


@login_required
def deletar_link(request, id):

    link = get_object_or_404(
        LinkModel,
        id=id
    )

    link.delete()

    return redirect('listar_links')