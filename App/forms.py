from django import forms

class ImportarCSVForm(forms.Form):
    archivo_csv = forms.FileField(label='Archivo CSV')

    def clean_archivo_csv(self):
        archivo = self.cleaned_data['archivo_csv']
        # Aquí puedes realizar validaciones adicionales en el archivo CSV si es necesario
        return archivo
