from django.shortcuts import render
from .forms import VisitForm


def main(request):
    form = VisitForm()
    return render(request, 'main.html', {'form': form})