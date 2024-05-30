"""BugAndTestcase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from managementapp import views as management_view
from adminsapp import views as admins_view
from employeeapp import views as employee_view


urlpatterns = [
    #----------------management---------------------
    path("",management_view.index,name="index"),
    path("index/", management_view.index, name="index"),
    path("about/",management_view.about,name="about"),
    path("blog/",management_view.blog,name="blog"),
    path("contact/",management_view.contact,name="contact"),
    path("management/",management_view.management,name="management"),
    path("management_home/",management_view.management_home,name="management_home"),
    path("management_logout/",management_view.management_logout,name="management_logout"),
    path("add_task/",management_view.add_task,name="add_task"),
    path("view_task/",management_view.view_task,name="view_task"),
    path("delete_task/<id>",management_view.delete_task,name="delete_task"),
    path("edit_task/<int:id>",management_view.edit_task,name="edit_task"),
    path("update_task/",management_view.update_task,name="update_task"),
    #path("view_testcases/",management_view.view_testcases,name="view_testcases"),
    #path("view_bugs/",management_view.view_bugs,name="view_bugs"),
    path("task_update_status/<id>",management_view.task_update_status,name="task_update_status"),
    path("task_status_insert/",management_view.task_status_insert,name="task_status_insert"),
    path("manager_view_testcases/",management_view.manager_view_testcases,name="manager_view_testcases"),
    path("manager_view_bugs/",management_view.manager_view_bugs,name="manager_view_bugs"),
    #----------------------admin-----------------
    path('admin/', admin.site.urls),
    path("admins/",admins_view.admins,name="admins"),
    path("admins_home/",admins_view.admins_home,name="admins_home"),
    path("admins_change_pwd/",admins_view.admins_change_pwd,name="admins_change_pwd"),
    path("admins_logout/",admins_view.admins_logout,name="admins_logout"),
    path("add_employee/",admins_view.add_employee,name="add_employee"),
    path("view_employee/",admins_view.view_employee,name="view_employee"),
    path("delete_employee/<id>",admins_view.delete_employee,name="delete_employee"),
    path("edit_employee/<int:id>",admins_view.edit_employee,name="edit_employee"),
    path("update_employee/",admins_view.update_employee,name="update_employee"),
    path("add_project/",admins_view.add_project,name="add_project"),
    path("add_new_project/",admins_view.add_new_project,name="add_new_project"),
    path("view_project/",admins_view.view_project,name="view_project"),
    path("delete_project/<id>",admins_view.delete_project,name="delete_project"),
    path("edit_project/<id>",admins_view.edit_project,name="edit_project"),
    path("update_project/",admins_view.update_project,name="update_project"),
    path("view_testcases/",admins_view.view_testcases,name="view_testcases"),
    path("view_bugs/",admins_view.view_bugs,name="view_bugs"),
    path("add_news/",admins_view.add_news,name="add_news"),
    path("view_news/",admins_view.view_news,name="view_news"),
    path("delete_news/<id>",admins_view.delete_news,name="delete_news"),
    path("edit_news/<id>",admins_view.edit_news,name="edit_news"),
    path("update_news/",admins_view.update_news,name="update_news"),
    #----------------------employee------------------------
    path("employee/",employee_view.employee,name="employee"),
    path("employee_home/",employee_view.employee_home,name="employee_home"),
    path("employee_change_pwd/",employee_view.employee_change_pwd,name="employee_change_pwd"),
    path("employee_logout/",employee_view.employee_logout,name="employee_logout"),
    path("employee_edit_profile/",employee_view.employee_edit_profile,name="employee_edit_profile"),
    path("employee_update_profile/",employee_view.employee_update_profile,name="employee_update_profile"),
    path("add_testcase/",employee_view.add_testcase,name="add_testcase"),
    path("view_testcase/",employee_view.view_testcase,name="view_testcase"),
    path("delete_testcase/<id>",employee_view.delete_testcase,name="delete_testcase"),
    path("edit_testcase/<id>",employee_view.edit_testcase,name="edit_testcase"),
    path("update_testcase/",employee_view.update_testcase,name="update_testcase"),
    path("add_bug/",employee_view.add_bug,name="add_bug"),
    path("view_bug/",employee_view.view_bug,name="view_bug"),
    path("delete_bug/<id>",employee_view.delete_bug,name="delete_bug"),
    path("edit_bug/<id>",employee_view.edit_bug,name="edit_bug"),
    path("update_bug/",employee_view.update_bug,name="update_bug"),
    path("developer_view_bugs/",employee_view.developer_view_bugs,name="developer_view_bugs"),
    path("developer_view_testcases/",employee_view.developer_view_testcases,name="developer_view_testcases"),
    path("developer_update_status/<id>",employee_view.developer_update_status,name="developer_update_status"),
    path("developer_status_insert/",employee_view.developer_status_insert,name="developer_status_insert"),
    path("tester_update_status/<id>",employee_view.tester_update_status,name="tester_update_status"),
    path("tester_status_insert/",employee_view.tester_status_insert,name="tester_status_insert"),
    path("analyst_view_bugs/",employee_view.analyst_view_bugs,name="analyst_view_bugs"),
    path("analyst_view_testcases/",employee_view.analyst_view_testcases,name="analyst_view_testcases"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

