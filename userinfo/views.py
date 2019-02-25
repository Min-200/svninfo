from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def Loginindex(requset):

    return render(requset,"index.html")

def login(request):
        print  "start login"
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            print username,password
            user = auth.authenticate(username=username,password=password)

            print user
            if user is not None:
                print "user is authenticate"
                auth.login(request,user)
                request.session["user"] = username
                return render(request,"index.html")


            else:
                print "user is not authenticate"
#            return render(request,"index.html",{"error":"passwd if err"})
                return HttpResponse("User is not authenticate")

        return render(request,"login.html")

@login_required()
def logout(request):
    auth.logout(request)
    print  request.user
    response = HttpResponseRedirect("index.html")
    return response
