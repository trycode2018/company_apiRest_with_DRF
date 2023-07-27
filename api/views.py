
""" 
    #from rest_framework import status
        - Modulo para apresentar o estado do request
    #from rest_framework.response import Response
        - Modulo para retornar o response do verbo HTTP requisitado
    #from rest_framework.decorators import action
        - Modulo para customizar uma accao da viewset(Modelo)

"""

from rest_framework import viewsets, mixins
from .models import Company
from .serializers import CompanySerializer

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
