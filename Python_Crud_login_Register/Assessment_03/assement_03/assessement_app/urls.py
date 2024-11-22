from .views import View
from .import views
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('demo/',views.CreateEmployee.as_view(),name='index'),
    path('Records',views.GetEmployee.as_view(),name = 'Records'),
    path('Records/<int:id>',views.DeleteEmployee.as_view(),name = 'delete_employee'),
    path('Update/<int:id>',views.Update_employee.as_view(),name = 'update_employee'),
    path('View/<int:id>',views.View_employee.as_view(),name ="view_employee"),
    path('dashboard/',views.index,name='dashboard'),
    path('',views.Login.as_view(),name='login'),
    path('register/',views.Register.as_view(),name='register'),
    path('logout/',views.Logout.as_view(), name='logout'),
    path('forget/',views.ForgetPassword.as_view(), name='forget'),
    path('reset/<uuid>',views.Reset_Pass.as_view(), name='reset'),

]