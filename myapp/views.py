from .models import Product, Carousel,Contact, Blog
from django.contrib import messages
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render,HttpResponse
from django.core.mail import send_mail
from myproject.settings import EMAIL_HOST_USER
import random
from django.conf import settings

def Index(request):
    products = Product.objects.all()
    carousels = Carousel.objects.all()
    context = {
        'products': products,
        'carousels': carousels
    }
    return render(request, 'myapp/index.html', context)

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'myapp/blog.html', context)

def blog_post(request, id):
    blog = Blog.objects.filter(post_id=id)
    return render(request, 'myapp/blogpost.html', {'blog': blog[0]})

def About(request):
    return render(request,'myapp/about.html')

def Services(request):
    return render(request,'myapp/services.html')
def ViewProduct(request, id):
    # Fetch the product using id
    product = Product.objects.filter(id=id)

    return render(request, 'myapp/productview.html', {'product':product[0]})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,mobile=mobile,desc=desc)
        contact.save()
        messages.success(request, "Your details and message have been saved. Our executive will contact you in next 24hrs.")

    return render(request,'myapp/contact.html')

def Signup(request):
    return render(request,'myapp/signup.html')


def Signup_user(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        # Checking for erroneous inputs
        if len(username) > 20:
            messages.error(request, "Your username must be under 20 characters...")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request, "Username must only contain alphabet and numbers...")
            return redirect('signup')
        if password != cpassword:
            messages.error(request, "Password does not match...")
            return redirect('signup')
        
        # Checking if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
            return redirect('signup')

        # Creating user
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        otp = random.randint(100000, 999999)
        message = f"Hello {fname} {lname}!\n\nWelcome to Nik InZone. We're excited that you are joining us.\n\nYour OTP for verification is: {otp}\n\nPlease enter this OTP on the verification page to complete the registration process.\n\nThank you!\n\nBest regards,\nThe Nik InZone Team"
        send_mail("Welcome to Nik InZone - OTP Verification", message, EMAIL_HOST_USER, [email], fail_silently=True)

        request.session['otp'] = otp  # Storing OTP in session for verification
        request.session['email'] = email  # Storing email in session for verification
        
        return redirect('verify')  # Redirecting to the verification page
    
    # Redirect to signup page if the request method is not POST
    return redirect('signup')



def Verify(request):
    if 'otp' in request.session and 'email' in request.session:
        if request.method == 'POST':
            otp = request.POST.get('otp')
            email = request.session['email']
            
            # Check if the OTP is valid
            if otp == str(request.session['otp']):
                del request.session['otp']  # Remove OTP from session
                del request.session['email']  # Remove email from session
                
                messages.success(request, "Your account has been successfully created and verified. Please log in to continue.")
                return redirect('login')
            else:
                messages.error(request, "Invalid OTP. Please try again.")
                return redirect('verify')
        
        # Redirect to the verification page if the request method is not POST
        return render(request, 'myapp/verify.html')
    
    # Redirect to signup page if the OTP and email are not in the session
    return redirect('signup')

def Login(request):
    return render(request, 'myapp/login_vp.html')

def Login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('apphome')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('login')
    else:
        return redirect('login')


def Logout(request):
    logout(request)
    messages.success(request, "Successfully Loged Out")
    return redirect('apphome')
# Send the OTP to the user via email
        