from django.shortcuts import render, redirect
from adminsapp.models import Employee, Project
from adminsapp.forms import EmployeeForm, ProjectForm
from employeeapp.models import Testcase, Bug
from employeeapp.forms import TestcaseForm, BugForm


# Create your views here.
def employee(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]

        try:
            employee = Employee.objects.get(email=email, password=password, role=role)
            print(role)
            request.session["email"] = email
            request.session["role"] = role
            return render(request, "employee_home.html", {"employee":employee,"role":role})
        except Exception as e:
            msg = "Invalid credentials"
            print(e)
            return render(request, "employee_login.html", {"msg": msg})
    return render(request, "employee_login.html", {})

def employee_home(request):
    return render(request, "employee_home.html", {})


def employee_change_pwd(request):
    if islogin(request):
        role = request.session["role"]
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            new_password = request.POST["new_password"]
            try:
                employee = Employee.objects.get(email=email, password=password, role=role)

                employee.password = new_password
                employee.save()
                msg = "password update successfully"
                return redirect("/employee_logout")
            except:
                msg = "invalid data"
                request.session["role"] = role
                return render(request, "employee_chpwd.html", {"msg": msg,"role":role})
        return render(request, "employee_chpwd.html", {"role":role})
    else:
        return render(request, "employee_login.html", {})


def employee_logout(request):
    request.session["email"] = ""
    request.session["role"] = ""
    del request.session["email"]
    del request.session["role"]

    return render(request, "employee_login.html", {})


def islogin(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False


def employee_edit_profile(request):
    email = request.session["email"]
    role = request.session["role"]
    employ = Employee.objects.get(email=email, role=role)
    print(employ)
    return render(request, "employee_edit_profile.html", {"employ": employ, "role":role})


def employee_update_profile(request):
    email = request.session['email']
    role = request.session["role"]
    data = Employee.objects.get(email=email, role=role)
    if request.method == "POST":
        print("hi1")
        email = request.session["email"]
        print(email)
        emp = Employee.objects.get(email=email, role=role)
        print("hi3")
        employee = EmployeeForm(request.POST, instance=emp)
        print("hi4")
        try:
            if employee.is_valid():
                print("hi6")
                employee.save()
                print("hi")
                return render(request, "employee_home.html", {"msg": "update successfully", "role": role})
        except Exception as e:
            print(e)
            return render(request, "employee_home.html", {"msg": "your details not updated", "role":role})
    return render(request, "employee_edit_profile.html", {"employee":data, "role":role})


def add_testcase(request):
    if request.method == "POST":
        testcase = TestcaseForm(request.POST)
        print("hi1")
        try:
            if testcase.is_valid():
                print("hi2")
                testcase.save()
                print("h3")
        except Exception as e:
            print(e)
            return render(request, "add_testcase.html", {"msg": "success"})
    tester_emails = request.session["email"]
    details_project = Project.objects.all()
    return render(request, "add_testcase.html", {"tester_emails": tester_emails, "details_project": details_project})


def view_testcase(request):
    if request.method == "GET":
        testcases = Testcase.objects.all()
        role=request.session["role"]
        return render(request, "view_testcase.html", {"testcases": testcases,"role": role})


def delete_testcase(request, id):
    testcase = Testcase.objects.get(id=id)
    testcase.delete()
    return redirect("/view_testcase")

def edit_testcase(request, id):
    testcases = Testcase.objects.get(id=id)
    tester_emails = request.session["email"]
    details_project = Project.objects.all()
    return render(request, "edit_testcase.html",
                  {"testcases": testcases, "tester_emails": tester_emails, "details_project": details_project})


def update_testcase(request):
    if request.method == "POST":
        userid = request.POST["id"]
        testcase = Testcase.objects.get(id=userid)
        testcase = TestcaseForm(request.POST, instance=testcase)
        print("hi1")
        try:
            if testcase.is_valid():
                print("hi2")
                testcase.save()
                print("h3")
        except Exception as e:
            print(e)
            return redirect("/view_testcase", {"msg": "success"})
        return render(request, "edit_testcase.html", {})

def add_bug(request):
    if request.method == "POST":
        print("hi")
        bugs = BugForm(request.POST,request.FILES)
        print(bugs.errors)
        print("hi1")
        try:
            if bugs.is_valid():
                print("hi2")
                bugs.save()
                print("h3")
        except Exception as e:
            print(e)
        return render(request, "add_bug.html", {"msg": "success"})
    tested_by = request.session["email"]
    testcaseids = Testcase.objects.all()
    return render(request, "add_bug.html",
                          {"tested_by": tested_by, "testcaseids": testcaseids})

def view_bug(request):
    if request.method=="GET":
        bugs=Bug.objects.all()
        role=request.session["role"]
        return render(request,"view_bug.html",{"bugs":bugs,"role":role})

def delete_bug(request, id):
    bugs = Bug.objects.get(id=id)
    bugs.delete()
    return redirect("/view_bug")

def edit_bug(request, id):
    bugs = Bug.objects.get(id=id)
    tested_by = request.session["email"]
    testcaseids = Testcase.objects.all()
    return render(request, "edit_bug.html",
                  {"tested_by": tested_by, "testcaseids": testcaseids,"bugs":bugs})


def update_bug(request):
    if request.method == "POST":
        userid = request.POST["id"]
        bugs = Bug.objects.get(id=userid)
        print("hi")
        bugs = BugForm(request.POST,request.FILES,instance=bugs)
        print(bugs.errors)
        print("hi1")
        try:
            if bugs.is_valid():
                print("hi2")
                bugs.save()
                print("h3")
        except Exception as e:
            print(e)
        return redirect("/view_bug", {"msg": "success"})
    return render(request, "edit_bug.html", {})

def developer_view_bugs(request):
    if request.method=="GET":
        role=request.session["role"]
        print(role)
        bugs=Bug.objects.all()
        return render(request,"developer_view_bugs.html",{"bugs":bugs,"role":role})

def developer_view_testcases(request):
    if request.method == "GET":
        role=request.session["role"]
        testcases = Testcase.objects.all()
        return render(request, "developer_view_testcases.html", {"testcases": testcases,"role":role})

def developer_update_status(request,id):
    bugs = Bug.objects.get(id=id)
    email= request.session["email"]
    return render(request,"developer_status_update.html",{"bugs":bugs,"email":email,"id":id})

def developer_status_insert(request):
    if request.method == "POST":
        try:
            tested_by_email = request.session["email"]
            status=request.POST['status']
            id=request.POST['id']
            print("hi1")
            print("hi2")
            bug=Bug.objects.get(id=id)
            print("hi3")
            bug.status=status
            bug.tested_by_email=tested_by_email
            print("hi4")
            bug.save()
            print("hi")
        except Exception as e:
            print(e)
            return render(request, "developer_view_bugs.html", {})
    return render(request, "developer_status_update.html", {})

def tester_update_status(request,id):
    bugs = Bug.objects.get(id=id)
    email= request.session["email"]
    return render(request,"tester_update_status.html",{"bugs":bugs,"email":email,"id":id})

def tester_status_insert(request):
    if request.method == "POST":
        try:
            tested_by_email = request.session["email"]
            status=request.POST['status']
            id=request.POST['id']
            print("hi1")
            print("hi2")
            bug=Bug.objects.get(id=id)
            print("hi3")
            bug.status=status
            bug.tested_by_email=tested_by_email
            print("hi4")
            bug.save()
            print("hi")
        except Exception as e:
            print(e)
            return render(request, "view_bug.html", {})
    return render(request, "tester_update_status.html", {})

def analyst_view_bugs(request):
    if request.method=="GET":
        bugs=Bug.objects.all()
        return render(request,"analyst_view_bugs.html",{"bugs":bugs})

def analyst_view_testcases(request):
    if request.method == "GET":
        testcases = Testcase.objects.all()
        return render(request, "analyst_view_testcases.html", {"testcases": testcases})
