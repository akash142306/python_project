from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
# Create your views here.

def index(request):  # with the help of this function we are triying to create a web page by passing an html file 
    data=Student.objects.all()
    print(data)
    context={"data":data}  # context is like a dictionary in django 
    return render(request,"index.html",context)  # with the help of this we will check if our routing works properly


def insertData(request):    #request is a parameter representing the HTTP request that is sent to the server. 
    if request.method=="POST":   # Check if the request method is POST   
        # extracting parameters from POST methods  
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        print(name,email,age,gender)

        # Create a new Student object with the extracted data
        query=Student(name=name,email=email,age=age,gender=gender)
        query.save()        # Save the new Student object to the database

        messages.info(request,"Student Data Inserted Successfully")
        return redirect("/")        # Redirect to the homepage ("/") after successfully inserting data


    return render(request,"index.html")    # If the request method is not POST, render the "index.html" template



def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        gender=request.POST['gender']

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.age=age
        edit.save()
        messages.warning(request,"Student Data Updated Successfully")
        return redirect("/")

    d=Student.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id) 
    d.delete()
    messages.error(request,"Student Data deleted Successfully")
    return redirect("/")
    
    
def about(request):
    return render(request,"about.html")