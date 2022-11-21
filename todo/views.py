from django.shortcuts import render

# Create your views here.

def today_page_view(request):
    return render(request, 'todo/today.html')