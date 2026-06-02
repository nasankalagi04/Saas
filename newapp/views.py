
from .models import Subscription
from django.shortcuts import render, redirect,get_object_or_404
from .forms import SubscriptionForm
from django.contrib.auth.decorators import login_required

@login_required
def subscription_list(request):
    subs = Subscription.objects.filter(user=request.user)
    return render(request, 'subscriptions/list.html', {'subs': subs})

@login_required
def add_subscription(request):
    form = SubscriptionForm(request.POST or None)
    if form.is_valid():
        sub = form.save(commit=False)
        sub.user = request.user   # 🔥 IMPORTANT LINE
        sub.save()
        return redirect('list')
    
    return render(request, 'subscriptions/add.html', {'form': form})

@login_required
def edit_subscription(request, id):
    sub = get_object_or_404(Subscription, id=id, user=request.user)

    form = SubscriptionForm(request.POST or None, instance=sub)

    if form.is_valid():
        updated_sub = form.save(commit=False)
        updated_sub.user = request.user   # keep user intact
        updated_sub.save()
        return redirect('edit',id=sub.id)

    return render(request, 'subscriptions/edit.html', {'form': form})