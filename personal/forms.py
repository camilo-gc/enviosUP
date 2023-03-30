from django import forms
from personal.models import Cliente, Persona

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [  
            'td_id',
            'per_documento',
            'per_nombre', 
            'per_apellido',
            'per_fecha_naci', 
            'per_email',
            'per_contrasena', 
            'per_telefono',
            'per_celular', 
            'per_direccion',
        ]
        labels = {
            'td_id' : 'Tipo de Documento',
            'per_documento' : 'Número de Documento',
            'per_nombre' : 'Nombres', 
            'per_apellido' : 'Apellidos',
            'per_fecha_naci' : 'Fecha de Nacimiento', 
            'per_email' : 'Correo Electrónico',
            'per_contrasena' : 'Contraseña', 
            'per_celular' : 'Número de Celular',
            'per_telefono' : 'Número de Teléfono', 
            'per_direccion' : 'Dirección',
        }
        widgets = {
            'td_id' : forms.Select(attrs={'class':'form-control'}),
            'per_documento' : forms.TextInput(attrs={'class':'form-control'}),
            'per_nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'per_apellido' : forms.TextInput(attrs={'class':'form-control'}), 
            'per_fecha_naci' : forms.DateInput(format='%d/%m/%Y', attrs={'class': 'form-control datepicker'}),  
            'per_email' : forms.EmailInput(attrs={'class':'form-control'}), 
            'per_contrasena' : forms.PasswordInput(attrs={'class':'form-control'}),  
            'per_celular' : forms.TextInput(attrs={'class':'form-control'}),
            'per_telefono' : forms.TextInput(attrs={'class':'form-control'}), 
            'per_direccion' : forms.TextInput(attrs={'class':'form-control'}),
        }


    