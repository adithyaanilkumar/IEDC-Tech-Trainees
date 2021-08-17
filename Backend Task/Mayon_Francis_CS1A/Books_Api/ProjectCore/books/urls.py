from django.urls import path , include
from .views import  ModelViewset, BookGeneric        #, GenericApiView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', ModelViewset, basename='Book')

urlpatterns = [
    # path('', UserProfileView.as_view()),
    # path('<str:username>/', UserProfileViewDetails.as_view()),

    path('<str:name>/', BookGeneric.as_view()),
    path('', include(router.urls)),

    path('generic/', BookGeneric.as_view()),

    # path('detail/<int:id>/', ArticleDetails.as_view())
]