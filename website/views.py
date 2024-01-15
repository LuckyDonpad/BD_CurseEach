from django.shortcuts import render


def auth(request):
    return render(request, template_name='auth/auth.html')


def add_client(request):
    return render(request, template_name='add_client/add_client.html')


def add_worker(request):
    return render(request, template_name='add_worker/add_worker.html')


def backup(request):
    return render(request, template_name='backup/backup.html')


def create_task(request):
    return render(request, template_name='create_task/create_task.html')


def manage_tasks(request):
    return render(request, template_name='manage_tasks/manage_tasks.html')


def failed_tasks(request):
    return render(request, template_name='current_tasks/current_tasks.html')


def view_client(request):
    return render(request, template_name='view_client/view_client.html')


def view_worker(request):
    return render(request, template_name='view_worker/view_worker.html')
