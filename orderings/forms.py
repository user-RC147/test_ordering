from django import forms
from orderings.models import Client,Product,Order,OrderItem


class OrderFilterForm(forms.Form):
    client = forms.ModelChoiceField(
        queryset=Client.objects.all(),
        required=False,
        empty_label="Всі клієнти"
    )


class ClientForm(forms.ModelForm):

    #необов'язкови
    email = forms.EmailField(required=False)

    class Meta:
        model=Client
        fields=['name','email']


class ProductForm(forms.ModelForm):

    class Meta:
        model=Product
        fields=['name','price']

class OrderForm(forms.ModelForm):

    class Meta:
        model=Order
        fields=['client']


OrderItemFormSet=forms.inlineformset_factory(
    Order,
    OrderItem,
    fields=['product','quantity'],
    extra=0,
    can_delete=True,
    min_num=1,        # мінімум 1 форма
    validate_min=True # вмикає валідацію min_num
)