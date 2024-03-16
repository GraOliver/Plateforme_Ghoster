from django.shortcuts import render,redirect
from django.http import Http404,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import LoginUser,UserChangeSign,UserCreationSign
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.views.generic import View
message_erreur ="Identifiant ou mot de passe incorecte"


class LoginAppView(View):
    """cette classe vas gérer la connexion dans la page de notre application

    Args:
        View : il herite de la classe générique Vieu pour sa gestion 
    """
    template ="Account.html"
    auth_form_class =LoginUser
    
    def get(self,request):
        """Elle vas gerer que le poste de l'application

        Args:
            request (): requette envoyer depui la form
        """
        form =self.auth_form_class()
        return render(request,self.template,{"form":form})
    
    def post(self,request):
        form =self.auth_form_class(request.POST)
        
        if request.method =='POST':
            user =authenticate(request,
                username=request.POST["username"],
                password=request.POST["password"]
            )
            
            if user is not None :
                login(request,user)
                return redirect("Article:index")
            else:
                messages.info(request,message_erreur)        
                
        return render(request,"Account.html",{"form":form})  

class LogoutUserView(View):
    """la deconnection de l'utilisateur 

    Args:
        View (_type_): _description_
    """
    direction ="Accounts:login"
    def get(self,request):
        logout(request)
        return redirect("Accounts:login")

class UserRegister(View):
    
    def get(self,request):
        pass
    def post(self,request):
        pass

def register_app(request):
    
    if request.method=='POST':
        form =UserCreationSign(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:indexOffApp")
    else:    
        form = UserCreationSign()
        
    return render(request,"register.html",{"form":form}) 

def user_change_pass(request):
    form =UserChangeForm()
    return render(request,"pass_forgeted.html",{"form":form})

def change_user(request):
    form =UserChangeForm()
    return render(request,"pass_forgeted.html",{"form":form})

def pass_forgeted(request):
    form =UserChangeForm()
    return render(request,"pass_forgeted.html",{"form":form})