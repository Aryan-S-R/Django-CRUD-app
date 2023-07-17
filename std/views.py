from django.shortcuts import render,redirect 
from.models import Students


def home(request):
    std=Students.objects.all()

    return render(request, 'home.html', {'std': std})

def navbar(request):
    return render(request, 'navbar.html')

def add_std(request):
    if request.method == "POST":
        print("added")
        std_roll=request.POST.get("std_roll")
        std_name=request.POST.get("std_name")
        std_email=request.POST.get("std_email")
        std_address=request.POST.get("std_address")
        std_phone=request.POST.get("std_phone")

        s=Students()
        s.roll=std_roll
        s.name=std_name
        s.email=std_email
        s.address=std_address
        s.phone=std_phone

        s.save()
        return redirect('add_std')
    
    return render(request, 'add_std.html')

def delete_std(request):
    print('Deleted')
    s_id = request.GET.get('s_id')
    Students.objects.filter(id = int(s_id)).delete()

    return redirect('home')


def edit_std(request):
    std_id = request.GET.get('s_id')
    std=Students.objects.get(id=int(std_id))
    return render(request, 'update_std.html',{'std':std})

def do_edit_std(request):
    std_roll=request.POST.get("std_roll")
    std_name=request.POST.get("std_name")
    std_email=request.POST.get("std_email")
    std_address=request.POST.get("std_address")
    std_phone=request.POST.get("std_phone")
    std_id = request.GET.get('s_id')
    std=Students.objects.get(id=int(std_id))

    std.roll = std_roll
    std.name = std_name
    std.email = std_email
    std.address = std_address
    std.phone = std_phone

    std.save()
    return redirect('home')
    