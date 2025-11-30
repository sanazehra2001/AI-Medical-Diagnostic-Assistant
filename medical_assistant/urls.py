from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import ConversationViewSet, MessageViewSet, RegisterUserView

router = DefaultRouter()
router.register("conversations", ConversationViewSet, basename="conversation")
router.register("messages", MessageViewSet, basename="message")

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", obtain_auth_token, name="api_token_auth"),
]
