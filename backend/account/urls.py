from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework.routers import DefaultRouter
from .views import CustomUserCreate, BlacklistTokenUpdateView, MeView, ProfileEditView, ChangePasswordView, DeleteUserView



# router = DefaultRouter()
# router.register(r'avatar', EditAvatarViewSet, basename='avatar')


urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/blacklist/', BlacklistTokenUpdateView.as_view(), name="token_blacklist"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
    path('edit-profile/', ProfileEditView.as_view(), name='edit-profile'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), 
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('delete-user/', DeleteUserView.as_view(), name='delete_user'),
  
   
   ]



