from django.shortcuts import render
from wiki.models import Category, Page
# Create your views here.
def wiki(request):
    categories = Category.objects.order_by('-likes')
    context = {'categories':categories}
    return render(request, 'wiki/wiki.html',context)