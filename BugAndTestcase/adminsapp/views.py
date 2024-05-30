from django.shortcuts import render, redirect
from adminsapp.models import Admins
from adminsapp.models import Employee
from adminsapp.forms import EmployeeForm
from adminsapp.models import Project
from adminsapp.forms import ProjectForm
from employeeapp.models import Bug, Testcase
from employeeapp.forms import BugForm, TestcaseForm
from adminsapp.models import News
from adminsapp.forms import NewsForm


# Create your views here.

def admins(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        request.session["username"] = username
        try:
            admin = Admins.objects.get(username=username, password=password)

            msg = "data found"
            print("msg")
            return render(request, "admins_home.html", {"admin": admin, "msg": msg})
        except Exception as e:
            msg = "Invalid credentials"
            print(e)
            return render(request, "admins.html", {"msg": msg})
    return render(request, "admins.html", {})


def admins_home(request):
    return render(request, "admins_home.html", {})


def admins_change_pwd(request):
    if islogin(request):
        if request.method == "POST":
            username = request.session["username"]
            password = request.POST["password"]
            new_password = request.POST["new_password"]
            try:
                admins = Admins.objects.get(username=username, password=password)
                admins.password = new_password
                admins.save()
                msg = "password update successfully"
                return redirect("/admins_logout")
            except:
                return render(request, "admins_chpwd.html", {"msg": "invalid data"})
        return render(request, "admins_chpwd.html", {})
    else:
        return render(request, "admins.html", {})


def admins_logout(request):
    request.session["username"] = ""
    del request.session["username"]
    return render(request, "admins.html", {})


def islogin(request):
    if request.session.__contains__("username"):
        return True
    else:
        return False


def add_employee(request):
    if request.method == "POST":
        print("hi")
        employee = EmployeeForm(request.POST)
        print("hi1")
        try:
            if employee.is_valid():
                print("hi2")
                employee.save()
                print("h3")
        except Exception as e:
            print(e)
            return render(request, "add_employee.html", {"msg": "success"})
    return render(request, "add_employee.html", {})


def view_employee(request):
    if request.method == 'GET':
        employee = Employee.objects.all()
    return render(request, "view_employee.html", {"employee": employee})


def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/view_employee")


def edit_employee(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit_employee.html", {"employee": employee})


def update_employee(request):
    if request.method == "POST":
        print("h")
        userid = request.POST["id"]
        print("hi")
        employee = Employee.objects.get(id=userid)
        print("HI")
        employee = EmployeeForm(request.POST, instance=employee)
        print("hii")
        if employee.is_valid():
            print("hiii")
            employee.save()
            print("hiiiii")
        return redirect("/view_employee")
    return redirect("/view_employee")


def add_project(request):
    managers = Employee.objects.filter(role="manager")
    return render(request, "add_project.html", {"managers": managers})


def add_new_project(request):
    if request.method == "POST":
        project = ProjectForm(request.POST)
        try:
            if project.is_valid():
                print("hi2")
                project.save()
                print("h3")
                return render(request, "admins_home.html", {})
        except Exception as e:
            print(e)
            return render(request, "add_project.html", {})
    return render(request, "add_project.html", {})


def view_project(request):
    if request.method == 'GET':
        projects = Project.objects.all()
    return render(request, "view_project.html", {"projects": projects})


def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete()
    return redirect("/view_project")


def edit_project(request, id):
    project = Project.objects.get(id=id)
    managers = Employee.objects.filter(role="manager")
    return render(request, "edit_project.html", {"project": project, "managers": managers})


def update_project(request):
    if request.method == "POST":
        print("h")
        userid = request.POST["id"]
        print("hi")
        project = Project.objects.get(id=userid)
        print("HI")
        project = EmployeeForm(request.POST, instance=project)
        print("hii")
        if project.is_valid():
            print("hiii")
            project.save()
            print("hiiiii")
        return redirect("/view_project")
    return redirect("/view_project")


def view_testcases(request):
    if request.method == "GET":
        testcases = Testcase.objects.all()
    return render(request, "view_testcases.html", {"testcases": testcases})


def view_bugs(request):
    if request.method == "GET":
        bugs = Bug.objects.all()
    return render(request, "view_bugs.html", {"bugs": bugs})


def add_news(request):
    if request.method == "POST":
        news = NewsForm(request.POST)
        if news.is_valid():
            news.save()
        return render(request, "add_news.html", {"msg": "success"})
    return render(request, "add_news.html", {})


def view_news(request):
    if request.method == "GET":
        news = News.objects.all()
    return render(request, "view_news.html", {"news": news})

def delete_news(request,id):
    news=News.objects.get(id=id)
    news.delete()
    return redirect("/view_news")

def edit_news(request, id):
    news = News.objects.get(id=id)
    return render(request, "edit_news.html", {"news": news})


def update_news(request):
    if request.method == "POST":
        userid = request.POST["id"]
        news = News.objects.get(id=userid)
        news = NewsForm(request.POST, instance=news)
        if news.is_valid():
            news.save()
        return redirect("/view_news")
    return redirect("/view_news")
