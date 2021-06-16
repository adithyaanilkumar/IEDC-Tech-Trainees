from django.urls import path , include
from .views import UserProfileView, ModelViewset, GenericApiView, UserProfileViewDetails
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('', ModelViewset, basename='UserProfile')
urlpatterns = [
    path('', UserProfileView.as_view()),
    path('<str:username>/', UserProfileViewDetails.as_view()),

    path('viewsets/', include(router.urls)),

    path('generic/<str:username>/', GenericApiView.as_view()),
    path('generic/', GenericApiView.as_view()),

    # path('detail/<int:id>/', ArticleDetails.as_view())
]