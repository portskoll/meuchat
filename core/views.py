from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})


def frontpage(request):
    return render(request, 'core/frontpage.html')
