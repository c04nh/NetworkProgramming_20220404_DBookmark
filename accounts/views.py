from django.shortcuts import render

from accounts.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            profile = form.save()
            return render(request, 'accounts/register_done.html', {'profile': profile})
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})