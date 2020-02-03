from django.shortcuts import render,redirect

# Create your views here.

def login_page(request):
    if request.method == 'POST':
        return redirect('Pharma:home')
    return render(request, 'login.html')

def home_page(request):
    return render(request, 'home.html')

def list_medicine(request):
    return render(request, 'medicine.html')

def list_transactions(request):
    return render(request, 'transactions.html')
