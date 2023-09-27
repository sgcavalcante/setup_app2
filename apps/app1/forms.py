from django import forms
from .models import Subestacoes

class SubestaoesForm(forms.ModelForm):
    class Meta:
        model = Subestacoes
        fields = ['subestacao','nivel_de_tensao','descricao']