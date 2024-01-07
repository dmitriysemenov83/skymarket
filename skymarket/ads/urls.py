from django.urls import path, include
from ads.views import AdViewSet, CommentViewSet
from rest_framework_nested import routers

from rest_framework_nested.routers import NestedDefaultRouter

from ads.views import AdMyListAPIView

router = routers.DefaultRouter()
router.register(r'ads', AdViewSet, basename='ads')

ads_router = NestedDefaultRouter(router, r'ads', lookup='ad')
ads_router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('ads/me/', AdMyListAPIView.as_view(), name='ad_my_list'),
    path('', include(router.urls)),
    path('', include(ads_router.urls)),
]
