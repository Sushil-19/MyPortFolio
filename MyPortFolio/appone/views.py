from django.shortcuts import render
from django.http import HttpResponse
from .models import Services, Pricing, Blogs, MyInfo, Education, Experiance, Skills, Language, Project, Expertise
from django.http import FileResponse
from .sendMessage import send
from django.contrib import messages
from django.http import HttpResponseRedirect

def index(request):

    servlist = Services.objects.all()
    prices = Pricing.objects.all()
    blogs = Blogs.objects.all()
    myinfo = MyInfo.objects.all()
    educations = Education.objects.all()
    experiances = Experiance.objects.all()
    skills = Skills.objects.all()
    languages = Language.objects.all()
    projects = Project.objects.all()
    expertises = Expertise.objects.all()

    return render(request,'index.html', {'servlist' : servlist, 'prices':prices, 'blogs':blogs, 'myinfo':myinfo, 'expertises': expertises,
    'educations':educations, 'experiances':experiances,'skills':skills, 'languages':languages, 'projects':projects})

def comp(request):
    return render(request,'comp.html')

def sentMessages(request):
    flag = True
    name = request.GET["senderName"]
    email = request.GET["senderMail"]
    message = request.GET["senderMessage"]
    send(name,email,message)

    messages.info(request, 'Your message has been sent successfully!')
    return HttpResponseRedirect("/")

