from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    """
    Receive the request from the client
    """
    my_dict = {'insert_me' : "Hello I am from views.py"}
    return render(request,'basicapp/index.html', context=my_dict)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            # Do Something
            print("VALIDATION SUCESS!")
            print("Name"+form.cleaned_data["name"])
            print("Email"+form.cleaned_data["email"])
            print("Text"+form.cleaned_data["text"])  
    return render(request,'basicapp/form_page.html',{'form':form})



