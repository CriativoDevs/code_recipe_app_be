from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer
from rest_framework import viewsets, mixins
from rest_framework.response import Response


class BlogApiView(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    # Usamos o genericviewset por ser o mais simples de se implementar,
    # mas depende da necessidade.
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "slug"
    # pode ser usado qualquer campo, mas decidi usar esse.


class CategoryApiView(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = "id"


# Aqui fazermos o request, por isso o viewset.ViewSet
class CategoryPostApiView(viewsets.ViewSet):
    # Aqui vamos pesquisar por todos os dados da categoria, exemplo,
    # drinks deveria ser apenas da categoria drinks
    # A função criada aqui irá tratar de todos os dados de uma única categoria
    def retrieve(self, request, pk=None):
        queryset = Blog.objects.filter(
            category=pk
        )  # irá verificar se há match com o pk dos objetos e categoria
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)


class PopularPostApiView(viewsets.ViewSet):
    def list(self, request, pk=None):
        queryset = Blog.objects.filter(post_label__iexact="POPULAR").order_by("-id")[:4]
        # Será mostrado apenas os 4 mais novos e em ordem de inserção
        serializer = BlogSerializer(queryset, many=True)
        return Response(serializer.data)
