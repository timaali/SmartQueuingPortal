from django.db import models

class customers(models.Model):
    
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255, default=None)
    lname = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None, unique= True)
    password = models.CharField(max_length=255, default=None)
    msisdn = models.IntegerField(default=None, unique= True)
    role = models.CharField(max_length=255, default=None)
    status = models.IntegerField(default=0)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)

class service(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default=None)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)

class counters(models.Model):

    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=255, default=None)
    service_id = models.CharField(max_length=255, default=None)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)

class tellers(models.Model):

    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255, default=None)
    lname = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None, unique= True)
    password = models.CharField(max_length=255, default=None)
    counter_id = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)

class tickets(models.Model):

    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=0)
    customer_id = models.IntegerField(default=0)
    teller_id = models.IntegerField(default=0)
    ticket = models.IntegerField(default=None)
    status = models.IntegerField(default=None)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)

class logs(models.Model):

    id = models.AutoField(primary_key=True)
    ticket_no = models.IntegerField(default=None)
    teller_id = models.IntegerField(default=None)
    created_at = models.DateField(default=None)
    updated_at = models.DateField(default=None)