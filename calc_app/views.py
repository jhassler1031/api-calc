from django.shortcuts import render

from rest_framework import generics

from calc_app.permissions import IsOwnerOrReadOnly
from calc_app.models import Operation
from calc_app.serializers import OperationSerializer

# Create your views here.
