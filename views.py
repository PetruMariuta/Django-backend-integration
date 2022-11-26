from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse
from django.shortcuts import render



a=" insert name "
def index(request):
  mymembers = Members.objects.all().values()
  output = ""
  
  for x in mymembers:
    output += x["firstname"]
  output+=" insert name "
  output+=a
  for x in range(0,5):
    output += "x"
  
  return HttpResponse(output,a)
  
def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
    
  }
  
  
  return HttpResponse(template.render(context, request))
# Create your views here.

def add(request):
    template = loader.get_template("add.html")
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST["first"]
    y = request.POST["last"]
    member = Members(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse("index"))

def delete(request,id):
  member = Members.objects.get(id=id)
  member.delete()
  '''entries= Members.objects.all()   deletes all
     entries.delete()'''
  return HttpResponseRedirect(reverse("index"))

def update(request, id):
 mymember = Members.objects.get(id=id)
 template = loader.get_template("update.html")
 context = {
  'mymember': mymember
  }
 return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))
