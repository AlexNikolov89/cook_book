
from django.urls import path

from recipes import views
from recipes.views import RecipeList, ListUpdateDeleteRecipe

urlpatterns = [
    path('', RecipeList.as_view()),
    path('<int:pk>/', RecipeList.as_view()),
    path('create/', RecipeList.as_view()),
    path('update/<int:pk>/', ListUpdateDeleteRecipe.as_view()),
    path('delete/<int:pk>/', ListUpdateDeleteRecipe.as_view())
]
