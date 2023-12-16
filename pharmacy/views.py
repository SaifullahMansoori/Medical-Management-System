from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import MedicineModel, SalesModel, CustomerModel, LonsModel


def homeView(request):
    return render(request, 'home.html', {})


def loginView(request):
    if request.method == 'POST':
        username = request.POST['txt_name']
        password = request.POST['txt_password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            return render(request, 'login.html', {'error_message': 'Incorrect username or password.'})
    return render(request, 'login.html')


def medicineView(request):
    if request.method == 'POST':
        if 'btnAdd' in request.POST:
            medicineModel = MedicineModel()
            medicineModel.name = request.POST['txt_name']
            medicineModel.price = request.POST['txt_price']
            medicineModel.quantity = request.POST['txt_quantity']
            medicineModel.expire_date = request.POST['txt_expire_date']
            medicineModel.catagory = request.POST['txt_catagory']
            if all([medicineModel.name, medicineModel.price, medicineModel.quantity, medicineModel.catagory,
                    medicineModel.expire_date]):
                medicineModel.save()
                return redirect('/medicine/')
            else:
                return render(request, 'medicine.html', {'error_message': 'Same input is invalid try again'})
    select = MedicineModel.objects.all()
    return render(request, 'medicine.html', {'form': select})


def medicineUpdateView(request, pk):
    updateMedicine = MedicineModel.objects.get(id=pk)
    context = {'up': updateMedicine}
    if request.method == 'POST':
        if 'btnUpdate' in request.POST:
            updateMedicine.name = request.POST['txt_name']
            updateMedicine.price = request.POST['txt_price']
            updateMedicine.expire_date = request.POST['txt_expire_date']
            updateMedicine.catagory = request.POST['txt_catagory']
            updateMedicine.quantity = request.POST['txt_quantity']
            if all([updateMedicine.name, updateMedicine.price, updateMedicine.expire_date, updateMedicine.catagory,
                    updateMedicine.quantity]):
                updateMedicine.save()
                return redirect('/medicine/')
            else:
                return render(request, 'updateMedicine.html', {'error': 'same input is invalid'})
    return render(request, 'updateMedicine.html', context)


def medicineDeleteView(request, pk):
    deleteMedicine = MedicineModel.objects.get(id=pk)
    context = {'g': deleteMedicine}
    if request.method == 'POST':
        if 'btnDelete' in request.POST:
            deleteMedicine.delete()
            return redirect('/medicine/')
    return render(request, 'deleteMedicine.html', context)


def selesView(request):
    if request.method == 'POST':
        if 'btnAdd' in request.POST:
            sale = SalesModel()
            sale.customer = request.POST['txt_customer']
            sale.medicine = request.POST['txt_medicine']
            sale.amount = request.POST['txt_amount']
            sale.price = request.POST['txt_price']
            sale.date = request.POST['txt_date']
            if all([sale.customer, sale.medicine, sale.amount, sale.price, sale.date]):
                sale.save()
                return redirect('/sales/')
            else:
                return render(request, 'sales.html', {'error', 'same input is invalid'})
    sale = SalesModel.objects.all()
    context = {'form': sale}
    return render(request, 'sales.html', context)


def saleUpdateView(request, pk):
    order = SalesModel.objects.get(id=pk)
    if request.method == 'POST':
        if 'btnUpdate' in request.POST:
            order.customer = request.POST['txt_customer']
            order.medicine = request.POST['txt_medicine']
            order.amount = request.POST['txt_amount']
            order.price = request.POST['txt_price']
            order.date = request.POST['txt_date']
            if all([order.customer, order.medicine, order.amount, order.price, order.date]):
                order.save()
                return redirect('/sales/')
            else:
                return render(request, 'updateSales.html', {'error': 'same input is invalid'})
    context = {'up': order}
    return render(request, 'updateSales.html', context)


def saleDeleteView(request, pk):
    deleteOrder = SalesModel.objects.get(id=pk)
    if request.method == 'POST':
        if 'btnDelete' in request.POST:
            deleteOrder.delete()
            return redirect('/sales/')
    context = {'g': deleteOrder}
    return render(request, 'deleteSales.html', context)


def customerView(request):
    if request.method == 'POST':
        if 'btnAdd' in request.POST:
            new_customer = CustomerModel()
            new_customer.fullName = request.POST['txt_fullName']
            new_customer.address = request.POST['txt_address']
            new_customer.phoneNumber = request.POST['txt_phone']
            new_customer.registerDate = request.POST['txt_date']
            if all([new_customer.fullName, new_customer.address, new_customer.phoneNumber, new_customer.registerDate]):
                new_customer.save()
                return redirect('/customer/')
            else:
                return render(request, 'customer.html', {'error': 'same input in invalid'})
    customer = CustomerModel.objects.all()
    context = {'form': customer}
    return render(request, 'customer.html', context)


def customerUpdateView(request, pk):
    update = CustomerModel.objects.get(id=pk)
    if request.method == 'POST':
        if 'btnUpdate' in request.POST:
            update.fullName = request.POST['txt_name']
            update.address = request.POST['txt_address']
            update.phoneNumber = request.POST['txt_phone']
            update.registerDate = request.POST['txt_date']
            if all([update.fullName, update.address, update.phoneNumber, update.registerDate]):
                update.save()
                return redirect('/customer/')
            else:
                return render(request, 'updateCustomer.html', {'error': 'same input is invalid'})
    return render(request, 'updateCustomer.html', {'up': update})


def customerDeleteView(request, pk):
    removeCustomer = CustomerModel.objects.get(id=pk)
    if request.method == "POST":
        removeCustomer.delete()
        return redirect('/customer/')
    context = {'g': removeCustomer}
    return render(request, 'deleteCustomer.html', context)


def lonsView(request):
    if request.method == "POST":
        if 'btnAdd' in request.POST:
            newLoans = LonsModel()
            newLoans.customerName = request.POST['txt_name']
            newLoans.amount = request.POST['txt_amount']
            newLoans.date = request.POST['txt_date']
            if all([newLoans.customerName, newLoans.amount, newLoans.date]):
                newLoans.save()
                return redirect('/lons/')
            else:
                return render(request, 'lons.html', {'error': 'Same input is invalid'})

    loans = LonsModel.objects.all()
    context = {'form': loans}
    return render(request, 'lons.html', context)


def lonsDeleteView(request, pk):
    deletLoans = LonsModel.objects.get(id=pk)
    context = {'g': deletLoans}
    if request.method == "POST":
        deletLoans.delete()
        return redirect('/lons/')
    return render(request, 'deleteLons.html', context)


def lonsUpdateView(request, pk):
    update = LonsModel.objects.get(id=pk)
    if request.method == 'POST':
        if 'btnUpdate' in request.POST:
            update.customerName = request.POST['txt_name']
            update.amount = request.POST['txt_amount']
            update.date = request.POST['txt_date']
            if all([update.customerName, update.amount, update.date]):
                update.save()
                return redirect('/lons/')
            else:
                return render(request, 'updateSales.html', {'error': 'same input is invalid'})
    return render(request, 'updateLons.html', {'up': update})
