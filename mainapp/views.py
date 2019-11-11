from django.shortcuts import render, get_object_or_404
from .models import Tutoriallac
from django.views import generic
import io
from django.http import FileResponse, HttpResponseRedirect, HttpResponse

# Create your views here.


class detailViewLac(generic.DetailView):
    model = Tutoriallac
    template_name = 'detail.html'
    context_object_name = 'tutorial_object_lac'

def index_lac(request):
    return render(request=request,
                  template_name='index.html',
                  context=None)

def homepage_lac(request):
    tutoriales = Tutoriallac.objects.all()
    return render(request,
                  'homepage.html',
                  {'tutoriales':tutoriales})
