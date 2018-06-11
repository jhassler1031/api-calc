import requests

operations_url = "http://localhost:8000/operations/"

operand_one = input("Operand One: ")
operand_two = input("Operand Two: ")
operator = input("Operator: ")
owner = input("Owner ID: ")

request.POST(operations_url, "operand_one": operand_one, "operand_two": operand_two, "operator": operator, "owner": owner)
