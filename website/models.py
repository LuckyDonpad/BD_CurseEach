from django.db import models


class Workers(models.Model):
    name = models.CharField(max_length=256, verbose_name="Имя")
    surname = models.CharField(max_length=256, verbose_name="Фамилия")
    patronymic = models.CharField(default="отчество", max_length=256, verbose_name="Отчество")


class Tasks(models.Model):
    name = models.CharField(max_length=256, verbose_name="Задача")
    status = models.IntegerField(verbose_name="Статус", default=0)
    begin_date = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    end_date = models.DateField(verbose_name="Дэдлайн")
    worker_id = models.ForeignKey(Workers, on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name="ID сотрудника")


class Users(models.Model):
    name = models.CharField(default="имя", max_length=256, verbose_name="Имя")
    surname = models.CharField(default="фамилия", max_length=256, verbose_name="Фамилия")
    patronymic = models.CharField(default="отчество", max_length=256, verbose_name="Отчество")


class Clients(models.Model):
    name = models.CharField(default="имя", max_length=256, verbose_name="Имя")
    surname = models.CharField(default="фамилия", max_length=256, verbose_name="Фамилия")
    patronymic = models.CharField(default="отчество", max_length=256, verbose_name="Отчество")
    phone = models.CharField(max_length=256, verbose_name="Телефон")
    register_date = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")


#TODO
"""
редактирование полей в бд
миграция постгрес
переделать бэкапы на постгресзависимые
разграничение доступа (админ редачи, юзер смотрит)
"""
