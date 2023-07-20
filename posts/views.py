from django.views.generic import ListView
from .models import Post
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "posts.html"


# class SearchResultView(ListView):
#     model = Post
#     context_object_name = "posts"
#     template_name = "search.html"
#


# Q objects
# class SearchResultsList(ListView):
#     model = Post
#     context_object_name = "posts"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Post.objects.filter(
#             Q(title__icontains=query) | Q(body__icontains=query)
#         )


# Single Field Search
# class SearchResultsList(ListView):
#     model = Post
#     context_object_name = "posts"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Post.objects.filter(body__search=query)


# Multi Field Search
# class SearchResultsList(ListView):
#     model = Post
#     context_object_name = "posts"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Post.objects.annotate(search=SearchVector("title", "body")).filter(
#         search=query
#         )

class SearchResultView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        search_vector = SearchVector("title", "body")
        search_query = SearchQuery(query)
        return (
            Post.objects.annotate(
                search=search_vector, rank=SearchRank(search_vector, search_query)
            )
            .filter(search=search_query)
            .order_by("-rank")
        )
