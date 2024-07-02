from django.shortcuts import render

# Create your views here.
def my_view(request):
    myName="Hemanth"
    favPlayer="Gayle"
    favAnimal="Tiger"
    favSubject="Python"
    d={'name':myName,"player":favPlayer,'animal':favAnimal,'subject':favSubject}
    return render(request,'myApp/1.html',d)