from django.shortcuts import render
from django.views import generic
from . import models
from django.contrib.auth import mixins
from Cashier.forms import CashierPosForms, InPosForms
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.
class ListCashier(generic.ListView):
    template_name = 'cashier/cashier_list.html'
    context_object_name = 'cashierList'
    model = models.CashierPos

    """
    SELECT * 
    FROM CashierPos
    WHERE closed_date IS NULL
    ORDER_BY created_date DESC
    """
    def get_queryset(self):
        return models.CashierPos.objects.filter(closed_date__isnull = True).order_by('-created_date')
    

class ListHistory(generic.ListView):
    template_name = 'cashier/history_list.html'
    context_object_name = 'historyList'
    model = models.CashierPos

    """
    SELECT *
    FROM CashierPos
    WHERE closed_date <= timezone.now()
    ORDER_BY closed_date DESC
    """
    def get_queryset(self):
        return models.CashierPos.objects.filter(closed_date__lte = timezone.now()).order_by('-closed_date')
    

class DetailHistory(generic.DetailView):
    template_name = 'cashier/cashier_history.html'
    model = models.CashierPos


class CreateCashier(generic.CreateView):
    template_name = 'cashier/cashier_create.html'
    model = models.CashierPos
    form_class = CashierPosForms


class DetailCashier(generic.DetailView):
    template_name = 'cashier/cashier_detail.html'
    model = models.CashierPos


class CreateInPos(generic.CreateView):
    template_name = 'cashier/in_create.html'
    model = models.InPos
    form_class = InPosForms

    def get_success_url(self):
        cashierId = self.kwargs['pk']
        return reverse_lazy('cashier:detailCashier', kwargs={'pk': cashierId})

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)
