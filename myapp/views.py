from django.http import HttpResponse
import datetime  
from django.shortcuts import render

def home(request):

    if request.method == 'POST':
      check = request.POST['check']
      print(check)

    date = datetime.datetime.now()
    isActive = True
    name = "Sumitra Maharjan"
    list_of_programs = [
        'WAP to check even or odd',
        'WAP to check prime number', 
        'WAP to print all prime numbers from 1 to 100'
    ]
    student = {
        'student_name': "Sumeetra Maharjan",
        'student_college': "NCCS",
        'student_city': "Kathmandu"
    }
    print('function is called from view')
    # return HttpResponse('<h1>hello this is index page  </h1>'+str(date))
    data = {
        'date':date,
        'isActive':isActive, 
        'name':name,
        'list_of_programs':list_of_programs,
        'student_data':student
    }
    return render(request, "home.html", data)

def about(request):
   # return HttpResponse('<h1> this is about pages</h1>')
   return render(request, "about.html", {})

def services(request):
    # return HttpResponse('<h1>This is services page</h1>')
    return render(request, "services.html", {})