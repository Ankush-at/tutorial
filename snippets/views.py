from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework.decorators import action

class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer



# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })	

class SnippetViewSet(viewsets.ModelViewSet):
	queryset = Snippet.objects.all()
	serializer_class = SnippetSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

	@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
	
	def highlight(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)



	


# class SnippetHighlight(generics.GenericAPIView):
# 	queryset = Snippet.objects.all()
# 	renderer_classes = [renderers.StaticHTMLRenderer]

# 	def get(self,request):
# 		snippet = self.get_object()
# 		return Response(snippet.highlighted)

# @api_view(['GET'])
# def api_root(request,format=None):
# 	return Response({
# 		'users':reverse('user-list',request=request,format=format),
# 		'snippets':reverse('snippet-list',request=request,format=format),

# 		})


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class SnippetList(generics.ListCreateAPIView):

# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# 	def perform_create(self, serializer):
# 	    serializer.save(owner=self.request.user)

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

# 	queryset = Snippet.objects.all()
# 	serializer_class = SnippetSerializer
# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
