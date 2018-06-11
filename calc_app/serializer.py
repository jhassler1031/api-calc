from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from calc_app.models import Operation

class OperationSerializer(ModelSerializer):

    class Meta:
        model = Operation
        fields = ["operand_one", "operator", "operand_two", "result", "owner"]
        read_only_fields = ["owner"]
