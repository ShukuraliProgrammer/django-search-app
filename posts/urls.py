from django.urls import path

from .views import PostListView, SearchResultView

urlpatterns = [
    path("", PostListView.as_view(), name="all_posts"),
    path("search/", SearchResultView.as_view(), name="search_result"),
]
