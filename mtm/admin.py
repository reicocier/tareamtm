from django.contrib import admin
from .models import Actor
from .models import Pelicula
from .models import Actuacion
#from .models import ActuacionInLine
#from .models import ActorAdmin
#from .models import PeliculaAdmin


admin.site.register(Actor)
admin.site.register(Pelicula)
admin.site.register(Actuacion)
#admin.site.register(ActuacionInLine)
#admin.site.register(ActorAdmin)
#admin.site.register(PeliculaAdmin)