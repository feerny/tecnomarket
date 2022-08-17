

from django import forms
from .models import Contactos,Producto

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model=Contactos
        #fields = ["nombre","correo","tipo_consulta","mensaje","avisos"]
        fields = '__all__'
        
        
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model=Producto
        fields = '__all__'
        
        widgets = {
            "fecha_fabricacion":forms.SelectDateWidget()
        }