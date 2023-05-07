from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def links(request):
    return render(request, "links.html")

@login_required(login_url='/login')
def admin_profile_view(request, username):
    user = User.objects.get(username=username)
    return render(request, 'admin.html', {'user': user})