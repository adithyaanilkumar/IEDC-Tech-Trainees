from django.urls import path , include
from .views import AuthorProfileView, AuthorProfileViewDetails   #, ModelViewset, GenericApiView
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('', ModelViewset, basename='AuthorProfile')
urlpatterns = [
    path('', AuthorProfileView.as_view()),
    path('<str:username>/', AuthorProfileViewDetails.as_view()),

    # path('viewsets/', include(router.urls)),

    # path('generic/<str:username>/', GenericApiView.as_view()),
    # path('generic/', GenericApiView.as_view()),

    # path('detail/<int:id>/', ArticleDetails.as_view())
]