from django.contrib import admin
from .models import Post #importa o model post que criamos

admin.site.register(Post) #registra o post para que fique visivel na pag de adm
