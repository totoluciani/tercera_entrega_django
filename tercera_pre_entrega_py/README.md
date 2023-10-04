Este proyecto funciona con python 3.11
_________________________________________________________________

Se basa en una web para poder cargar tareas y luego poder buscarlas

Para poder iniciar el proyecto se debe estar sitaudo dentro de:

.\tercera_pre_entrega\tercera_pre_entrega_py

y luego se debe ejecutar el comando 

py manage.py runserver

http://127.0.0.1:8000/GestorTareas para ingresar a la App

________________________________________________________________________________________
dentro de la web, hay varios apartados en la 'navbar', siendo 'Tareas' el que cuenta con la funcion para poder cargar tareas... Este formulario se encarga de cargar datos a 2 de los 3 models existentes en la App.. Estos datos se pueden observar yendo al apartado 'Busqueda de tareas' y escribiendo alli el nombre de la tarea.
Para cargar usuarios se debe ingresar al apartado 'Usuario'..

Todos los datos pueden ser visibles dentro del admin de Django, las crendenciales son:

user = toto
pass = rstursto

Hay 3 models, uno para usuarios, otro para las tareas y otro para descripcion de las tareas, siendo este ultimo dependeinte entre si con el model 'Task'
