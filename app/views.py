# Import necessary modules
from django.shortcuts import render, redirect
from .models import UserAccount, TempStatus  # Importing UserAccount and TempStatus models
from .form import UserAccountForm  # Importing UserAccountForm from forms.py
from django.contrib.auth import logout  # Importing logout function


# Views for User Authentication and Management

# Render the signup page
def signup(request):
    return render(request, 'signup.html')


# Handle signup form submission
def signupaction(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST['txtusername']
        password = request.POST['txtpassword']
        firstname = request.POST['txtfirstname']
        lastname = request.POST['txtlastname']
        address = request.POST['txtaddress']
        mobile = request.POST['txtmobile']
        email2 = request.POST['txtemail']
        status = 0
        role = 'user'
        # Create new UserAccount object and save it to the database
        useraccount = UserAccount.objects.create(username=username, password=password, role=role,
                                                  firstname=firstname, lastname=lastname, address=address,
                                                  mobile=mobile, email=email2, status=status)
        try:
            useraccount.save()
            return redirect(login)
        except:
            errmsg = 'User Registration Failed'
            return render(request, 'signup.html', {'errmsg': errmsg})
    else:
        return redirect(signup)


# Render the home page based on user role
def home(request):
    role = request.session['role']
    if role == 'admin':
        return render(request, 'adminhome.html')
    else:
        return render(request, 'userhome.html')


# Render the login page
def login(request):
    form = UserAccountForm()
    return render(request, 'login.html', {'form': form})


# Handle login form submission
def loginaction(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = UserAccount.objects.filter(username=username, password=password, status=1).first()
        if user:
            # Update temporary status to "Online" and store user information in session
            TempStatus.objects.update_or_create(username=username, defaults={'status': 'Online'})
            request.session['username'] = user.username
            request.session['role'] = user.role
            # Redirect to appropriate home page based on user role
            if user.role == "admin":
                return render(request, 'adminhome.html')
            else:
                return render(request, 'userhome.html')
        else:
            form = UserAccountForm()
            # Render login page with error message
            return render(request, 'login.html', {'errmsg': 'Invalid username or password, or your account is not approved by the admin', 'form': form})
    else:
        return redirect(login)


# Handle user logout
def logout(request):
    # Update temporary status to "Offline" and clear user session
    TempStatus.objects.update_or_create(username=request.session.get('username'), defaults={'status': 'Offline'})
    request.session.flush()
    return redirect('login')


# Views for User Account Management

# Render the edit login page
def editlogin(request, username):
    login = UserAccount.objects.get(username=username)
    return render(request, 'editlogin.html', {'login': login})


# Handle updating user login details
def updatelogin(request, id):
    login = UserAccount.objects.get(userid=id)
    form = UserAccountForm(request.POST, instance = login)
    if form.is_valid():
        form.save()
        return render(request,'editusers.html')
    else:
        login = UserAccount.objects.get(userid=id)
        return render(request,'editlogin.html', {'login':login})


# Handle deleting user login
def deletelogin(request, id):
    login = UserAccount.objects.get(userid=id)
    login.delete()
    logins = UserAccount.objects.all()
    return render(request, 'adminhome.html', {'logins': logins})


# Render the edit profile page
def editprofile(request):
    username = request.session['username']
    login = UserAccount.objects.get(username=username)
    return render(request, 'editprofile.html', {'login': login})


# Handle updating user profile details
def updateprofile(request):
    username=request.session['username']
    firstname=request.POST['txtfirstname']
    lastname=request.POST['txtlastname']
    address=request.POST['txtaddress']
    mobile=request.POST['txtmobile']
    email=request.POST['txtemail']
    login=UserAccount.objects.get(username=username)
    try:
        login.firstname=firstname
        login.lastname=lastname
        login.address=address
        login.mobile=mobile
        login.email=email
        login.save()
        return redirect(home)
    except:
        errmsg='Update Failed'
        username=request.session['username']
        login = UserAccount.objects.get(username=username)
        return render(request,'editprofile.html', {'login':login,'errmsg':errmsg})


# Handle custom logout action
def custom_logout(request):
    logout(request)
    return redirect('login')


# Render the change password page
def changepassword(request):
    return render(request, 'changepassword.html')


# Handle updating user password
def updatepassword(request):
    password=request.POST['password']
    newpassword=request.POST['newpassword']
    confirmpassword=request.POST['confirmpassword']
    username=request.session['username']
    login=UserAccount.objects.get(username=username)
    p=login.password
    if p==password:
        if newpassword==confirmpassword:
            login.password=newpassword
            login.save()
            errmsg='Password changed successfully'
            return render(request,'changepassword.html',{'errmsg':errmsg})
        else:
            errmsg='New Password and Confirm Password must be the same'
            return render(request,'changepassword.html',{'errmsg':errmsg})
    else:
        errmsg='Invalid Current Password'
        return render(request,'changepassword.html',{'errmsg':errmsg})


# Views for Admin Functions

# Render the page to validate user accounts
def validateuser(request):
    logins = UserAccount.objects.filter(status=0)
    return render(request, 'validateuser.html', {'logins': logins})


# Approve a user account
def approveuser(request, username):
    login = UserAccount.objects.get(username=username)
    login.status = 1
    login.save()
    return redirect(validateuser)


# Reject a user account
def rejectuser(request, username):
    login = UserAccount.objects.get(username=username)
    login.delete()
    return redirect(validateuser)


# Render the page to edit user accounts
def editusers(request):
    logins = UserAccount.objects.all()
    return render(request, 'editusers.html', {'logins': logins})


# Views for User Profile Display

# Render the base profile page
def profilebase(request):
    user_accounts = UserAccount.objects.order_by('username')
    status_list = TempStatus.objects.order_by('username')
    return render(request, "profilebase.html", {'user_accounts': user_accounts, 'status_list': status_list})
