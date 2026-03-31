# from rest_framework import generics, mixins, status
# from rest_framework.decorators import api_view
# from rest_framework.request import Request
# from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.serializers import PostSerializer

from .models import Post

# @api_view(http_method_names=["GET", "POST"])
# def homepage(request:Request):
#     response={"message": "Hello World!"}
#     return Response(data=response, status=status.HTTP_200_OK)

# class PostListCreateView(
#     generics.GenericAPIView, 
#     mixins.ListModelMixin, 
#     mixins.CreateModelMixin):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request:Request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request:Request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class PostRetrieveUpdateDeleteView(
#     generics.GenericAPIView,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin):

#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
    
#     def get(self, request:Request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request:Request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request:Request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class PostViewset(viewsets.ModelViewSet):
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Връща само постовете на текущия user
        return Post.objects.filter(author=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

