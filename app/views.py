from django.shortcuts import render, HttpResponse, redirect
from random import randint
from app.models import Account, Instructor, Device, Request, Admin_Account
from datetime import datetime, date
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache

# Create your views here.
def borrow(request):
    rand = randint(0, 16777215)
    hexa = "%x" % rand
    hexa = hexa.upper()
    dic = list(Request.objects.values_list('request_number', flat=True))

    while True:
        if hexa in dic:
            rand = randint(0, 16777215)
            hexa = "%x" % rand
            hexa = hexa.upper()
        else:
            break

    context = {
        'hexa': hexa,
        'accounts': Account.objects.all(),
        'instructors': Instructor.objects.all(),
    }
    return render(request, 'request.html', context)

def ret(request):
    return render(request, 'return.html')

def ret_process(request):
    req = Request.objects.get(request_number=request.POST['request-number'])
    req.returned = True
    req.date_returned = datetime.strftime(date.today(), "%Y-%m-%d")
    req.save()
    return redirect('/ret-success/')

def ret_success(request):
    return render(request, 'return-success.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'adminlogin.html')

def logs(request):
    id_number = request.session.get('id_number')
    context = {
        "account": Account.objects.get(id_number=id_number),
        "requests": Request.objects.all()
    }
    return render(request, 'logs.html', context)

def requests(request):
    id_number = request.session.get('id_number')
    context = {
        "account": Account.objects.get(id_number=id_number),
        "requests": Request.objects.filter(approved=False)
    }
    return render(request, 'requests.html', context)

def approve_process(request, pk):
    req = Request.objects.get(pk=pk)
    req.approved = True
    req.save()
    return redirect('/requests/')

def register_process(request):
    account = Account()

    account.name = request.POST['name']
    account.id_number = request.POST['id_number']

    account.save()

    return redirect("/")

def request_process(request):
    account = request.POST['requested_by']
    instructor = request.POST['instructor']
    reason = request.POST['reason']
    room = request.POST['room']
    date_needed = datetime.strptime(request.POST['date-needed'], "%Y-%m-%d")
    time_in = request.POST['time-in']
    time_out = request.POST['time-out']
    devices = request.POST.getlist('device[]')
    request_number = request.POST['request-number']
    print(devices)

    req = Request()

    req.requested_by = Account.objects.get(name=account)
    req.instructor_in_charge = Instructor.objects.get(name=instructor)
    req.reason = reason
    req.room = room
    req.request_number = request_number
    req.date_needed = date_needed
    req.date_borrowed = datetime.strftime(date.today(), '%Y-%m-%d')
    req.time_in = time_in
    req.time_out = time_out
    req.returned = False
    req.approved = False
    req.save()

    for device in devices:
        req.device.add(Device.objects.get(name=device))
    
    req.save()

    return redirect('/request-success/' + request_number)

def request_success(request, request_number):
    context = {
        'num': request_number
    }
    return render(request, 'request-sent.html', context)

def login_process(request):
    admin_account = Admin_Account.objects.get(id_number=request.POST['id-number'])
    if request.POST['password'] == admin_account.password:
        request.session['id_number'] = request.POST['id-number']

        return redirect('/logs/')
    else:
        return HttpResponse('wrong id number or password')

@never_cache
def logoutview(request):
    logout(request)
    return redirect('/login/')