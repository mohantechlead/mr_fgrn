from django.shortcuts import render


def mr_base(request):
    return render(request, 'mr_base.html')