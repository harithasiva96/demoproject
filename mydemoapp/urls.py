from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='path'),
    path('path2',views.home2,name='path2'),
    path('login',views.login,name='login'),
    path('edit',views.edit,name='edit'),
    path('userhome',views.user_home,name='userhome'),
    path('logout',views.log_out,name='logout'),
    path('info',views.addinfo,name='info'),
    path('adminhome',views.admin_home,name='adminhome'),
    path('view',views.admin_view,name='view'),
    path("view_info",views.user_view,name='view_info'),
    path('update/<int:id>', views.update_info, name='update'),
    path('delete/<int:id1>', views.deletion, name='delete'),
    path('files',views.file_upload,name='files'),
    path('view_files', views.view_files, name='view_files'),
]