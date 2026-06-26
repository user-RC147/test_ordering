from http.client import HTTPResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.views.generic.base import TemplateView
from .models import Client, Order, OrderItem,Product
from .forms import ClientForm,OrderForm, OrderItemFormSet, ProductForm,OrderFilterForm
from django.shortcuts import render,redirect


# Create your views here.
class IndexPage(TemplateView):
    template_name = "index.html"


class OrderListPage(ListView):
    model=Order
    template_name='order_temp/order_page.html'

    def get_queryset(self):
        client_id = self.request.GET.get('client')
        if client_id:
            return Order.objects.filter(client_id=client_id)
        return Order.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_filter_form'] = OrderFilterForm(self.request.GET or None)
        return context


class CreateClientPage(CreateView): 
    model=Client
    form_class=ClientForm
    template_name='user_temp/create_client.html'
    success_url = reverse_lazy('orderings:order_page')


class CreateProductPage(CreateView):
    model=Product
    form_class=ProductForm
    template_name='product_temp/create_product.html'
    success_url=reverse_lazy('orderings:create_order')


class CreateOrderPage(CreateView):
    template_name='order_temp/create_order.html'


    
    def get(self,request):
        order_form=OrderForm()
        formset=OrderItemFormSet()
        return render(request, self.template_name, 
            {
                'order_form':order_form,
                'formset':formset
            }
        )
    
    def post(self,request):
        order_form=OrderForm(request.POST)

        if order_form.is_valid():
            # commit=False — створює об'єкт Order але НЕ зберігає в БД
            # потрібно щоб отримати об'єкт для передачі в formset
            order=order_form.save(commit=False)
            order.save() # тепер зберігаємо → order отримує pk в БД
            

            formset=OrderItemFormSet(request.POST, instance=order)

            if formset.is_valid():
                formset.save()  # зберігає всі OrderItem
                return redirect('orderings:order_page')
            else:
                # formset невалідний — видаляємо order щоб не було сироти в БД
                order.delete()
        else:
            formset = OrderItemFormSet(request.POST)

        return render(request, self.template_name, {
            'order_form': order_form,
            'formset': formset
        })


class OrderDetailPage(DetailView):
    model=Order
    template_name='order_temp/order_detail.html'