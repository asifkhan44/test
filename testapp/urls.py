from django.urls import path
from testapp import views
urlpatterns= [
        path('',views.TestView.as_view(), name='test')
]