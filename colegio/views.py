from django.shortcuts import render

# Create your views here.
def asignacion_new(request):
    if request.method == "POST":
        form = AsignacionForm(request.POST)
        if form.is_valid():
            consulta = Consulta.objects.create(idAnimal=form.cleaned_data['idAnimal'], sintomas=form.cleaned_data['sintomas'], observaciones=form.cleaned_data['observaciones'], diagnostico = form.cleaned_data['diagnostico'], fechaConsulta = form.cleaned_data['fechaConsulta'])
            for medicina_id in request.POST.getlist('receta'):
                medicacion = Medicacion(medicina_id=medicina_id, consulta_id = consulta.id)
                medicacion.save()
            return redirect('lista_consultas')
            
    else:
        form = ConsultaForm()

    return render(request, 'persona/consulta_new.html',{'form':form})