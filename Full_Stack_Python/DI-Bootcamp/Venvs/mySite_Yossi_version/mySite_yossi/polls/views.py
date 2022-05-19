from audioop import reverse
from re import template
from turtle import update
from unicodedata import category
from django.shortcuts import render # this line is added automatically
from django.http import HttpResponse # pass view information into the browser
from .models import Person, Post, ImageProfile, Category
from .forms import ContactForm, PersonForm, PostForm
from django.views import generic
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView

def contact(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'profile/contact.html', context)


# takes a request, returns a response
# person = Person.objects.filter(first_name="Shon", 
#                                last_name = "Ben Shimon").first() 
                    # get the first object because Person.objects.filter returns a QuerSet (ie. a list)


def index(request):
    #POST method - request method = POST

    if request.method == 'POST':
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            context = {'page_title' : 'Homepage', 'user': person, 'name': name, 'email': email, 'comment': comment, 'submit' : True}
            return render(request, 'posts/homepage.html', context)
            
            
    #GET Method - request method = GET
    context = {
        'page_title' : "Homepage",
        'user' : person,
        'form' : ContactForm(),
        'submit' : False
    }
    return render(request, 'posts/homepage.html', context)


def posts(request):
    context = {
        'user' : person,
        'page_title' : "Posts",
        'posts' : Post.objects.filter(
                    author__first_name=person.first_name,
                    author__last_name=person.last_name)
    }
    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = PostForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            post_to_add = form.save(commit=False)
            form.save()
            # will return an object that hasn’t yet been saved to the database
            for attr, value in post_to_add.__dict__.items():
                print(f'{attr} : {value}')
                
            context['submit'] = True

            return render(request, 'posts/posts.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'posts/posts.html', context)

    else:
        # GET, generate blank form
        context['form'] = PostForm()
    return render(request, 'posts/posts.html', context)

def email(request):
    context = {'page_title' : 'Email',
    'user' : person,
    'email_address': person.email}

    return render(request, 'profile/email.html', context)

def create_user(request):
    context = {'page_title' : 'New user',
    'form': PersonForm()}

    return render(request, 'profile/new_user.html', context)

def signup(request):
    context = {
        'page_title' : "SignUp",
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = PersonForm(request.POST) # the Person Form
        # check if it's valid:
        if form.is_valid():
            new_user = form.save()

            form_first_name = form.cleaned_data['first_name']
            form_last_name = form.cleaned_data['last_name']
            form_birth_date = form.cleaned_data['birth_date']
            form_has_pet = form.cleaned_data['has_pet']
            form_number_pet = form.cleaned_data['number_pet']
            context['formInfo'] = {
                    'first_name' : form_first_name,
                    'last_name': form_last_name,
                    'birth_date': form_birth_date,
                    'has_pet': form_has_pet,
                    'number_pet': form_number_pet 
                }
            print(context['formInfo'])
            return render(request, 'profile/signup.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'profile/signup.html', context)

    else:
        # GET, generate blank form
        context['form'] = PersonForm()
    return render(request, 'profile/signup.html', context)

def category(request):
    context = {
        'user' : person,
        'page_title' : "Posts",
        'posts' : Post.objects.filter(
                    author__first_name=person.first_name,
                    author__last_name=person.last_name)
    }

    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form = PostForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            post_to_add = form.save(commit=False) 
            # will return an object that hasn’t yet been saved to the database
            for attr, value in post_to_add.__dict__.items():
                print(f'{attr} : {value}')

            return render(request, 'posts/posts.html', context)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'posts/posts.html', context)

    else:
        # GET, generate blank form
        context['form'] = PostForm()
    return render(request, 'posts/posts.html', context)

# class PostIndex(generic.ListView):
#     template_name = 'posts/posts.html'
#     model = Post


# class PostIndex(generic.ListView):
#     template_name = 'posts/posts.html'
#     context_object_name = 'posts' 
#     # change the name of the object_list variable to posts -> use the variables
#     # posts in the template
#     model = Post

class PostIndex(generic.ListView):
    template_name = 'posts/posts.html'
    context_object_name = 'posts' 
    model = Post

    def get_context_data(self, **kwargs):
         # **kwargs contains keyword context initialization values (if any)
         # Call base implementation to get a context
        context = super(PostIndex, self).get_context_data(**kwargs)
         # Add context data to pass to template
        context['page_title'] = "Post"
        context['user'] = person
        return context

class Person_id(DetailView):

    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class NewPerson(generic.CreateView):
    template_name = 'profile/new_user.html'
    model = Person
    fields = '__all__'

class NewCategory(generic.CreateView):
    template_name = 'posts/new_category.html'
    model = Category
    fields = '__all__'

    def get_success_url(self):
        return reverse('index')

class CategoryUpdateView(generic.UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'posts/category_update_fr'




