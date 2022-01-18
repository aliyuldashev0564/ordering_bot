from django.forms import ModelForm
from .models import agent,product


class agent_forms(ModelForm):
    class Meta(ModelForm):
        model = agent
        fields = ('name', 'tel_num', 'id')
class product_forms(ModelForm):
    class Meta(ModelForm):
        model = product
        fields = ['charecter','image','narx', 'id']
