from django import forms
from .models import Grado, Materia, Asignacion

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ('nombre','seccion','aula','materias',)

    def __init__ (self, *args, **kwargs):
        super(AsignacionForm, self).__init__(*args, **kwargs)
        self.fields["materias"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materias"].queryset = Materia.objects.all()