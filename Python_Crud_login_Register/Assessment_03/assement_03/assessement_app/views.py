from django.shortcuts import render,redirect
from django.views import View
from .models import Employee,ResetUuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import datetime
import uuid, random
from django.utils import timezone
import pytz
timezone.now()
datetime.datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)



class CreateEmployee(View):
    def get(self,request):
        return render(request,'employee_form.html')
    def post(self,request):
        employee_id = request.POST['employee_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = request.POST['department']
        position = request.POST['position']
        date_of_birth = request.POST['date_of_birth']
        date_joined = request.POST['date_joined']
        salary = request.POST['salary']
        is_full_time = request.POST.get('is_full_time',False) == 'on'
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        last_performance_review = request.POST['last_performance_review']
        Employee.objects.create(
             employee_id = employee_id,
            first_name =first_name,
            last_name = last_name,
            department = department,
            position = position,
            date_of_birth = date_of_birth,
            date_joined = date_joined,
            salary = salary,
            is_full_time = is_full_time,
            email = email,
            phone_number = phone_number,
            address = address,
            city = city,
            state = state,
            last_performance_review = last_performance_review
        )
        obj = Employee.objects.all()
        return redirect('/Records')


class GetEmployee(View):
    def get(self,request):
        Emplyees = Employee.objects.all()
        return render(request,'employee_list.html',{'Employees':Emplyees})
    
class DeleteEmployee(View):
    def get(self,request,id):
        obj = Employee.objects.get(id = id)
        obj.delete()
        print("employee is deleted succussfully")
        return render(request,'empoyee_list.html',{'obj':obj})    
    
class Update_employee(View):
    def get(self,request,id):
        obj = Employee.objects.get(id = id)
        return render(request,'employee_update.html',{'obj':obj})
    def post(self,request,id):
        obj = Employee.objects.get(id = id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        department = request.POST.get('department')
        position = request.POST.get('position')
        date_of_birth = request.POST.get('date_of_birth')
        date_joined = request.POST.get('date_joined')
        salary = request.POST.get('salary')
        is_full_time = request.POST.get('is_full_time',False) =='on'
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        last_performance_review = request.POST.get('last_performance_review')
        if first_name:
            obj.first_name = first_name
        if last_name:
            obj.last_name = last_name
        if department:
            obj.department = department
        if position:
            obj.position = position
        if date_of_birth:
            obj.date_of_birth = date_of_birth
        if date_joined:
            obj.date_joined = date_joined
        if salary:
            obj.salary = salary
        if email:
            obj.email = email
        if phone_number:
            obj.phone_number = phone_number
        if address:
            obj.address = address
        if city:
            obj.city = city
        if state:
            obj.state = state
        if last_performance_review:
            obj.last_performance_review = last_performance_review
        if is_full_time:
            obj.is_full_time = True
        else:
            obj.is_full_time = False   
        obj.save()
        return redirect('/Records')
class View_employee(View):
    def get(self,request,id):
        obj = Employee.objects.get(id = id)
        return render(request,'employee_detail.html',{'obj':obj})
    
def index(request):
    return render(request,'index.html')

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            user =authenticate(username=username,password=password)
            print("user is same",user)
            if user != None:
                login(request,user)

                return redirect('/dashboard')
            else:
                print("invalid credentials")
        else:
            print("username not found")

        return render(request,'login.html')
    
class Register(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        email= request.POST.get("email")
        username= request.POST.get("username")
        password= request.POST.get("password")
        print("....1",first_name)
        print('..2',password)
        print('..3',last_name)
        print('..4',email)
        print('..5',username)

        if User.objects.filter(email = email).exists():
            print("email taken already")
            
        elif User.objects.filter(username=username).exists():
            print('username taken already')
        else:
            User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                password = password
            )
            address = email
            subject = "hello in my website"
            message = f"{username}-{password}"
            print("registeration succussfull please go to the login page")
            if address and subject and message:
                try:
                    print("yoou are mail section01")
                    send_mail(subject,message,settings.EMAIL_HOST_USER,[address])
                    print("sent")
                except Exception as e:
                    print("yoou are mail section02")
                    print(e)
            else:
                    print("yoou are mail section03")

            return redirect('login')
        return render(request,'signup.html')

class Logout(View):
    def get(self,request):
        logout(request)
        print("logout succcueessly")
        return redirect('dashboard')    
    
class ForgetPassword(View):
    def get(self,request):
        return render(request,'forget.html')
    def post(self,request):
        email = request.POST.get('email')
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            exp_date = datetime.datetime.now() + datetime.timedelta(hours=  2)
            UUID_data = uuid.uuid1(random.randint(0, 25415447))
            forget = ResetUuid.objects.create(UUID=UUID_data,user=user,expiry =exp_date)
            print("forget",forget)
            url = f'{settings.SITE_URL}reset/{forget.UUID}'
            print('url',url)
            message = f"password reset link {url}"
            address = email
            subject = "password reset link "
            try:
                print("you are sending mail")
                send_mail(subject,message,settings.EMAIL_HOST_USER,[address])
            except Exception as e:
                print("error in sending mail")
                print(e)
            else:
                    print("mail sent successfull check your mail")
            return redirect('login') 
        return render(request,'forget.html')
class Reset_Pass(View):
    def get(self,request,uuid):
        context = { 'uuid':uuid}
        return render(request,'reset.html',context)
    def post(self,request,uuid):
        new_pass = request.POST.get('new_pass')
        confirm_pass = request.POST.get('confirm_pass')
        current_date_time = datetime.datetime.now()
        obj = ResetUuid.objects.get(UUID = uuid)
        user = obj.user
        current_time  = current_date_time.astimezone()

        if current_time < obj.expiry and new_pass == confirm_pass:
            user.set_password(new_pass)
            user.save()
            return redirect('/')
        else:
            print("link expired")
            return redirect('/')    
    
