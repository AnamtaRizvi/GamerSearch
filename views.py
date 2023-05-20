from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models import Q
from .models import User,followers,followings,gamer,profile,game
# Create your views here.
def index(request):
    u=request.user
    
    try:
     g=gamer.objects.get(gamingname=u)
     fer=followings.objects.get(name=g.gamingname)
     f=fer.following.all()
     count1=f.count()
     return render(request, "search/index.html",{
            "gamers":f,})
    except:
      try:
       g=gamer.objects.exclude(gamingname=u)
      except:
        g=gamer.objects.all()
      return render(request, "search/index.html",{ 
        "gamers":g })
def search(request):
    if request.method == "POST":
        si=request.POST["s"]
        try:
         s=profile.objects.get(role=si)
         g=gamer.objects.filter(Q(r1=s)|Q(r2=s)|Q(r3=s))
        except:
            pass
        try:
         s=game.objects.get(role=si)
         g=gamer.objects.filter(Q(g1=s)|Q(g2=s)|Q(g3=s))
        except:
            pass
        try:
          g=gamer.objects.filter(location=s)
        except:
            pass
        try:
          s=User.objects.get(username=si)
          g=gamer.objects.filter(gamingname=s)
        except:
           pass
        return render(request, "search/index.html",{ 
        "gamers":g })


       
    
    
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "search/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "search/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        f_name=request.POST["fname"]
        l_name=request.POST["lname"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "search/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name=f_name
            user.last_name=l_name
            user.save()
        except IntegrityError:
            return render(request, "search/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        s=profile.objects.all()
        gm=game.objects.all()
        return render(request, "search/Accinfo.html",{
            "skills":s,"games":gm
        })
    else:
        return render(request, "search/register.html")

def Account(request):
    f=0
    if request.method=="POST":
        gm=gamer.objects.all()
        g=request.user
        st=request.POST["Description"]
        m=request.POST["matches"]
        w=request.POST["win"]
        k=request.POST["kill"]
        d=request.POST["damage"]
        l=request.POST["level"]
        loc=request.POST["location"]
        i=request.FILES['X']
        ch=request.POST.getlist("check")
        chg=request.POST.getlist("checkg")
        n1=request.user.get_full_name()
        game1=game.objects.get(name=chg[0])
        game2=game.objects.get(name=chg[1])
        game3=game.objects.get(name=chg[2])
        s1=profile.objects.get(role=ch[0])
        s2=profile.objects.get(role=ch[1])
        s3=profile.objects.get(role=ch[2])
        try:
            gm=gamer.objects.get(gamingname=g)
        except:
            gamer.objects.create(fname=n1,image=i,location=loc,gamingname=g,status=st,matches=m,win=w,kill=k,damage=d,r1=s1,r2=s2,r3=s3,level=l,g1=game1,g2=game2,g3=game3)
        else:
          up=gamer(id=gm.id,fname=n1,status=st,image=i,location=loc,matches=m,win=w,kill=k,damage=d,r1=s1,r2=s2,r3=s3,level=l,g1=game1,g2=game2,g3=game3)
          up.save(update_fields=['fname','image','matches', 'win','kill','damage','location','status','r1','r2','r3','g1','g2','g3','level'])
        return HttpResponseRedirect(reverse("index"))
        
        
def gprofile(request,fid):
    
    g=gamer.objects.get(id=fid)
    try:
      fer=followings.objects.get(name=g.gamingname)
      f=fer.following.all()
      count1=f.count()
    except:
        count1=0
    try:
      fer2=g.following.all()
      count2=fer2.count()
    except:
        count2=0
    return render(request, "search/Acc.html",{
            "gamer":g,"fwerc":count2,"fwingc":count1
            }
    )
def editacc(request):
     u=request.user
     s=profile.objects.all()
     gm=game.objects.all()
     g1=gamer.objects.get(gamingname=u)
     return render(request, "search/Accinfo.html",{
            "skills":s,"games":gm, "gamer":g1, 
        })

def follow(request,gid):
    if request.method=="POST":
        u=request.user
        g=gamer.objects.get(id=gid)
        try:
            f1=followings.objects.get(name=u)
        except:
            followings.objects.create(name=u)
            f1=followings.objects.get(name=u)

        f1.following.add(g)
        
        return HttpResponseRedirect(reverse("gprofile", args=(g.id,)))


# Create your views here.
def f_wers(request,gid):
    g=gamer.objects.get(id=gid)
    fer=g.following.all()
    return render(request, "search/followers.html",{
            "followers":fer,
        })

def f_wings(request,gid):
    g=gamer.objects.get(id=gid)
    fer=followings.objects.get(name=g.gamingname)
    f=fer.following.all()
    count1=f.count()
    return render(request, "search/followings.html",{
            "followings":f,})
def myaccount(request):
    u=request.user
    g=gamer.objects.get(gamingname=u)
    return render(request, "search/Acc.html",{
            "gamer":g,"message":u,
            })
