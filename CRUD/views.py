from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductForm

# Create your views here.
# def homeView(request):
#     return render(request,'home/home.html')



def create_product(request):
    
  
    form =ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('Product-view')



    return render(request,'CRUD/create_product.html',{'form':form})



# viewing all the Products
def productView(request):
    # get all the product from the Product class
    product=Product.objects.all()

    context={'product':product}
    return render(request,'home/home.html',context)


def productUpdate(request,pk):
    product=Product.objects.get(id=pk)
    
    form = ProductForm(request.POST or None,instance=product)
    if form.is_valid():
        form.save()
        return redirect('Product-view')

    context={'form':form}
    return render(request,'CRUD/update_product.html',context)

def productDelete(request,pk):
    obj=Product.objects.get(id=pk)
    
    
    if request.method == 'POST':
        obj.delete()
        return redirect('Product-view')
    

   
    return render(request,'CRUD/delete_product.html')