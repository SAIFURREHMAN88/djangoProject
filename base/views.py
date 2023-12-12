from django.shortcuts import render
from django.http import JsonResponse
import subprocess
import os


def home(request):
    return render(request, 'index.html')

def your_view(request):
    return render(request, 'your_template_file.html')