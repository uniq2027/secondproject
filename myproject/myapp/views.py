from django.shortcuts import render

# # Create your views here.
# # Create your views here.

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, Django!")


# Create your views here.

def show(request):
    context = [ 'message', 'Welcome to Django using get_template!'] #request is passed to render() to allow template processing based on user requests.
    return render(request,'home.html',{"data":context})



#_____________________________________________________________________
from django.template import loader


def about(request):
    template = loader.get_template('about.html')  # Load the template
    context = [ 'message', 'Welcome to Django using get_template!']

         # Context to pass into the template
    
    return HttpResponse(template.render({"context":context}, request))  # Render and return the response


#_____________________________________________________________________


def color(request):
    return render(request,'color.html')




#_____________________________________________________________________

def bootstrab(request):
    return render(request,'bootstrab.html')




#_____________________________________________________________________

# from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def page1(request):
    return render(request, 'page1.html')

def page2(request):
    return render(request, 'page2.html')

def page3(request):
    return render(request, 'page3.html')



# _____________________________________________________________________


def submit_form(request):
    print("result:",request.method)
    if request.method == 'POST':
        # Get form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # (Optional) Do something with the form data like saving to the database, sending an email, etc.

        # Return a simple response or redirect to a thank-you page
        return HttpResponse(f'Thank you, {name}! We received your message.')
    
    # If GET request, display the form
    return render(request, 'form.html')
# #_____________________________________________________________________

# from .form import ContactForm


# def contact_view(request):
#     form=ContactForm()
#     return render(request, 'home.html',{"get_form":form})



from .form import ContactForm
from django.core.mail import send_mail

def contact_view(request):
    print(request)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            stored={
                "name":name,
                "email":email,
                "message":message,
                "information":'Form submitted and email sent successfully!'
            }
            
            # Send an email (assuming email is properly configured in settings.py)
            send_mail(
                f"Message from {name}",
                message,
                email,  # From email
                ['poovarasanuniq@gmail.com'],  # To email
            )
            return render(request,'home.html',{"data":stored})
            
    else:
        form = ContactForm()

    return render(request, 'home.html', {'get_form': form})


# #_____________________________________________________________________
# # views.py
from django.shortcuts import render, redirect
from .form import ProductForm

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new product
            return redirect("product_list") # Redirect after successful submission
    else:
        form = ProductForm()

    return render(request, 'color.html', {'form': form})

# # views.py 
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})



#  messages.success(request, "Registration successful! Please log in.")
#             return redirect("login")






from django.shortcuts import render, redirect
from .form import StudentEnrollmentForm
from .models import Student

def enroll_student(request):
    if request.method == "POST":
        form = StudentEnrollmentForm(request.POST)
        if form.is_valid():
            student = form.save()  # Save the student
            student.courses.set(form.cleaned_data['courses'])  # Assign selected courses
            return redirect('course_list')  # ✅ Redirect to student list page after saving
    else:
        form = StudentEnrollmentForm()

    return render(request, 'enroll_student.html', {'form': form})




def course_list(request):
    courses = Student.objects.all()  # ✅ Ensure 'Course' is imported
    return render(request, 'course_list.html', {'courses': courses})






# {% if messages %}
#     <ul class="messages">
#         {% for message in messages %}
#             <li class="{% if message.tags %}{{ message.tags }}{% endif %}">
#                 {{ message }}
#             </li>
#         {% endfor %}
#     </ul>
# {% endif %}





from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .form import ItemForm


#C-CREATE


def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})


#R-READ
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

#R-READ(SPECIFIC DATA)
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_details.html', {'item': item})


#U-UPDATE
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_form.html', {'form': form})



#D-DELETE
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item': item})




from .form import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        # Create a new user
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
         
       


        # Log the user in after registration
        login(request, user)
        messages.success(request, 'Registration successful!')
        return redirect('login')
    else:
        form = UserForm()


    return render(request, 'register.html',{'form':form})




from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('item_list')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('item_list')

