from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(http_method_names=["GET", "POST"])
def homepage(request:Request):
    response={"message": "Hello World!"}
    return Response(data=response, status=status.HTTP_200_OK)
