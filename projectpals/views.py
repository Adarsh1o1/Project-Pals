#created by me
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import category,post
from .models import post
from .forms import upload
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404

# Account actions and authentications

@login_required(login_url='loginpage')
def home(request): #main home page

    # return HttpResponse("home page <button><a href='/loginpage'>logout</a></button>")
    return render(request, 'home.html')


def signup(request): #signup page
    if request.method=='POST':
        username=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm-password')
        # if password!=confirm_pass:
        #     return HttpResponse("your password didn't match")
        # else:
        #     users=User.objects.create_user(username,email,password)
        #     users.save()
        #     return redirect("loginpage")
        # print(username,email,password,confirm_pass)

        if password==confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request,'this Email is already in use')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('loginpage')
        else:
            messages.info(request,"passwords didn't match")
            return redirect('signup')        
    return render(request, 'signup.html')

def loginpage(request): #login page
    if request.method=='POST':
        usernam=request.POST.get('username')
        passwor=request.POST.get('password')
        user=authenticate(request,username=usernam,password=passwor)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, "username or password is incorrect")
            # return redirect('login')
        # print(username,password)
    return render(request, 'login.html')

def Logout(request): #to logout
    logout(request)
    return redirect('loginpage')


# database tables

@login_required(login_url='loginpage')
def categories(request):
    name = category.objects.all()
    print(name)
    return render(request, 'category.html', {'names': name})

# @login_required(login_url='loginpage')
def posts(request):
    posts = post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

# @login_required(login_url='loginpage')
def embedded(request):
    posts = post.objects.filter(category=3)
    print(posts)
    return render(request, 'embedded.html', {'posts': posts})

# @login_required(login_url='loginpage')
def electronics(request):
    posts = post.objects.filter(category=6)
    print(posts)
    return render(request, 'electronics.html', {'posts': posts})


# forms to feed data to database models (post)
@login_required(login_url='loginpage')
def uploadpost(request):
    context={}
    if request.POST:
        forms=upload(request.POST,request.FILES)
        # print(request.FILES)
        if forms.is_valid():
            data=forms.save(commit=False)
            login_user=User.objects.get(username=request.user.username)
            data.user=login_user
            data.save()
            # context["status"]="{} created successfully".format(post.project_name)
            return redirect('home')
    # context["forms"]=upload
    context={
        "forms":upload, "status":"Post created successfully"
    }
    print(post.project_name)
    return render(request,'uploadpost.html',context)
from django.shortcuts import render, get_object_or_404
from .models import post

@login_required(login_url='loginpage')
def sendmail(request,pk,pk1):
    # gmail=request.user.id
    # mail=User.objects.get(id=gmail)
    # eemail=mail.email
    # print(eemail,mail,gmail)
    # Post = post.objects.select_related('user').get(pk=1)
    # recipient_email = Post.user.email
    # user=request.user
    # gmail=User.objects.get(email=recipient_email)
    # print(gmail)

# def post_detail(request, pk):
        # posts = get_object_or_404(post, pk=1)

        # user = user.posts.emailemail=pk
        # send_email_to_user(user.email)
    # return render(request, 'post_detail.html', {'post': post})

        posts = User.objects.get(id=pk)
        print(posts)
        mail_id=posts.email
        user=request.user.username
        user_mail=request.user.email
        print(user_mail)
        post_username=posts.username
        # project_nam=posts.project_name
        print(user,post_username)
        print(mail_id)
        detail=post.objects.get(id=pk1)
        # name=detail.project_name
        print(detail)


        # print(pk)
        context={
        "status":"mail sent successfully"
    }
        def send_email_to_user(email):
                    subject = "Request to Join Your Project Team as a Partner"
                    message = f'Hello {post_username}, {user} showed interest on your recently uploaded project "{detail}". You can contact him with the provided mail id {user_mail} '
                    from_email = 'alertscompanions@gmail.com'
                    recipient = [email]
                    send_mail(subject, message, from_email, recipient)
        send_email_to_user(mail_id)
        return render(request, 'mail.html',context)

