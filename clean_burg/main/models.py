from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField


class Service(models.Model):
    name = models.CharField(_("Название"), max_length=100)
    price = MoneyField(verbose_name=_("Стоимость"), max_digits=14, decimal_places=2, default_currency="RUB")

    created_at = models.DateTimeField(_("Время создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Время обновления"), auto_now=True)

    class Meta:
        ordering = ("name",)
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")

    def __str__(self):
        return self.name


class Order(models.Model):
    NEW = 10
    PROCESSING = 20
    DONE = 30
    CANCELED = 40

    STATUS_OPTIONS = (
        (NEW, _("Новый")),
        (PROCESSING, _("В обработке")),
        (DONE, _("Выполнен")),
        (CANCELED, _("Отменён")),
    )
    status = models.IntegerField(_("Статус"), choices=STATUS_OPTIONS, default=NEW)

    client = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="orders", null=True, blank=True, )
    client_name = models.CharField(_("Имя клиента"), max_length=100)
    client_phone = models.CharField(_("Телефон клиента"), max_length=100)
    client_comment = models.TextField(_("Комментарий к заказу"), blank=True, null=True)

    created_at = models.DateTimeField(_("Время создания"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Время обновления"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")

    def __str__(self):
        return f"Заказ #{self.pk}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="order_items", verbose_name=_("Услуга"))
    price = MoneyField(verbose_name=_("Стоимость"), max_digits=14, decimal_places=2, default_currency="RUB", default=0)

    class Meta:
        ordering = ("pk",)
        verbose_name = _("Элемент заказа")
        verbose_name_plural = _("Элементы заказа")

    def __str__(self):
        return f"Элемент заказа #{self.order.pk}"
