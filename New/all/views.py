from django.shortcuts import render
from .models import agent, orders,product
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
import random
from .forms import agent_forms, product_forms
def all(request):
    agent_view = agent.objects.all()
    order_view = orders.objects.all()
    product_view = product.objects.all()
    product_form = product_forms
    agent_produ = agent_forms
    return render(request, 'form.html',{'agent':agent_view, 'order':order_view,'agent_f':agent_produ,'product_f':product_form,'product':product_view})

class ser_agent(serializers.ModelSerializer):
    class Meta:
        model = agent
        fields = ['id','name','tel_num']

class agent_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = agent.objects.all()

        serlized_agent = ser_agent(all_agent, many=True)
        return Response(serlized_agent.data)

class ser_product(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['id','charecter','image','narx','name']

class product_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = product.objects.all()
        serlized_agent = ser_product(all_agent, many=True)
        return Response(serlized_agent.data)
