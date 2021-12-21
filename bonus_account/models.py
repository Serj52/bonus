from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


class Account(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=20, verbose_name='Фамилия')
    tel_number = models.PositiveIntegerField(verbose_name='Телефон')
    card_number = models.PositiveIntegerField(verbose_name='Номер карты')
    balance = models.DecimalField(verbose_name='Баланс', max_digits=1000, decimal_places=2)
    def __str__(self):
        return self.surname


class Trasaction(models.Model):
    pay = 'Оплата'
    pay_bon = 'Оплата бонусами'
    pay_get = 'Начисление бонусов'
    type_pay = ((pay, 'Оплата'), (pay_bon, 'Оплата бонусами'), (pay_get, 'Начисление бонусов'))
    type = models.CharField(choices=type_pay, max_length=len('Начисление бонусов'), verbose_name='Тип')
    sum = models.DecimalField(max_digits=19, decimal_places=2, verbose_name='Сумма')
    date = models.DateField(verbose_name='Дата')
    account = models.ForeignKey(Account, verbose_name='Аккаунт')

    def __str__(self):
        return self.type



















# Create your models here.
