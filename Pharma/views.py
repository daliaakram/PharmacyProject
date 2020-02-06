from django.shortcuts import render,redirect
from Pharma.models import Medicine,Transactions
from Pharma.forms import MedicineForm, TransactionsForm
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory,inlineformset_factory
# Create your views here.


def login_page(request):
    if request.method == 'POST':
        return redirect('Pharma:home')
    return render(request, 'login.html')

# def create_med(request):
#     Formset = inlineformset_factory( Medicine,
#         extra = 5,
#         fields = ('scientific_name','trade_name','alternate1', 'alternate2' ,'qnt', 'item_price', 'start_date','end_date'),
#         )
#     if request.method == 'POST':
#         form = Formset(request.POST)
#         form.save()
#         return redirect('Pharma:medicine')
#     form = Formset(queryset = Medicine.objects.none())
#     return render(request, 'createmed.html', {'form':form})

def create_med(request):
    Formset = modelformset_factory(Medicine, fields = ('scientific_name','trade_name','alternate1', 'alternate2' ,'qnt', 'item_price', 'start_date','end_date'), extra=5)
    if request.method == 'POST':
        form = Formset(request.POST)
        form.save()
        return redirect('Pharma:medicine')
    form = Formset(queryset = Medicine.objects.none())
    return render(request, 'createmed.html', {'form':form})

def create_trans(request):
    Formset = modelformset_factory(Transactions, fields = ('med_name','sell_qnt','sell_price', 'sell_date'), extra=5)
    if request.method == 'POST':
        form = Formset(request.POST)
        form.save()
        return redirect('Pharma:transactions')
    form = Formset(queryset = Transactions.objects.none())
    return render(request, 'createtrans.html', {'form':form})

def list_medicine(request):
    medicine_list = Medicine.objects.order_by('trade_name')
    return render(request, 'listmedicine.html', {'medicine_records':medicine_list})

def list_transactions(request):
    transactions_list = Transactions.objects.order_by('med_name')
    return render(request, 'listtransactions.html', {'transactions_records':transactions_list})

def get_loggedin_user(request):
    name = request.POST['uname']
    print(name)
    return render(request, 'master.html', {'your_name':name})

def update_medicine(request, id = None):
    form = MedicineForm()
    instance = get_object_or_404(Medicine, id = id)
    form = MedicineForm(instance=instance)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=instance)

        if form.is_valid():
            print("form is valid")
            instance.save()
            return redirect('Pharma:medicine')

    context = {
        'form' : form
    }

    return render(request, 'modelform.html', context)


def delete_medicine(request, id =None):
    instance = get_object_or_404(Medicine, id = id)
    if request.method == 'POST':
        instance.delete()
        # return redirect('Pharma:medicine')
    return render(request, 'listmedicine.html', {'insert_med':instance})


def update_transaction(request, id = None):
    form = TransactionsForm()
    instance = get_object_or_404(Transactions, id = id)
    form = TransactionsForm(instance=instance)

    if request.method == 'POST':
        form = TransactionsForm(request.POST, instance=instance)

        if form.is_valid():
            print("form is valid")
            instance.save()
            return redirect('Pharma:transactions')

    context = {
        'form' : form
    }

    return render(request, 'modelform.html', context)


def delete_transaction(request, id =None):
    instance = get_object_or_404(Transactions, id = id)
    if request.method == 'POST':
        instance.delete()
        # return redirect('Pharma:transactions')
    return render(request, 'listtransactions.html', {'insert_med':instance})
