import firebase_admin
import os
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from firebase_admin import credentials
from django.contrib import auth as django_auth
from .forms import RegisterManufacturerForm

app = settings.APP_NAME

auth = settings.FIREBASE.auth()

database = settings.FIREBASE.database()

storage = settings.FIREBASE.storage()

filepath = os.path.join(settings.BASE_DIR, 'DigiRC//service_account_key.json')
cred = credentials.Certificate(filepath)
firebase_admin.initialize_app(cred)


def user_details(self, context):
    if 'logged_status' in self.request.session:
        user = self.request.session['user']
        user_info = database.child('users').child(str(user['userId'])).child('profile').get()
        if user_info.val() is not None:
            for info in user_info.each():
                context.update({info.key(): info.val()})
    return context


def logged_user(users, email):
    if users.val() is not None:
        for user in users.each():
            if user.key().replace(',', '.') == email:
                return True
    return False


def get_logged_user_list(usertype):
    return database.child('users').child(usertype).get()


def process_login(request, usertype):
    email = request.POST.get('email')
    password = request.POST.get('password')
    users = get_logged_user_list(usertype)
    if logged_user(users, email):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            user = auth.refresh(user['refreshToken'])
            request.session['logged_status'] = True
            request.session['user'] = user
            request.session['usertype'] = usertype
            return True
        except:
            messages.error(request, f'Invalid Credentials')
            return False
    else:
        messages.error(request, f'Invalid Email or Password')
        return False


def check_user_exists(users, email):
    for user_type in users.each():
        for user_email in user_type.val():
            if user_email.replace(',', '.') == email:
                return True
    return False


def login(request, usertype):
    if request.method == 'POST':
        if process_login(request, str(usertype).lower()):
            path = str(usertype).lower() + "-dashboard"
            return redirect(path)
    return render(request, 'users/login.html',
                  context={'app': app, 'title': 'Login', 'usertype': usertype})


def register(request, usertype):
    if request.method == 'POST':
        form = RegisterManufacturerForm(request.POST, request.FILES)
        if form.is_valid():
            email = request.POST.get('email')
            users = database.child('users').get()
            if not check_user_exists(users, email):
                file_name = request.FILES['industry_license']
                if str(file_name).find('.jpg') == -1 and str(file_name).find('.png') == -1:
                    messages.error(request, f'License Must be in JPG/PNG Format')
                else:
                    try:
                        user = form.save()
                        user = user.__dict__
                        for key in {'_state', 'id'}:
                            user.pop(key)
                        path = os.path.join(settings.BASE_DIR, 'media') + "/" + str(user.get('industry_license'))
                        if str(file_name).find('.jpg') != -1:
                            file_name = 'license.jpg'
                        else:
                            file_name = 'license.png'
                        user.update({'industry_license': file_name, 'usertype': 'manufacturer'})
                        storage.child('manufacturer').child(str(user.get('email'))).child(str(file_name)).put(path)
                        database.child('requests').child('registration').child(
                            str(user.get('email')).replace('.', ',')).set(user)
                        os.remove(path)
                        messages.success(request, f'Applied for Registration')
                    except:
                        messages.error(request, f'System Error')
            else:
                messages.error(request, f'Email Already Registered')
        else:
            messages.error(request, f'Invalid Details')
    else:
        form = RegisterManufacturerForm()
    return render(request, 'users/register.html', context={'app': app, 'title': 'Register', 'usertype': usertype,'form': form})


def logout(request):
    context = {'app': app, 'title': 'Logout', 'usertype': str(request.session['usertype'])}
    django_auth.logout(request)
    return render(request, 'users/logout.html', context)


def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            auth.send_password_reset_email(email)
            messages.success(request,
                             f'Check your email for a link to reset your password. If it doesn’t appear within a few '
                             f'minutes, check your spam folder.')
        except:
            messages.error(request, f'Email address is not registered')
    return render(request, 'users/forgot_password.html', context={'app': app, 'title': 'Password Reset'})
