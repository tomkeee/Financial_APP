from django import forms
from .models import Instrument,Stock
from django.forms import ModelForm, widgets

class TickerForm(forms.Form):
    ticker=forms.CharField(required=False,max_length=100,widget=forms.TextInput(attrs={"class":"form-control mr-sm-2","placeholder":"AAPL"}))

######################################## In the future ######################################################################
# choices=Region.objects.all().values_list('name','name')
# choices_list = []
# for item in choices:
# choice_list.append(item)
#############################################################################################################################


class InstrumentForm(ModelForm):
    class Meta:
        model=Instrument
        fields =['name','price','quantity','region','stake']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control mb-2'}),
            'price': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'quantity': forms.NumberInput(attrs={'class':'form-control mb-2'}),
            'region':forms.Select(attrs={'class':'form-control mb-2'}),
            'stake':forms.Select(attrs={'class':'form-control mb-4'}),
        }

class BarTypeForm(forms.Form):

    CHART_CHOICES=(
    ('#1','Bar chart'),
    ('#2','Pie chart'),
    ('#3','Line chart'),
    )
    
    chart_type=forms.ChoiceField(choices=CHART_CHOICES,label="Select Chart Type")

class StockForm(ModelForm):
    class Meta:
        model=Stock
        fields=['ticker']
        widgets={
            'ticker':forms.TextInput(attrs={'class':'form-control mr-2'})
        }

