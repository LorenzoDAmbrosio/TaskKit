from http.client import HTTPResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from TaskKit.tasks.forms import *
from TaskKit.tasks.models import *


def page_index(request):
    return render(request, 'pages/index.html')
def page_register_account(request):
    return render(request, 'pages/register_account.html')

@login_required
def page_community_create(request):
    users= User.objects.exclude(id=request.user.id).all()
    return render(request, 'pages/community_create.html',{'users': users})


def account_create(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken')
                return redirect('register_account')

            # Check if the email is already in use
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already in use')
                return redirect('register_account')

            # Create the user account
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('account')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register_account')

    return redirect('register_account')

def page_explore(request):
    from django.db.models import Q
    if not request.user.is_authenticated:
        communities = Community.objects \
            .filter(is_public=1)
    else:
        communities = Community.objects \
            .filter(is_public=1)
        communities.union(Community.objects \
                          .filter(members__in=[request.user]))
    return render(request, 'pages/explore.html', {'communities': communities})


def page_communities(request):
    if not request.user:
        return render(request, 'pages/index.html')
    communities = Community.objects \
        .filter(members__in=[request.user])\
        .order_by('-creation_date')
    return render(request, 'pages/communities.html', {'communities': communities})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('communities')  # Replace 'home' with the URL name of your home page
        else:
            # Handle invalid login credentials here
            pass

    return render(request, 'pages/index.html')


def community_detail(request, community_id, page):
    community = Community.objects.get(id=community_id)
    users = User.objects.all

    return render(request, 'pages/community_detail.html',
                  {'community': community, 'page': page, 'users': users})
def project_detail(request, project_id, page):
    project = get_object_or_404(Project, id=project_id)

    return render(request, 'pages/project_detail.html',
                  {'project': project })

@login_required
def account_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'pages/account.html', context)


@login_required
def edit_account_view(request):
    if request.method == 'POST':
        user = request.user
        new_username = request.POST.get('username')
        new_email = request.POST.get('email')

        # Update user info
        user.username = new_username
        user.email = new_email
        user.save()

        return redirect('account')

    return render(request, 'account')


@login_required
def delete_account_view(request):
    user = request.user

    # Delete the user account
    user.delete()

    # Logout the user after deleting the account
    logout(request)

    return redirect('index')




@login_required
def account_edit(request):
    user = request.user

    if request.method == 'POST':
        form = AccountEditForm(request.POST, instance=user)

        if form.is_valid():
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if not password and not confirm_password:
                form.cleaned_data['password'] = user.password
                form.cleaned_data['confirm_password'] = user.password
            elif password != confirm_password:
                messages.error(request, 'Passwords do not match')
                return render(request, 'account', {'form': form})

            form.save()
            messages.success(request, 'Account details updated successfully')
    else:
        form = AccountEditForm(instance=user)

    return render(request, 'account', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # Replace 'home' with the appropriate URL name for your home page

@login_required
def task_update(request, task_id=None, project_id=None, page='community'):
    task = None
    if task_id:
        task = get_object_or_404(Task, id=task_id)
    if project_id:
        project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    if page == 'community':
        return redirect('community_detail', community_id=project.community.id, page='communities')
    elif page == 'project':
        return redirect('project_detail', project_id=project.id, page=page)
@login_required
def task_create(request, project_id):
    if project_id:
        project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('community_detail', community_id=project.community.id, page='communities')
@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('community_detail', community_id=task.project.community.id, page='communities')

@login_required
def project_create(request, community_id):
    if community_id:
        community = get_object_or_404(Community, id=community_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('community_detail', community_id=community.id, page='communities')
@login_required
def project_update(request, community_id=None, project_id=None):
    if community_id:
        community = get_object_or_404(Community, id=community_id)
    if project_id:
        project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()

    return redirect('community_detail', community_id=community.id, page='communities')

@login_required
def project_delete(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return redirect('community_detail', community_id=project.community.id, page='communities')

@login_required
def status_create(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect('community_detail', community_id=project.community.id, page='communities')

@login_required
def status_delete(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    status.delete()
    return redirect('community_detail', community_id=status.project.community.id, page='communities')

@login_required
def community_create(request):

    if request.method != 'POST':
        return redirect('community_creation')

    form = CommunityForm(request.POST)
    if not form.is_valid():
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{field}: {error}')
        return redirect('community_creation')

    form.founder_user = request.user
    form.save()
    messages.success(request, 'Community created successfully.')

    return redirect('communities')
@login_required
def community_join(request, community_id=None):
    if community_id:
        community = get_object_or_404(Community, id=community_id)

    community.members.add(request.user)
    if request.method == 'POST':
        form = CommunityForm(request.POST, instance=community)
        if form.is_valid():
            form.save()

    return redirect('community_detail', community_id=community.id, page='communities')
@login_required
def community_update(request, community_id=None):
    if community_id:
        community = get_object_or_404(Community, id=community_id)

    if request.method != 'POST':
        return redirect('community_creation')

    form = CommunityForm(request.POST, instance=community)
    if not form.is_valid():
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f'{field}: {error}')

    form.save()
    messages.success(request, 'Community updated successfully.')

    return redirect('community_detail', community_id=community.id, page='communities')
