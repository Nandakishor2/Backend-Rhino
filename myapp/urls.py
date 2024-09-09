from django.urls import path
from . import views
urlpatterns = [
    path('suggestions',views.suggestions,name = "suggestions"),
    path('suggestions/<str:id>/vote',views.vote,name = "vote")
]
