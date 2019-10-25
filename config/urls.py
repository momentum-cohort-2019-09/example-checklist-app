"""config URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from listo import views

urlpatterns = [
    path('', views.checklists_list, name='checklists_list'),
    path('lists/<int:pk>/', views.checklists_detail, name="checklists_detail"),
    path('lists/<int:pk>/edit/', views.checklists_edit, name="checklists_edit"),
    path('lists/<int:pk>/delete/',
         views.checklists_delete,
         name="checklists_delete"),
    path('lists/<int:pk>/reorder/',
         views.checklists_reorder,
         name="checklists_reorder"),
    path('lists/new/', views.checklists_create, name='checklists_create'),
    path('items/<int:pk>/edit/',
         views.checklist_items_edit,
         name="checklist_items_edit"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
