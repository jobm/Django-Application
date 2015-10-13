from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .forms import FeedbackForm
from .models import Student
# Create your views here.
def index(request):
    form = StudentForm(request.POST or None)
    # print (request.POST)
    context = {
        "hello_message": "Register New Student",
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit = False)
        full_name = form.cleaned_data.get('full_name')
        if full_name == "Job":
            full_name = "Engineer"
        instance.full_name = full_name
        instance.save()
        form.save()
        context = {
        "hello_message":"Student SAVED",
        }

    return render(request,'index.html',context)
    #return HttpResponse("Success")

def feedback(request):
    form = FeedbackForm(request.POST or None)
    # if form.is_valid():
        # for key,value in form.cleaned_data.items():
        #     print(key, value)
    context = {
        'form' : form
    }
    return render(request,'feedback.html',context)

def students(request):
    students = Student.objects.all()
    context = { 'students' : students}
    return render(request,'students.html',context)
