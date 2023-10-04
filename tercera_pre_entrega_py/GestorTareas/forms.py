from django import forms

#En esta seccion se configuran los formularios

class TareaFormulario(forms.Form):
    tarea = forms.CharField()
    fecha = forms.DateField()
    estado = forms.NullBooleanField(
        widget=forms.Select(choices=[
            (True, 'Completada'),
            (False, 'No Completada'), #Se establece para False, True o None diferentes palabras
            (None, 'Pendiente')
        ])
    )
    descripcion = forms.CharField(widget=forms.Textarea, required=False)  
                                  
class BuscarTarea(forms.Form):
    tarea = forms.CharField()

class CargarUsuario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()

