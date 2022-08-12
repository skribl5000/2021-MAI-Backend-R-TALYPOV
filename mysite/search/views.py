import abc

from django.http import HttpResponse
from elasticsearch_dsl import Q
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView

from recipes.documents import RecipeDocument
# from books.serializers import BookSerializer
from recipes.serializers import RecipeSerializer
# from genres.serializers import GenreSerializer
#
#
class SearchRecipes(APIView):
    serializer_class = RecipeSerializer
    document_class = RecipeDocument

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q)
            response = search.execute()
            for hit in response.hits:
                print(hit.recipe_description)
            return HttpResponse(response.hits)
            # return HttpResponse('<html>Hello world</html>')
        except Exception as e:
            return HttpResponse(e, status=500)

    def generate_q_expression(self, query):
        return Q(
                'multi_match', query=query,
                fields=[
                    'recipe_name',
                ], fuzziness='auto')
