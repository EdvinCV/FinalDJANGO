from django.contrib import admin
from .models import Materia, Grado, Asignacion, GradoAdmin, MateriaAdmin

admin.site.register(Grado, GradoAdmin)
admin.site.register(Materia, MateriaAdmin)