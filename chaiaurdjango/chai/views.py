from django.shortcuts import render
from .models import chaiVarity, Store
from django.shortcuts import get_object_or_404
from .forms import chaiVarityForm

# Create your views here.

def all_chai(request):
    chais = chaiVarity.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})
def chai_detail(request, chai_id):
    chai = get_object_or_404(chaiVarity, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def chai_stores(request):
    stores=None
    if(request.method=="POST"):
        form=chaiVarityForm(request.POST)
        if form.is_valid():
            chai_Varity=form.cleaned_data['chai_Varity']
            stores=Store.objects.filter(chai_vareties=chai_Varity)
    else:
        form=chaiVarityForm()
    return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})
