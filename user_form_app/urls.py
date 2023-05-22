from django.urls import path
from .views import user_form, submitted_forms

urlpatterns = [
    path('user-form/', user_form, name='user_form'),
    path('submitted-forms/', submitted_forms, name='submitted_forms'),
]
