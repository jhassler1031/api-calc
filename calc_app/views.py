from django.shortcuts import render

from rest_framework import generics

from calc_app.permissions import IsOwnerOrReadOnly
from calc_app.models import Operation
from calc_app.serializer import OperationSerializer

# Create your views here.
class OperationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
        data = serializer.validated_data
        calc_result = 0
        operand_one = data["operand_one"]
        operand_two = data["operand_two"]
        operator = data["operator"]

        if operator == "+":
            calc_result = operand_one + operand_two
        elif operator == "-":
            calc_result = operand_one - operand_two
        elif operator == "*":
            calc_result = operand_one * operand_two
        elif operator == "/":
            calc_result = operand_one / operand_two

        serializer.save(result = calc_result)


class OperationRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer
