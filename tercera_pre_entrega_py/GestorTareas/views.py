from django.shortcuts import render
from GestorTareas.models import Task,User,TaskDescription
from GestorTareas.forms import TareaFormulario,BuscarTarea,CargarUsuario

def inicio(request):

    return render(request, "GestorTareas/index.html") #Se renderiza el index.html (Asi con cada una de las views, se renderiza su respectivo html)

def tareas(request):

    if request.method == 'POST':
      
        Formulario = TareaFormulario(request.POST)

        if Formulario.is_valid():
            informacion = Formulario.cleaned_data
            tarea = Task(name=informacion["tarea"], deliverydate=informacion["fecha"],status=informacion["estado"])
            tarea.save()

            descripcion = informacion.get("descripcion", "")  # Obtén la descripción del formulario
            if descripcion:  # Verifica si se proporcionó una descripción
                task_description = TaskDescription(task=tarea, description=descripcion)
                task_description.save()



            return render(request, "GestorTareas/index.html")
    else:
        Formulario = TareaFormulario()
 
    return render(request, "GestorTareas/tareas.html", {"Formulario": Formulario})

def busquedatareas(request):
    if request.method == 'POST':
      
        Formulario = BuscarTarea(request.POST)

        if Formulario.is_valid():
            informacion = Formulario.cleaned_data #Se hace un cleaned_data

            tareas = Task.objects.filter(name__icontains=informacion['tarea']) #Se utliliza el model 'task'

            descripciones = TaskDescription.objects.filter(task__in=tareas) #Se utiliza el model 'taskdescription'



            return render(request, "GestorTareas/mostrar.html",{'tareas': tareas, 'descripciones': descripciones}) #Se genera el diccionario con key-value para tareas y descripciones
    else:
        Formulario = BuscarTarea() 


    return render(request, "GestorTareas/tareashist.html",{"Formulario": Formulario})

def usuarios(request):
     if request.method == 'POST':
      
        Formulario = CargarUsuario(request.POST)

        if Formulario.is_valid():
            informacion = Formulario.cleaned_data
            usuario = User(name=informacion["nombre"], lastname=informacion["apellido"],email=informacion["email"])
            usuario.save()
            return render(request, "GestorTareas/index.html")
     else:
        Formulario = CargarUsuario()

    
     return render(request, "GestorTareas/usuarios.html", {"Formulario": Formulario})

def about(request):

    return render(request, "GestorTareas/about.html")

def mostrar(request):
    pass




# Create your views here.
