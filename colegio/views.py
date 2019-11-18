from django.shortcuts import render

# Create your views here.
def asignacion_new(request):
    if request.method == "POST":
        form = AsignacionForm(request.POST)
        if form.is_valid():
            grado = Grado.objects.create(nombre=form.cleaned_data['nombre'], seccion=form.cleaned_data['seccion'], aula=form.cleaned_data['aula'])
            for materia_id in request.POST.getlist('materias'):
                asignacion = Asignacion(materia_id=materia_id, grado_id = grado.id)
                asignacion.save()
            
    else:
        form = AsignacionForm()

    return render(request, 'colegio/materia_new.html',{'form':form})