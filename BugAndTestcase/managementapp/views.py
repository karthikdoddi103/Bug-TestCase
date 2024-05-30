from django.shortcuts import render, redirect
from managementapp.models import Contact
from managementapp.forms import ContactForm
from adminsapp.models import Employee, Project
from adminsapp.forms import EmployeeForm, ProjectForm
from managementapp.models import Task
from managementapp.forms import TaskForm
from employeeapp.models import Bug, Testcase
from employeeapp.forms import BugForm, TestcaseForm


# Create your views here.

def index(request):
    return render(request, "index.html", {})


def about(request):
    return render(request, "about.html", {})


def blog(request):
    return render(request, "blog.html", {})


def contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
        return render(request, "contact.html", {})
    return render(request, "contact.html", {})


def management(request):
    if request.method == "POST":
        email = request.POST['email']
        p_word = request.POST['password']
        request.session['email'] = email
        if Employee.objects.filter(email=email, password=p_word, role="manager"):
            return render(request, "management_home.html", {"msg": "Great! login successfully"})
        else:
            return render(request, "management_login.html", {"msg": "Sorry! you are not a manager"})
    return render(request, "management_login.html", {})


def management_home(request):
    return render(request, "management_home.html", {})


def management_logout(request):
    request.session["email"] = ""
    del request.session["email"]
    return render(request, "management_login.html", {})


def islogin(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def add_task(request):
    if request.method == "POST":
        task = TaskForm(request.POST)
        print("hi1")
        try:
            if task.is_valid():
                print("hi2")
                task.save()
                print("h3")
        except Exception as e:
            print(e)
            return render(request, "add_task.html", {"msg": "success"})
    mngr_email = request.session["email"]
    details_emply = Employee.objects.all().exclude(role="manager")
    details_project = Project.objects.all()
    return render(request, "add_task.html",
                  {"mngr_email": mngr_email, "details_emply": details_emply, "details_project": details_project})


def view_task(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        return render(request, "view_task.html", {"tasks": tasks})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("/view_task")


def edit_task(request, id):
    tasks = Task.objects.get(id=id)
    mngr_email = request.session["email"]
    details_emply = Employee.objects.all().exclude(role="manager")
    details_project = Project.objects.all()
    return render(request, "edit_task.html", {"mngr_email": mngr_email, "details_emply": details_emply, "tasks": tasks,
                                              "details_project": details_project})


def update_task(request):
    if request.method == "POST":
        userid = request.POST["id"]
        task = Task.objects.get(id=userid)
        task = TaskForm(request.POST, instance=task)
        print("hi1")
        try:
            if task.is_valid():
                print("hi2")
                task.save()
                print("h3")
        except Exception as e:
            print(e)
            return redirect("/view_task", {"msg": "success"})
    return render(request, "edit_task.html", {})


def manager_view_testcases(request):
    if request.method == "GET":
        testcases = Testcase.objects.all()
        return render(request, "manager_view_testcases.html", {"testcases": testcases})


def manager_view_bugs(request):
    if request.method == "GET":
        bugs = Bug.objects.all()
        return render(request, "manager_view_bugs.html", {"bugs": bugs})


def task_update_status(request, id):
    tasks = Task.objects.get(id=id)
    # email= request.session["email"]
    return render(request, "task_update_status.html", {"tasks": tasks, "id": id})


def task_status_insert(request):
    if request.method == "POST":
        try:
            # tested_by_email = request.session["email"]
            status = request.POST['status']
            id = request.POST['id']
            print("hi1")
            print("hi2")
            task = Task.objects.get(id=id)
            print("hi3")
            task.status = status
            # task.tested_by_email=tested_by_email
            print("hi4")
            task.save()
            print("hi")
        except Exception as e:
            print(e)
            return render(request, "view_task.html", {})
    return render(request, "task_update_status.html", {})
