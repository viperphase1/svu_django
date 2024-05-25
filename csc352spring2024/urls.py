"""
URL configuration for csc352spring2024 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from lmsdev import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router=DefaultRouter()
router.register("question",views.QuestionCrud)
router.register("tag",views.TagCrud)
router.register("course",views.CourseCrud)
router.register("section",views.SectionCrud)
router.register("page",views.PageCrud)
router.register("block",views.BlockCrud)
router.register("user",views.UserCrud)
router.register("question_type",views.QuestionTypeCrud)
router.register("response_options",views.ResponseOptionCrud)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

# https://www.django-rest-framework.org/api-guide/authentication/#by-exposing-an-api-endpoint
# thomas added this
# obtain_auth_token is a view that you can post a username and password to and get back a token to authorize requests to the api
urlpatterns += [
    path('api-token-auth/', obtain_auth_token)
]
