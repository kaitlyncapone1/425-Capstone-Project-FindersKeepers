
"""
URL configuration for finderskeepers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path(x'', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
URL configuration for finderskeepers project.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views   # ← add this

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth routes
    path('login/', auth_views.LoginView.as_view(
        template_name='lostandfound/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # App routes
    path('', include('lostandfound.urls')),
]
