from django.shortcuts import redirect, render
from django.core.mail import send_mail
from blogs.models import Blog
from pages.models import Team, Email
from recipes.models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home_ru(request):
    recent_recipes_ru   = Recipe.objects.order_by('-created_date')[:4]
    recent_blogs_ru   = Blog.objects.order_by('-created_date')[:4]
    
    data = {
        'recent_recipes_ru':  recent_recipes_ru,
        'recent_blogs_ru':    recent_blogs_ru,
    }
    return render(request, 'pages/home_ru.html', data)

def home_az(request):
    recent_recipes_az   = Recipe.objects.order_by('-created_date')[:4]
    recent_blogs_az   = Blog.objects.order_by('-created_date')[:4]
    
    data = {
        'recent_recipes_az':  recent_recipes_az,
        'recent_blogs_az':    recent_blogs_az,
    }
    return render(request, 'pages/home_az.html', data)


def home(request):
    return redirect('home_ru')

def about_ru(request):
    members     = Team.objects.order_by('-created_date')
    
    data = {
        'members':  members,
    }
    
    return render(request, 'pages/about_ru.html', data)

def about_az(request):
    members     = Team.objects.order_by('-created_date')
    
    data = {
        'members':  members,
    }
    
    return render(request, 'pages/about_az.html', data)


def contact_ru(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        email_contact = Email(first_name=first_name, email=email, phone=phone, subject=subject, message=message)
        
        #Sending notification mails:
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        send_mail(
           'Новый запрос',
           'Вам, от ' + first_name + ' поступил новый запрос.',
           'asgarov.emin@gmail.com',
           [admin_email],
           fail_silently=False,
        )

        #Saving in DB:
        email_contact.save()
        
        messages.success(request, 'Ваш запрос был успешно отправлен')
        
    return render(request, 'pages/contact_ru.html')

def contact_az(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        email_contact = Email(first_name=first_name, email=email, phone=phone, subject=subject, message=message)
        
        #Sending notification mails:
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        send_mail(
           'Yeni sorğu',
           'Sizə, ' + first_name + '-dan sorğu daxil olmuşdur.',
           'asgarov.emin@gmail.com',
           [admin_email],
           fail_silently=False,
        )

        #Saving in DB:
        email_contact.save()
        
        messages.success(request, 'Sizin sorğunuz uğurla göndərilmişdir')
        
    return render(request, 'pages/contact_az.html')