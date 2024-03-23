from django import forms

from .models import RolPoints

REGION_CHOICE = (('Region 1', 'Amansea - School gate'), 'Region 2 (Inside Unizik and Environ)', 'Region 3 (School gate - Second Market)',  'Region 4 (Second Market - First Market)',  'Region 5 (First Market - Aroma)',  'Region 6 (Aroma - Tempsite)',  'Region 7 (Tempsite - Okpuno and Environ)', 'Others' )


class RolForm(forms.ModelForm):
    class Meta:
        model = RolPoints
        fields = [
            'region',
            'address',
            'image',
            'co_ordinator',
            'contact',
            'date_time'
        ]
        widgets = {
            'region':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'co_ordinator':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.NumberInput(attrs={'class':'form-control'}),
            'date_time':forms.TextInput(attrs={'class':'form-control'})
            
        }

class RolSearchForm(forms.Form):
    address = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}), label='Address', max_length=100, required=True)
    co_ordinator = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Co_ordinator (optional)', max_length=50, required=False)
    region = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Region (optional)', max_length=50, required=False)