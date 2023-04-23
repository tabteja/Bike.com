from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,permission_required
from app.models import *
from django.contrib import messages, auth
from django.views.generic import *
from app.models import User
from django.shortcuts import HttpResponseRedirect
from django.db.models import Q
from app.forms import *
from app.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from django.db.models import F


# Create your views here.

############### -  INDEX  - ###############

def indexview(request):
    if request.user.is_authenticated and request.user.role == "seller":
        return redirect('dashboard')
    elif request.user.is_authenticated and request.user.role == "buyer":
        return redirect('home')
    elif request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin_page')
    else:
        v = Vehicle.objects.all().order_by('-id')[:4]
        return render(request,'index.html',{'v':v })


def vehicles(request):
    v = Vehicle.objects.all()
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    return render(request,'vehicles.html',{'v':v,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


def vehicle_details(request,id):
    vd = Vehicle.objects.get(id=id)
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    return render(request,'vehicle_details.html',{'vd':vd,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})
    
    
def search(request):
    query = request.GET['query']
    s = Vehicle.objects.filter(Q(title__icontains=query) | Q(location__icontains=query))
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    return render(request, 'search.html', {'s':s,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


def companies(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    return render(request,'companies.html',{'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


def services(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    m = Membership_Applicants.objects.all()
    b = Book.objects.all()
    if request.method == 'POST':
        if not Membership_Applicants.objects.filter(email=request.POST['email']):
            return render(request, 'services.html')
        if Book.objects.filter(email=request.POST['email']):
            messages.warning(request,'You have already a booked a service..!')
            return render(request, 'already_booked_service.html')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        service_date = request.POST['service_date']
        user = request.user
        s = Book.objects.create(user=user,first_name=first_name,last_name=last_name,email=email,address=address,service_date=service_date)
        s.save()
        messages.success(request,'You have booked a service..! shortly you will get a mail')
        return render(request, 'service_payment.html', {'s': s})
    return render(request,'services.html',{'nu':nu,'ns':ns,'nb':nb,'nm':nm,'m':m,'b':b,'bk':bk})


@login_required(login_url='login')
def service_payment(request,id):
    s = Book.objects.get(id=id)
    return render(request,'service_payment.html',{'s':s})


def about(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    return render(request,'about.html',{'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


def blog(request):
    b = Blog.objects.all()
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    return render(request,'blog.html',{'b': b,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


def blog_details(request, id):
    p = get_object_or_404(Blog, id=id)
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    if p:
        p.views = p.views + 1
        p.save()
        p.update_views()
    return render(request, "blog_details.html", {'p': p,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


def contact(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        description = request.POST['description']
        c = Contact.objects.create(email=email,subject=subject,description=description)
        c.user = request.user
        c.save()
        messages.success(request,'Thanks for contacting us.. will get back soon...!')
        return render(request,'contact.html',{'c': c})
    else:
        return render(request,'contact.html',{'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})
    

@login_required(login_url='login')
def profile(request):   
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    return render(request, 'profile.html',{'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


@login_required(login_url='login')
def add_profile(request):
    if request.method == 'POST':
        profile_photo = request.FILES['profile_photo']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        p = Profile.objects.create(profile_photo=profile_photo,first_name=first_name,last_name=last_name,email=email)
        p.user = request.user
        p.save()
        messages.success(request,'Profile added successfully...!')
        return render(request, 'profile.html',{'p': p})
    return render(request, 'add_profile.html')


@login_required(login_url='login')
def memberships(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    if request.method == 'POST':
        if Membership_Applicants.objects.filter(email=request.POST['email']):
            messages.warning(request,'You have already a membership..!')
            return render(request, 'already_subscribed.html')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        name = request.POST['name']
        today = datetime.datetime.now()
        start_date = datetime.datetime(today.year, 1, 1)
        end_date = datetime.datetime(today.year, 12, 28)
        user = request.user
        subscription = Membership_Applicants.objects.create(user=user,first_name=first_name,last_name=last_name,email=email,name=name,start_date=start_date,end_date=end_date)
        subscription.save()
        messages.success(request,'You have purchased a subscription plan successfully..! shortly you will get a mail')
        return render(request, 'payment_gateway.html', { 'subscription': subscription })
    return render(request, 'memberships.html',{'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


@login_required(login_url='login')
def payment_gateway(request,id):
    p = Membership_Applicants.objects.get(id=id)
    return render(request,'payment_gateway.html',{'p':p})


@login_required(login_url='login')
def already_subscribed(request,id):
    m = Membership_Applicants.objects.get(user_id=id)
    messages.warning(request,'You have already a membership..!')
    return render(request,'already_subscribed.html', {'m':m})


@login_required(login_url='login')
def book(request,id):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    b = Membership_Applicants.objects.get(user_id=id)
    if request.method == 'POST':
        if Book.objects.filter(email=request.POST['email']):
            messages.warning(request,'You have already a booked a service..!')
            return render(request, 'book_details.html')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        name = request.POST['name']
        service_date = request.POST['service_date']
        user = request.user
        s = Book.objects.create(user=user,first_name=first_name,last_name=last_name,email=email,name=name,service_date=service_date)
        s.save()
        messages.success(request,'You have booked a service..! shortly you will get a mail')
        return render(request, 'book_details.html', { 's': s})
    return render(request, 'book.html',{'nu':nu,'ns':ns,'nb':nb,'nm':nm,'b':b,'bk':bk})


@login_required(login_url='login')
def book_details(request, id):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    b = Book.objects.get(user_id=id)
    return render(request, "book_details.html", {'nu':nu,'ns':ns,'nb':nb,'nm':nm,'b':b,'bk':bk})


@login_required(login_url='login')
def already_booked_service(request,id):
    al = Book.objects.get(user_id=id)
    m = Membership_Applicants.objects.get(user_id=id)
    messages.warning(request,'You have already booked a service..!')
    return render(request,'already_booked_service.html', {'al':al,'m':m})


class LoginView(FormView):
    """
        Provides the ability to login as a user with an email and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'login.html'

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)


###############  -  SELLER  -  ###############

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated and request.user.role == 'seller':
        v = Vehicle.objects.all().order_by('-id')[:4]
    return render(request,'dashboard.html',{"v": v})


class RegisterSellerView(CreateView):
    model = User
    form_class = SellerRegistrationForm
    template_name = 'seller_register.html'
    success_url = 'dashboard'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            messages.success(request,'Signup done successfully...!')
            return redirect('login')
        else:
            return render(request, 'seller_register.html', {'form': form})
        

@login_required(login_url='login')
def add_vehicle(request):
    if request.user.is_authenticated and request.user.role == 'seller':
        if request.method == 'POST':
            image1 = request.FILES['image1']
            image2 = request.FILES['image2']
            image3 = request.FILES['image3']
            title = request.POST['title']
            brand = request.POST['brand']
            model_type = request.POST['model_type']
            model_year = request.POST['model_year']
            km_run = request.POST['km_run']
            description = request.POST['description']
            price = request.POST['price']
            phone = request.POST['phone']
            location = request.POST['location']
            city = request.POST['city']
            a = Vehicle.objects.create(image1=image1,image2=image2,image3=image3,title=title,brand=brand,model_type=model_type,model_year=model_year,km_run=km_run,description=description,price=price,phone=phone,location=location,city=city)
            a.save()
            messages.success(request,'New vehicle added successfully..!')
            return redirect('vehicles')
    return render(request,'add_vehicle.html')


########### - BUYER - ###########

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated and request.user.role == 'buyer':
        v = Vehicle.objects.all().order_by('-id')[:4]
        if request.method == 'POST':
            year = request.POST['year']
            kilometers = request.POST['kilometers']
            c = Price_suggestion.objects.create(year=year,kilometers=kilometers)
            c.save()
            price = ((int(kilometers)) - int(year) / 2) * 10
            return render(request, 'home.html', {'price': price})
    return render(request,'home.html',{"v": v})


@login_required(login_url='login')
def buying(request, id):
    if request.user.is_authenticated and request.user.role == 'buyer':
        vehicle = Vehicle.objects.get(id=id)
        if request.method == 'POST':
            title = request.POST['title']
            brand = request.POST['brand']
            model_type = request.POST['model_type']
            model_year = request.POST['model_year']
            km_run = request.POST['km_run']
            price = request.POST['price']
            location = request.POST['location']
            city = request.POST['city']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            b = Buyer_Applicants.objects.create(user=request.user,vehicle=vehicle,title=title,brand=brand,model_type=model_type,model_year=model_year,km_run=km_run,price=price,location=location,city=city,first_name=first_name,last_name=last_name,email=email)
            b.save()
            vehicle.is_available = False
            vehicle.save()
            messages.success(request,'You have purchased this vehicle successfully..! shortly you will get a mail')
            return render(request, 'success_page.html', {'vehicle': vehicle , 'b':b})
        return render(request, 'buying.html', {'vehicle': vehicle})
    else:
        return render(request,'home.html')


@login_required(login_url='login')
def success_page(request, id):
    b = Buyer_Applicants.objects.get(id=id)
    return render(request, 'success_page.html', {'b': b})


class RegisterBuyerView(CreateView):
    model = User
    form_class = BuyerRegistrationForm
    template_name = 'buyer_register.html'
    success_url = 'home'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            messages.success(request,'Signup done successfully...!')
            return redirect('login')
        else:
            return render(request, 'buyer_register.html', {'form': form})


########### - ADMIN - ###########


@permission_required('is_superuser')
def manage_data(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    return render(request,'manage.html',{'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


@permission_required('is_superuser')
def admin_page(request):
    v = Vehicle.objects.all().order_by('-id')[:4]
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    b = Book.objects.all().order_by('-id')[:1]
    return render(request,'admin_page.html',{'v':v,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'b':b,'bk':bk})


# Blog #   

@permission_required('is_superuser')
def add_blog(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    if request.user.is_superuser:
        if request.method == 'POST':
            title = request.POST['title']
            subject = request.POST['subject']
            images = request.FILES['images']
            description = request.POST['description']
            b = Blog.objects.create(title=title,subject=subject,images=images,description=description)
            b.user = request.user
            b.save()
            messages.success(request,'New Blog added successfully..!')
            return redirect('blog')
    return render(request,'add_blog.html',{'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})

@permission_required('is_superuser')
def edit_blog(request, id):  
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    blog = Blog.objects.get(id=id)  
    return render(request,'edit_blog.html', {'blog':blog,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})  

@permission_required('is_superuser')
def update_blog(request, id):  
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    blog = Blog.objects.get(id=id)  
    form = BlogForm(request.POST, instance = blog)  
    if form.is_valid():  
        form.save()  
        return redirect("blog")  
    return render(request, 'update_blog.html', {'blog': blog,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk}) 

@permission_required('is_superuser')
def destroy_blog(request, id): 
    blog = Blog.objects.get(id=id)  
    blog.delete()  
    return redirect("blog")


# Vehicles #   

@permission_required('is_superuser')
def edit_vehicle(request, id): 
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    vehicle = Vehicle.objects.get(id=id)  
    return render(request,'edit_vehicle.html', {'vehicle':vehicle,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})  

@permission_required('is_superuser')
def update_vehicle(request, id):  
    vehicle = Vehicle.objects.get(id=id)  
    form = VehicleForm(request.POST, instance = vehicle)  
    if form.is_valid():  
        form.save()  
        return redirect("vehicles")  
    return render(request, 'update_vehicle.html', {'vehicle': vehicle}) 

@permission_required('is_superuser')
def destroy_vehicle(request, id):
    vehicle = Vehicle.objects.get(id=id)  
    vehicle.delete()  
    return redirect('vehicles')


# Contacts #   

@permission_required('is_superuser')
def all_contacts(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    ac = Contact.objects.all()
    return render(request,'all_contacts.html',{'ac': ac,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})

@permission_required('is_superuser')
def edit_contact(request, id):  
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    contact = Contact.objects.get(id=id)  
    return render(request,'edit_contact.html', {'contact':contact,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})  

@permission_required('is_superuser')
def update_contact(request, id): 
    contact = Contact.objects.get(id=id)  
    form = ContactForm(request.POST, instance = contact)  
    if form.is_valid():  
        form.save()  
        return redirect("all_contact")  
    return render(request, 'update_contact.html', {'contact': contact}) 

@permission_required('is_superuser')
def destroy_contact(request, id):  
    contact = Contact.objects.get(id=id)  
    contact.delete()  
    return redirect('all_contact')


# Membership Users #  

@permission_required('is_superuser')
def all_memberships_applicants(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    memberships_applicants = Membership_Applicants.objects.all()
    return render(request,'all_memberships_applicants.html', {'memberships_applicants': memberships_applicants,'bk':bk,'nu':nu,'ns':ns,'nb':nb,'nm':nm}) 

@permission_required('is_superuser')
def edit_memberships_applicants(request, id):  
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    memberships_applicants = Membership_Applicants.objects.get(id=id)  
    return render(request,'edit_memberships_applicants.html', {'memberships_applicants':memberships_applicants,'bk':bk,'nu':nu,'ns':ns,'nb':nb,'nm':nm})  

@permission_required('is_superuser')
def update_memberships_applicants(request, id):
    memberships_applicants = Membership_Applicants.objects.get(id=id)  
    form = Membership_ApplicantsForm(request.POST, instance = memberships_applicants)  
    if form.is_valid():  
        form.save()  
        return redirect("all_memberships_applicants")  
    return render(request, 'update_memberships_applicants.html', {'memberships_applicants': memberships_applicants}) 

@permission_required('is_superuser')
def destroy_memberships_applicants(request, id): 
    memberships_applicants = Membership_Applicants.objects.get(id=id)  
    memberships_applicants.delete()  
    return redirect('all_memberships_applicants')


# Buyer Users #  

@permission_required('is_superuser')
def all_buyers_applicants(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    buyers_applicants = Buyer_Applicants.objects.all()
    return render(request,'all_buyers_applicants.html', {'buyers_applicants': buyers_applicants,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk}) 

@permission_required('is_superuser')
def edit_buyers_applicants(request, id): 
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    buyers_applicants = Buyer_Applicants.objects.get(id=id)  
    return render(request,'edit_buyers_applicants.html', {'buyers_applicants':buyers_applicants,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})  

@permission_required('is_superuser')
def update_buyers_applicants(request, id):  
    buyers_applicants = Buyer_Applicants.objects.get(id=id)  
    form = Buyer_ApplicantsForm(request.POST, instance = buyers_applicants)  
    if form.is_valid():  
        form.save()  
        return redirect("all_buyers_applicants")  
    return render(request, 'update_buyers_applicants.html', {'buyers_applicants': buyers_applicants}) 

@permission_required('is_superuser')
def destroy_buyers_applicants(request, id): 
    buyers_applicants = Buyer_Applicants.objects.get(id=id)  
    buyers_applicants.delete()  
    return redirect('all_buyers_applicants')


# User #
@permission_required('is_superuser')
def user_data(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    ud = User.objects.all()
    return render(request,'user_data.html', {'ud': ud,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})


# Service slots #
@permission_required('is_superuser')
def all_service_slots(request):
    nu = User.objects.all().order_by('-id')[:2]
    ns = Vehicle.objects.all().order_by('-id')[:2]
    nb = Buyer_Applicants.objects.all().order_by('-id')[:2]
    nm = Membership_Applicants.objects.all().order_by('-id')[:2]
    bk = Book.objects.all().order_by('-id')[:2]
    ss = Book.objects.all().order_by('-id')
    return render(request,'all_service_slots.html', {'ss': ss,'nu':nu,'ns':ns,'nb':nb,'nm':nm,'bk':bk})