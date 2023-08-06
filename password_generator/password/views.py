from django.shortcuts import render, redirect
from .models import *
import random
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import re
import base64
import smtplib
from .forms import ForgottenPassword, UpdatePassword
from django.contrib.auth import get_user_model


#homepage view function
def index(request):

    salt_option = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0987654321@&$+$)"
    salt = "".join(random.choices(salt_option, k=8))


    if request.method == "POST":
        username = request.POST.get("username")
        site = request.POST.get("site")

        try:
            #check if the site already exist there can only be one password for each site
            if not Generator.objects.filter(username=username, site=site).exists():
                save_it = Generator.objects.create(username=username, site=site)
            else:
                messages.error(request, f"the site '{site}' for '{username}' already has a password")
                return redirect("index")
        #to prevent the error when there is no password in the database so that it can still create user

        except ObjectDoesNotExist:
            save_it = Generator.objects.create(username=username, site=site)

        #this part get the check box, store in a list and add to gen_password variable 
        choice = []
        uppercase =  request.POST.get('uppercase')
        lowercase = request.POST.get("lowercase")
        numbers = request.POST.get("numbers")
        special_char = request.POST.get("special-characters")
        if uppercase:
            choice.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if lowercase:
            choice.extend(list('abcdefghijklmnopqrstuvwxyz'))
        if numbers:
            choice.extend(list('0123456789'))
        if special_char:
            choice.extend(list('@#$%&-+()*?!;:'))

        length = int(request.POST.get("length", 12))

        for i in range(length):

            if choice:
                #save and display the password if choice is not empty
                gen_password = "".join(random.choices(choice,k=length))

                updated_gen_password = salt+" "+gen_password
                encode_updated_gen_password = base64.b64encode(updated_gen_password.encode("utf-8"))


                save_it.password = encode_updated_gen_password
                save_it.save()
                return redirect("dis_pass", username=username)
                break

            else:
                messages.error(request, "choose one of the option to generate password")
                break

    return render(request, "index.html", )


#view function for signup
def signup(request):

    #defining a function to validate user password
    def validate_password(password):
        regular_expression = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,20}$"
        pattern = re.compile(regular_expression)
        valid = re.search(pattern, password)
        return valid


    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        email = request.POST.get("email")

        #validate the password using the already defin function
        val_password = validate_password(password)

        #check if the username, email exist and if the two password are equal before creatting a user
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                if password == confirm_password:
                    if val_password:
                        User.objects.create_user( username=username, password=password, email=email)
                        messages.info(request, "account created successfully")
                        return redirect("signin")

                    else:
                        messages.error(request, "Not a strong password") 
                        return redirect("signup")
                else:
                    messages.error(request, "the password dont correspond")
            else:
                messages.error(request, "the email already exist")
        else:
            messages.error(request, "the username already exist")

    return render(request, "signup.html") 


#view function for signin
def signin(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(
                username=username, 
                password=password, )
        if user is not None:
            auth.login(request, user)
            return redirect("view_pass", username=username)
        
        else:
            messages.error(request, "incorrect username or password")
    return render(request, "signin.html")


def logout(request):
	auth.logout(request)
	return redirect("signin")


#view function to view your generated password
def dis_pass(request, username):

    #query the database to get the resent user who generated a password
    user = Generator.objects.filter(username=username).last()
    passwords = base64.b64decode(user.password).decode().split(" ")[-1]

    context = {
            "user":user,
            "passwords":passwords, 
            }
    return render(request, "dis_pass.html", context)


#view function to view all your generated password
def view_pass(request, username):

    #a search bar that help get a particular sites password
    search = request.GET.get("search", "")

    #the query of the search
    search_query = Generator.objects.filter(Q(site__icontains=search) | Q(site__iexact=search), username=request.user)


    #this is to iterate the returned query set and decode all the password for reference in the view_password.html file 

    output = ""
    for i in range(search_query.count()):

        output += base64.b64decode(search_query[i].password).decode().split(" ")[-1] + " "

    password_list = output.split(" ")
    password_list.remove("")#to remove the last comma in the list of decoded password

    context = {
            "searchs":search_query, 
            "passwords":password_list, 
            }
    return render(request, "view_pass.html", context)


def forgotten(request): 
    if request.method == "POST":

        forgotten_password = ForgottenPassword(request.POST)
        if forgotten_password.is_valid():
            username = forgotten_password.cleaned_data["username"]
            email = forgotten_password.cleaned_data["email"]

            code = "".join(random.choices("0987654321", k=6))
            USER = "joshuajosephizzyjosh@gmail.com"
            PASSWORD = "fdbcgktkbkebfjhm"

            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(USER, PASSWORD)
            server.sendmail(USER, [email], code)


            messages.info(request, "email sent check for you mail for code")

            return redirect("insert",code=code)
        else:
            messages.error(request, "please validate all your input field")
    else:
        forgotten_password = ForgottenPassword()
    return render(request, "forgotten.html", {"forgotten_password":forgotten_password})



def update(request):

    if request.method == "POST":
        update_pass = UpdatePassword(request.POST)
        if update_pass.is_valid():
            username = update_pass.cleaned_data["username"]
            password = update_pass.cleaned_data["password"]
            con_password = update_pass.cleaned_data["confirm_password"]

            if password == con_password:
                if User.objects.filter(username=username).exists():
                    user = get_user_model().objects.get(username=username)
                    user.set_password = password
                    user.save()
                    messages.info(request, "password successfully updated")
                    return redirect("signin")

                else:
                    messages.error(request, "the username inputed does not exists")
            else:
                messages.error(request, "both password does not match")
        else:
            messages.error(request, "please verify your inputs")
    else:
        update_pass = UpdatePassword()

    return render(request, "update.html", {"update_pass":update_pass})


def insert(request,code):
    if request.method == "POST":
        insert = Insert(request.POST)
        if insert.is_valid():
            user_code = insert.cleaned_data["code"]

            if code == str(user_code):
                return redirect("update_pass")
            else:
                messages.error(request,"invalid code")
        else:
            messages.error(request,"please fill form data properly")
    else:
        insert = Insert()
    return render(request,"insert.html",{"insert":insert})