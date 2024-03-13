import uuid
from django.shortcuts import redirect, render
from django.contrib import messages
from accounts.models import User

# Create your views here.

def home(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email Already Exists')
            return redirect('home')
        user = User.objects.create_user(email = email,password=password,username=email,token=str(uuid.uuid4()))
        messages.success(request,'Account Successfully Created , Please Verify Your Email')
    return render(request,'index.html')


def verify(request,token):
    user = User.objects.filter(token=token).first()
    if user:
        if not user.is_verified:
            user.is_verified=True
            user.save()
            messages.success(request,"Your account has been Verified Successfully")
        else:
            messages.success(request,"You account has already verified")
    else :
        messages.error(request,"Invalid Verification Token",'danger',fail_silently=True)
    return render(request,'verify.html')