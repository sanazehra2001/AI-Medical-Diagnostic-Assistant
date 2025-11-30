from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ConversationViewSet, MessageViewSet, RegisterUserView

router = DefaultRouter()
router.register("conversations", ConversationViewSet)
router.register("messages", MessageViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterUserView.as_view(), name="register"),
]
