from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserForm,CarForm,RideForm,LoginForm, editDestinationForm,editTimeForm, editNumForm, UserSearchForm
from .models import haha,Ride, Relation
from .models import car
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.hashers import make_password,check_password
from django.views.generic import TemplateView


# Create your views here.
def driver1(request,id1):
   # print(kk.status)
    kk= Ride.objects.get(pk = id1)
    kk.status = kk.status+1
    print(kk.status)
    kk.save()
   # print(kk)
    email = request.session.get('user_email')
    relas = Relation.objects.filter(r_request_id = kk)
    first = Relation.objects.filter(r_request_id = kk).first()
    #rela.r_driver_email = request.session.get('user_email')
    send_mail('Confirmed Email','test','heiheihei568@outlook.com',[first.r_owner_email],fail_silently=False)
    for rela in relas:
        send_mail('Confirmed Email','test','heiheihei568@outlook.com',[rela.r_sharer_email],fail_silently=False)
        rela.r_driver_email = email
        rela.save()
    
    
    
    #email = request.session.get('user_email')
    driverList = haha.objects.filter(email=email)
    driver = driverList.first()
#    print(driver.status_flag)
    flag = driver.status_flag
    if driver.status_flag == '1':
        hercar=car.objects.filter(driver_id=email).first()
        passen = hercar.max_passanger
       # print(passen)
        flag = 0
        #orderList=Ride.objects.filter(~Q(owner_email=email),NumPassanger__lte=passen,status=0)
        orders =list(Relation.objects.filter(~Q(r_owner_email=email),~Q(r_driver_email=email),~Q(r_sharer_email=email)).values('r_request_id'))
        h = None
        h = [sub['r_request_id'] for sub in orders]
        if Ride.objects.filter(id__in=h,NumPassanger__lte=passen,status=0):
            orderList = Ride.objects.filter(id__in=res,NumPassanger__lte=passen,status=0)
        else:
            orderList = None
            
        drive = list(Relation.objects.filter(r_driver_email=request.session.get('user_email')).values('r_request_id'))
        res = None
        res = [ sub['r_request_id'] for sub in drive ]
       # print(res)
        confirmList = None
        if Ride.objects.filter(id__in=res,status=1):
            confirmList = Ride.objects.filter(id__in=res,status = 1)
        else:
            confirmList = None
    else:
        orderList = None
        confirmList = None
        flag=1

         
    return render(request,'users/driver.html',{'isDriver':flag,'orderList':orderList,'confirmList':confirmList})   


def driver(request):
  
       
    email = request.session.get('user_email')
    if (email == None):
        return redirect('/login/')
    driverList = haha.objects.filter(email=email)
    driver = driverList.first()
    print(driver.status_flag)
    flag = driver.status_flag
    if driver.status_flag == '1':
        hercar=car.objects.filter(driver_id=email).first()
        passen = hercar.max_passanger
    #    print(passen)
        flag = 0
     #   orderList=Ride.objects.filter(~Q(owner_email=email),NumPassanger__lte=passen,status = 0)
        print(email)
        orders =list(Relation.objects.filter(~Q(r_owner_email=email),~Q(r_driver_email=email),~Q(r_sharer_email=email)).values('r_request_id'))
        print(orders)
        h = None
        h = [sub['r_request_id'] for sub in orders]
        if Ride.objects.filter(id__in=h,NumPassanger__lte=passen,status=0):
            orderList = Ride.objects.filter(id__in=h,NumPassanger__lte=passen,status=0)
        else:
            orderList  = None
        print(orderList)    
        drive = list(Relation.objects.filter(r_driver_email=request.session.get('user_email')).values('r_request_id'))
        res = None
        res = [ sub['r_request_id'] for sub in drive ]
   #     print(res)
        confirmList = None
        if Ride.objects.filter(id__in=res,status=1):
            confirmList = Ride.objects.filter(id__in=res,status = 1)
        else:
            confirmList = None
        
    else:
        orderList = None
   
        confirmList = None
        flag=1

         
    return render(request,'users/driver.html',{'isDriver':flag,'orderList':orderList,'confirmList':confirmList})   

        

def register(request):        
    if request.method=='POST':
        form = UserForm(request.POST)
 
        if (form.is_valid()):
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
             
            if password1 != password2:
                message = "Please enter same password twice"
                return render(request,'users/register.html',{'message':message,'form':form})
            if len(password1)<8:
                message = "Please enter password more than length of 8"
                return render(request,'users/register.html',{'message':message,'form':form})
               
            same = haha.objects.filter(email = email)
            if same:
                message = "Email has has been registered!"
                return render(request,'users/register.html',{'message':message,'form':form})

            new_user = haha()
               
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.email= form.cleaned_data.get('email')
            new_user.password = make_password(password1)
            new_user.status_flag = 0
            new_user.phone_number = form.cleaned_data.get('phone_number')
            new_user.save()
                             
            request.session.flush()
            return redirect('/login/')
    else:
        form = UserForm()
 
 
    return render(request,'users/register.html',{'form':form})

def login(request):
    if request.session.get('is_login',None):
        return redirect('/index/')        
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "Please check what you have entered"
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            message = "Please enter correct information"
            try:
                 user = haha.objects.get(email=email)
                 checkPassword = check_password(password,user.password)
                 if checkPassword == True:
                     request.session['is_login']=True
                     request.session['user_email']=user.email
                     request.session['user_id']=user.id
                     return redirect('/index/')
                 else:
                     message = "Incorrect password"
            except:
                message = "User dose not exist"
        
        return render(request, 'users/login.html', context={"message": message, 'login_form':login_form})
    else:
        login_form = LoginForm()
    return render(request,'users/login.html', {'login_form':login_form})

def request(request):    
    # display pages to request a ride
    if request.method =="POST":
        request_form = RideForm(request.POST)
        if request_form.is_valid():
            destination = request_form.cleaned_data.get('destination')
            arrivalTime = request_form.cleaned_data.get('arrivalTime')
            num = request_form.cleaned_data.get('NumPassanger')
            share = request_form.cleaned_data.get('CanShare')
#            new_request = Ride.objects.create(destination, arrivalTime, num, share)
            #new_request = Ride.objects.create();
            new_request = Ride()            
            new_request.destination = destination
            new_request.arrivalTime = arrivalTime
            new_request.NumPassanger = num           
            new_request.CanShare = share
            new_request.max_passanger = 100
            new_request.owner_email = request.session.get('user_email')
            #TODO: change to no/yes
            new_request.status = 0
            new_request.owner_id = request.session.get('user_id')
            new_request.save()

            # add to relation table
            new_relation = Relation()
            new_relation.r_request_id = new_request
            new_relation.r_owner_email = request.session.get('user_email')
            new_relation.save()
            
            return redirect('/display/')
            #return render(request,'rides/main.html')
    form = RideForm()
    return render(request, 'users/request.html', {'request_form':form})


def display_my_rides(request):
     requests = Ride.objects.filter(owner_email=request.session.get('user_email'))
     print(request.session.get('user_email'))
     #    return HttpResponse("a display pagexxxxxx")
     # requests = Ride.objects.filter(owner_email=request.session.get('user_email'))
     print(requests)
     #context = {'requests':requests}
     #filter driver
     drive = list(Relation.objects.filter(r_driver_email=request.session.get('user_email')).values('r_request_id'))
     print(drive)
     res = [ sub['r_request_id'] for sub in drive ]
     print(res)
     drivers = None
     if Ride.objects.filter(id__in=res):
         drivers = Ride.objects.filter(id__in=res)
     print(drivers)
     #TODO filter sharer
     share = list(Relation.objects.filter(r_sharer_email=request.session.get('user_email')).values('r_request_id'))
     share_res = [ sub['r_request_id'] for sub in drive ]
     sharers = None
     if Ride.objects.filter(id__in=share_res):
         sharers = Ride.objects.filter(id__in=share_res)
     print(sharers)    
     context = {'requests':requests, 'drivers':drivers, 'sharers':sharers}
     return render(request, "users/display.html", context=context)

def logout(request):
    if not request.session.get('is_login',None):
        #messages.info(request, 'You have not logged in!')
        return redirect("/login/")
    request.session.flush()
    #messages.info(request, 'Logout successfully')
    return redirect("/login/")
	
def addCar(request):
    form2 = CarForm(request.POST)
    if form2.is_valid():
                h = request.session.get('user_id',None) 
                new_user = haha.objects.filter(id = h).first()
                new_user.status_flag = '1'
                new_user.save()
                new_car = car.objects.create()
                new_car.driver_id = new_user.email
                new_car.vehicle_type =  form2.cleaned_data.get('vehicle_type')
                new_car.plate_number =  form2.cleaned_data.get('plate_number')
                                                              
                new_car.max_passanger =  form2.cleaned_data.get('max_passanger')
                new_car.save()
                return redirect('/profile/')
    return render(request,'users/newDriver.html',{'car':form2})

def profile(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    
    email = request.session.get('user_email',False)
            
    users = haha.objects.filter(email=email).first()
    cars = car.objects.filter(driver_id = email).first()
    if users.status_flag=='0':
        isDriver = 0
    else:
        isDriver = 1
    return render(request,'users/profile.html',{'isDriver':isDriver,'users':users,'cars':cars})

def profile_edit(request):
    user = request.session.get('user_email',False)
    new_user = haha.objects.filter(email=user).first()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.is_valid())
        if form.is_valid():                     
             new_user.first_name = form.cleaned_data.get('first_name')
             print(new_user.first_name)
             new_user.last_name = form.cleaned_data.get('last_name')
             new_user.email= form.cleaned_data.get('email')
                               
             new_user.vehicle_id =  form.cleaned_data.get('plate_number')
             new_user.phone_number = form.cleaned_data.get('phone_number')
             new_user.save()

        if new_user.status_flag=='1':
        
            car1 = CarForm(request.POST)
            if car1.is_valid():
                oldcar = car.objects.filter(driver_id = user).first()
                oldcar.driver_id = new_user.email
                oldcar.vehicle_type =  car1.cleaned_data.get('vehicle_type')
                oldcar.plate_number =  car1.cleaned_data.get('plate_number')                                                            
                oldcar.max_passanger =  car1.cleaned_data.get('max_passanger')
                oldcar.save()
        return redirect('/profile/')        
    else:
        UserForm1 = UserForm(initial={"first_name":new_user.first_name,"last_name":new_user.last_name,"phone_number":new_user.phone_number,"email":new_user.email})
        
        if new_user.status_flag == '1':
       
            oldcar = car.objects.filter(driver_id = user).first()
            CarForm1 = CarForm(initial={"vehicle_type":oldcar.vehicle_type,"plate_number":oldcar.plate_number,"max_passanger":oldcar.max_passanger})
            return render(request,'users/profile_edit.html',{'isDriver':1,'user_form':UserForm1,'car_form':CarForm1})
        else:
            return render(request,'users/profile_edit.html',{'isDriver':0,'user_form':UserForm1})
        
def rideDetail(request, request_id):
    response = "You're looking at the details of ride %s."
#    return HttpResponse(response % request_id)
    request_res = Ride.objects.get(pk=request_id)
    print(request_res)
    owner = haha.objects.get(email=request_res.owner_email)
    relations = Relation.objects.filter(r_request_id=request_id)
#    print(relation)
    try:
        relation = relations.first()
        driver_email = relation.r_driver_email;
        print(driver_email)
        driver = haha.objects.get(email=driver_email)
        vehilce = car.objects.get(driver_id=driver_email)   
    except:
        driver=None
        vehilce = None
    sharers = None
    try:
        sharers = Relation.objects.filter(r_request_id=request_id)
    except:
        sharers = None    
    return render(request, 'users/rideDetail.html', {'request_id':request_res, 'driver':driver, 'car':vehilce, 'owner':owner, 'sharers':sharers})
 #   return HttpResponse(response % request_id)


def edit_destination(request, request_id):
    request_res = Ride.objects.get(pk=request_id)
    print(request_res)
    if request.method == "POST":
        print("find post")
        form = editDestinationForm(request.POST)
        if form.is_valid():
            new_destination = form.cleaned_data.get('destination')
            request_res.destination = new_destination
            request_res.save()
            print(request_res.destination)
            return redirect('rideDetail', request_id=request_res.id)
#            return HttpResponseRedirect("ride/" % request_res.id)

    form = editDestinationForm()
    context = {'request':request_res, 'edit_form':form}
    return render(request, 'users/edit_destination.html', context=context)



def edit_time(request, request_id):
#     response = "You're editing details of ride %s."
#     return HttpResponse(response % request_id)
    request_res = Ride.objects.get(pk=request_id)
    print(request_res)
    if request.method == "POST":
        form = editTimeForm(request.POST)
        if form.is_valid():
            new_time = form.cleaned_data.get('arrivalTime')
            print(new_time)
            request_res.arrivaltime = new_time
            request_res.save()
            print(request_res.arrivaltime)
            return redirect('rideDetail', request_id=request_res.id)
#            return HttpResponseRedirect("ride/" % request_res.id)

    form = editTimeForm()
    context = {'request':request_res, 'edit_form':form}
    return render(request, 'users/edit_time.html', context=context)


def edit_num_passanger(request, request_id):
    request_res = Ride.objects.get(pk=request_id)
    print(request_res)
    if request.method == "POST":
        form = editNumForm(request.POST)
        if form.is_valid():
            new_num = form.cleaned_data.get('num')
            request_res.NumPassanger = new_num
            request_res.save()
            print(request_res.NumPassanger)
            return redirect('rideDetail', request_id=request_res.id)
#            return HttpResponseRedirect("ride/" % request_res.id)

    form = editNumForm()
    context = {'request':request_res, 'edit_form':form}
    return render(request, 'users/edit_num.html', context=context)



def index(request):
    return render(request, 'users/index.html');
    #return HttpResponse("This page is reserved for index")

def search(request):
    # display search form
    if request.method == "POST":
        form = UserSearchForm(request.POST)
        message = "Please check what you have entered"
        if form.is_valid():
            destination = form.cleaned_data.get('destination')
            time1 = form.cleaned_data.get('earlist_time')
            time2 = form.cleaned_data.get('latest_time')
            num = form.cleaned_data.get('num_pass')
            request.session['num']=num
            if(time2<=time1):
                    message = "latest time needs to be later than earlist time"
                    return render(request, 'users/search.html', {'form':form, 'message':message})
            else:
                print("trying to find data")
                try:
                #valid input trying to filter data from database
                    #results = Ride.objects.filter(max_passanger=num)
                    results = Ride.objects.filter(destination=destination, arrivaltime__gte=time1, arrivaltime__lte=time2, max_passanger__gte=num)
                    result = results.first()
                    print(result.max_passanger)
        
                    return render(request, 'users/search.html', {'form':form, 'results':results, 'owner_email':request.session.get('user_email')}) 
                except:
                    message = "no records are found"
        return render(request, 'users/search.html',  {'form':form, 'message':message})
    else:
        form = UserSearchForm()
    context = {'form':form}
    return render(request, 'users/search.html', context=context)



def join(request, request_id):
    request_res = Ride.objects.get(pk=request_id)
    request_res.max_passanger -= request.session.get('num') 
    #relation = Relation.objects.get(r_request_id = request_id)
    email = request.session.get('user_email')
    #try:
    relation = Relation.objects.filter(r_request_id = request_res.id, r_sharer_email__isnull=True)
    if not relation.count()==0:
        #add new one to model
        print("a")
        new_relation = Relation()
        new_relation.r_request_id = request_res
        new_relation.r_owner_email = request_res.owner_email
        new_relation.r_driver_email = relation.first().r_driver_email
        new_relation.r_sharer_email = email
        new_relation.sharer_num = request.session.get('num')
        new_relation.save()
    else:
        print("b")
        relation.r_sharer_email = email
        relation.sharer_num = request.session.get('num')
        relation.save()
    return redirect('/index/')
