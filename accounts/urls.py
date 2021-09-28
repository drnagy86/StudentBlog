
from django.urls import path
from .views import SignUpView

urlpatterns = [
    # unnecessary as I will be the only user
    #path('signup/', SignUpView.as_view(), name='signup'),
]