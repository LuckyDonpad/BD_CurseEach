from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DeleteView

from website.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.http import JsonResponse

import csv
import json


def logout_view(request):
    logout(request)
    return redirect("auth")


def auth(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return redirect(current_tasks)
    else:
        form = LoginUserForm()
    return render(request, template_name='auth/auth.html', context={'form': form})


@login_required
@permission_required("website.change_workers")
def change_worker(request, pk):
    if request.method == 'POST':
        form = ChangeWorkerForm(request.POST, instance=Workers.objects.filter(id=pk).first())
        if form.is_valid():
            form.save()
            return redirect("/view_worker/")
    else:
        form = AddWorkerForm(instance=Workers.objects.filter(id=pk).first())
    return render(request, template_name='change_worker/change_worker.html', context={'form': form})


@login_required
@permission_required("website.add_clients")
def add_client(request):
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddClientForm()
    return render(request, template_name='add_client/add_client.html', context={'form': form})


@login_required
@permission_required("website.add_workers")
def add_worker(request):
    if request.method == 'POST':
        form = AddWorkerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddWorkerForm()
    return render(request, template_name='add_worker/add_worker.html', context={'form': form})


@login_required
def backup(request):
    tables = ["Tasks", "Clients", "Workers"]
    formats = ["csv", "json"]
    if request.GET.get("export"):
        smth = request.GET["export"].split(" ")
        format = smth[0]
        table = smth[1]
        if table == "Tasks":
            data = Tasks.objects.all()
        elif table == "Clients":
            data = Clients.objects.all()
        elif table == "Workers":
            data = Workers.objects.all()

        if format == "csv":
            headers = list(data.values())[0].keys()
            data = list(data.values_list())
            return export_csv(request, data, headers, table)
        elif format == "json":
            return export_json(request, data.values(), table)
    return render(request, template_name='backup/backup.html', context={'tables': tables, "formats": formats})


@login_required
@permission_required("website.add_tasks")
def create_task(request):
    if request.method == 'POST':
        form = AddTasksForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AddTasksForm()
    return render(request, template_name='create_task/create_task.html', context={'form': form})


@login_required
def failed_tasks(request):
    tasks = Tasks.objects.filter(status=2)
    if request.GET.get('DeleteButton') and request.user.has_perm("website.delete_tasks"):
        Tasks.objects.filter(id=request.GET.get('DeleteButton')).delete()
        return redirect('/failed_tasks/')
    elif request.GET.get('ChangeButton'):
        return redirect(f'/change_task/{request.GET.get('ChangeButton')}')
    return render(request, template_name='failed_tasks/failed_tasks.html', context={'tasks': tasks})


@login_required
def current_tasks(request):
    tasks = Tasks.objects.filter(status=0)
    if request.GET.get('DoneButton'):
        Tasks.objects.filter(id=request.GET.get('DoneButton')).update(status=1)
        return redirect('/current_tasks/')
    elif request.GET.get('ChangeButton'):
        return redirect(f'/change_task/{request.GET.get('ChangeButton')}')
    return render(request, template_name='current_tasks/current_tasks.html', context={'tasks': tasks})


@login_required
def view_client(request):
    clients = Clients.objects.all()
    if request.GET.get('DeleteButton') and request.user.has_perm("website.delete_clients"):
        Workers.objects.filter(id=request.GET.get('DeleteButton')).delete()
        return redirect('/change_client/')
    elif request.GET.get('ChangeButton'):
        return redirect(f'/change_client/{request.GET.get('ChangeButton')}')
    return render(request, template_name='view_client/view_client.html', context={'clients': clients})


@login_required
def view_worker(request):
    workers = Workers.objects.all()
    if request.GET.get('DeleteButton') and request.user.has_perm("website.delete_workers"):
        Workers.objects.filter(id=request.GET.get('DeleteButton')).delete()
        return redirect('/view_worker/')
    elif request.GET.get('ChangeButton'):
        return redirect(f'/change_worker/{request.GET.get('ChangeButton')}')
    return render(request, template_name='view_worker/view_worker.html', context={'workers': workers})


def export_csv(request, data, headers, name):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(headers)

    for row in data:
        writer.writerow(row)

    response['Content-Disposition'] = f'attachment; filename="{name}.csv"'

    return response


def export_json(request, data, name):
    response = JsonResponse(list(data.values()), safe=False, content_type='text/json')
    response['Content-Disposition'] = f'attachment; filename="{name}.json"'
    return response


@permission_required("website.change_clients")
def change_client(request, pk):
    if request.method == 'POST':
        form = ChangeClientForm(request.POST, instance=Clients.objects.filter(id=pk).first())
        if form.is_valid():
            form.save()
            return redirect("/view_client/")
    else:
        form = AddClientForm(instance=Clients.objects.filter(id=pk).first())
    return render(request, template_name='change_client/change_client.html', context={'form': form})


@login_required
@permission_required(perm="website.change_tasks")
def change_task(request, pk):
    if request.method == 'POST':
        form = ChangeTaskForm(request.POST, instance=Tasks.objects.filter(id=pk).first())
        if form.is_valid():
            form.save()
            if Tasks.objects.filter(id=pk).first().status == 0:
                return redirect("/current_tasks/")
            else:
                return redirect("/failed_tasks/")
    else:
        form = AddTasksForm(instance=Tasks.objects.filter(id=pk).first())
    return render(request, template_name='change_task/change_task.html', context={'form': form})
