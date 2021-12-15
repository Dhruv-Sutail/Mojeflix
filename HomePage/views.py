from typing import final
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from .models import Content, Subscription,Usersubscription,Comment
from django.views.decorators.csrf import csrf_exempt
import razorpay


class HomeView(View):
    def get(self , request):
        return render(request,"Homepage/Home.html")

class LoginView(View):
    def get(self , request):
        return render(request,"Homepage/Login.html")

    def post(self,request):
        context = {}
        if request.method == "POST":
            username = request.POST['user']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                request.session['username'] = user.username
                return HttpResponseRedirect(reverse("profile"))
            else:
                context["error"] = "Enter Valid Credentials!!"
                return render(request , "Homepage/Login.html",context)

class RegisterView(View):    
    def post(self,request):
        context = {}
        if request.method == "POST":
            user = request.POST['user']
            email = request.POST['email']
            password = request.POST['password']
            userprofile = User(
                    username = user,
                    email = email,
                    password = make_password(password)
                )
            userprofile.save()
            context["success"] = "You have Registered Successfully! Please Login Now:)"
            return render(request, "Homepage/Login.html",context)
        else:
            context["error"] = "Some Error Occured Please Try Again:("
            return render(request, "Homepage/Login.html",context)

class LoginSuccess(View):
    def get(self , request):
        # name = request.session.get('username')
        # a = User.objects.filter(username=name).values_list('email', flat=True)
        # print(a)
        name = request.user
        # print(name)
        
        if Usersubscription.objects.filter(username=name).exists():
            a = Usersubscription.objects.filter(username=name)
            f_list = a[0].genre
            gen_str = ""
            for i in range(len(f_list)):
                if f_list[i]=="[" or f_list[i]=="]" or f_list[i]=="'" or f_list[i]==" ":
                   pass
                else:
                    gen_str = gen_str + f_list[i]
            print(gen_str)
            genre_list = gen_str.split(",")
            print(genre_list[0])
            if (len(genre_list)==1):
                if genre_list[0] == "Action":
                    content = Content.objects.filter(genre=1)
                    content3 = Content.objects.filter(genre=3)
                    content4 = Content.objects.filter(genre=4)
                    context = { 
                    "content": content,
                    "content3": content3,
                    "content4": content4
                    }
                    return render(request,"Homepage/Profile.html",context)
                elif genre_list[0] == "Comedy":
                    content = Content.objects.filter(genre=2)
                    content3 = Content.objects.filter(genre=3)
                    content4 = Content.objects.filter(genre=4)
                    context = { 
                    "content": content,
                    "content3": content3,
                    "content4": content4
                    }
                    return render(request,"Homepage/Profile.html",context)
            elif len(genre_list)==2:
                if genre_list[0] == "Action" or genre_list[1]=="Comedy":
                    content = Content.objects.filter(genre=1)
                    content1 = Content.objects.filter(genre=2)
                    content3 = Content.objects.filter(genre=3)
                    content4 = Content.objects.filter(genre=4)
                    context = { 
                    "content": content,
                    "content1": content1,
                    "content3": content3,
                    "content4": content4
                    }
                    return render(request,"Homepage/Profile.html",context)
     
        else:
           return render(request,"Homepage/choice.html")

    def post(self,request):
        if request.method == "POST":
            user = request.user
            sub = request.POST['subs']            
            subs = Subscription.objects.get(id=sub)
            genre = request.POST.getlist('genre')
            usersubs = Usersubscription(
                username = user,
                subscription = subs,
                genre = genre
            )
            usersubs.save()
            return HttpResponseRedirect(reverse("profile"))

class VideoPlayerView(View):
    def get(self,request,slug):
        user = request.user
        user_subs = Usersubscription.objects.filter(username=user).values_list('subscription', flat=True)[0]
        if user_subs == 1:
            movie_subs = Content.objects.filter(slug=slug).values_list('subscription', flat=True)[0]
            # print(movie_subs)
            if movie_subs == 1:
                video = Content.objects.filter(slug=slug)
                comments = Comment.objects.filter(slug=slug).order_by("-date")
                context = {
                    "video": video,
                    "comments":comments,
                }
                return render(request,"Homepage/video-player.html",context)    
            else:
                if request=="POST":
                    DATA = {
                        "amount": 499,
                        "currency": "INR",
                    }
                    client = razorpay.Client(auth=("rzp_test_Gj1BnBn6EMq45q", "FBsWx6ghc4IlPAAt1tMxLyuP"))
                    payment = client.order.create(data=DATA)
                    print(payment)
                return render(request,"Homepage/payment-gateway.html")
        else:
            video = Content.objects.filter(slug=slug)
            comments = Comment.objects.filter(slug=slug)
            context = {
                "video": video,
                "comments":comments,
            }
            return render(request,"Homepage/video-player.html",context)
        
    
    def post(self,request,slug):
        if request.method == "POST":
            user = request.user
            msg = request.POST['msg']
            rating = request.POST['rating']
            slug = request.POST['slug']            
            user_ratings = Comment(
                username = user,
                comment = msg,
                ratings = rating,
                slug = slug,
            )
            user_ratings.save()
            return HttpResponseRedirect(reverse("videoplayer",kwargs={'slug':slug}))

@csrf_exempt
def success(request):
    user = request.user
    t = Usersubscription.objects.get(username=user)
    t.subscription = Subscription.objects.get(id=2)
    t.save()
    return render(request,"Homepage/payment_success.html")

class LogoutView(View):
    def post(self, request):
        if request.method == "POST":
            logout(request)
            return HttpResponseRedirect(reverse("login"))