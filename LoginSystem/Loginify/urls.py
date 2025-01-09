
from django.urls import path
from. import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("Test/", views.print_hello),  
    path("Login/", views.login_view),
    path("Register/", views.register_view),
    path("GetAllUserDetails/", views.get_all_user_details_view),
    path("GetUserDetails/<str:username>/", views.get_user_by_email_view),
    path("UpdateUserDetails/<str:username>/", views.update_user_details_view),
    path("DeleteUserDetails/<str:username>/", views.delete_user_details_view),
    path("UpdateUserDetails/<str:username>/<email>/", views.update_user_details_view),
    path("UpdateUserDetails/<str:username>/<password>/", views.update_user_details_view),
    path("UpdateUserDetails/<str:username>/<email>/<password>/", views.update_user_details_view),
]