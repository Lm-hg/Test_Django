from django.shortcuts import render
from main.models import Articles #on import notre models


#on affiche les articles
def index(request):
        Article=Articles.objects.all()
        return render(request,"main/index.html",{
                "Article":Article
        })


#un plus, on va créer


# Create your views here.
