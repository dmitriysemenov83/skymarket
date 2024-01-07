from rest_framework import pagination, viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from ads.filters import AdFilter

from ads.models import Comment, Ad
from ads.serializers import AdSerializer, CommentSerializer
from rest_framework.generics import get_object_or_404

from ads.permissions import IsOwnerOrRoles
from rest_framework.response import Response

from ads.serializers import AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.all().order_by('-created_at')
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    # def get_permissions(self):
    #     if self.action == 'create' or self.action == 'update' \
    #             or self.action == 'partial_update' or self.action == 'destroy':
    #         permission_classes = [IsAuthenticated, IsOwnerOrRoles]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsAuthenticated, IsOwnerOrRoles]
        elif self.action in ["update", "partial_update"]:
            permission_classes = [IsAuthenticated, IsOwnerOrRoles]
        elif self.action == "destroy":
            permission_classes = [IsAuthenticated, IsOwnerOrRoles]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = AdDetailSerializer(instance)
        return Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' \
                or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwnerOrRoles]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
    def get_queryset(self):
        ad_pk = self.kwargs.get('ad_pk')
        return Comment.objects.filter(ad_id=ad_pk)

    def perform_create(self, serializer):
        ad_pk = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_pk)
        serializer.save(author=self.request.user, ad=ad)


class AdMyListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrRoles]

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user).order_by('-created_at')

