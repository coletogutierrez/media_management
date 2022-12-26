from django.db.models import Q
#from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector


from django.shortcuts import render

from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_protect

        
import random







def index_view(request):

    if request.method == 'GET':
        pass

    datos = {
        'numbers': range(40),

    }

    return render(request, 'home/index.html', datos)










