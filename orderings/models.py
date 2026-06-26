from django.db import models
from django.conf import settings

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name='Імʼя клієнта')
    email = models.EmailField(unique=True, verbose_name='Email')

    class Meta:
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Сутність товару.
    Зберігає назву та ціну за одиницю.
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Назва товару'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Ціна'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Сутність замовлення (один чек).
    Прив'язана до клієнта. Містить дату створення.
    Сума розраховується динамічно через property.
    """
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name='Клієнт'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f"Замовлення #{self.pk} — {self.client.name}"

    @property
    def total_price(self):
        """
        Динамічно рахує суму замовлення.
        Проходить по всіх OrderItem цього замовлення
        і сумує: ціна товару * кількість.
        Не зберігається в БД — обчислюється щоразу при виклику.
        """
        return sum(
            item.product.price * item.quantity
            for item in self.orderitem_set.all()
        )


class OrderItem(models.Model):
    """
    Один рядок чека (позиція замовлення).
    Прив'язана до конкретного замовлення (Order)
    та конкретного товару (Product).
    Зберігає кількість одиниць товару.
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Замовлення'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Кількість'
    )

    class Meta:
        verbose_name = 'Позиція замовлення'
        verbose_name_plural = 'Позиції замовлення'

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"