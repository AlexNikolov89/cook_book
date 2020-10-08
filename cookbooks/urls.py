from django.urls import path

from cookbooks.views import CookbookList, ListUpdateDeleteCookbook

urlpatterns = [
    path('', CookbookList.as_view()),
    path('<int:pk>/', CookbookList.as_view()),
    path('create/', CookbookList.as_view()),
    path('update/<int:pk>/', ListUpdateDeleteCookbook.as_view()),
    path('delete/<int:pk>/', ListUpdateDeleteCookbook.as_view()),
]

