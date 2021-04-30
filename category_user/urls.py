from django.urls import path

from category_user.views import CategoryListView, TVShowListView, TVShowDetailView

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryListView.as_view()),
    path('shows/', TVShowListView.as_view()),
    path('shows/<int:pk>/', TVShowDetailView.as_view()),
]