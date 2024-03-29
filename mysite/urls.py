"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from ptt_user.views import user_name_page
from ptt_user.views import ptt_msg_search_engine_page
from ptt_user.views import ptt_count_keyword_api
from ptt_user.views import count_eachUser_keyword_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user_name_page/', user_name_page),
    path('msg_search_engine/', ptt_msg_search_engine_page),
    path('count_keyword/',ptt_count_keyword_api),      
    path('count_eachUser_keyword_page/',count_eachUser_keyword_page),      
]