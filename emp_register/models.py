# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class EmpRegister(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    designation = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    mob_no = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_register'

    def __str__(self):
        return (f'{self.id} {self.name}')
