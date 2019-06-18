from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Queu.models import customers, tellers
from django.core.serializers import serialize
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as password_handler
import datetime
from django.core.paginator import Paginator

@api_view(['POST'])
def create_customer(request):
    """
    Create Customer
    -----
        {
           
            fname:tima,
            lname:ali,
            email:tima@yahoo.com,
            msisdn:254682312,
            password:wooff,
            role: super or customer
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            customer = customers(
                fname=request.data['fname'],
                lname=request.data['lname'], 
                email=request.data['email'],  
                role=request.data['role'], 
                password=make_password(request.data['password']), 
                status='1', 
                msisdn=request.data['msisdn'],
                created_at = datetime.datetime.today(),
                updated_at= datetime.datetime.today()
            )
            customer.save()
            success={
                'message':'success',
                'status_code':200
            }
            return Response(success)
            
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)        



#update existing customer    
@api_view(['POST'])
def update_customer(request):    
    """
    Update customer details
    -----
        {
            id:1,
            fname:tima,
            lname:ali,
            email:tima@gmail.com,
            msisdn:254682312,
            password:miaww,
            role: super or user
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            customer = customers.objects.get(id=request.data['id'])
            customer.fname = request.data['fname']
            customer.lname=request.data['lname']
            customer.email=request.data['email']
            customer.msisdn=request.data['msisdn']
            customer.role=request.data['role']
            customer.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)  


#update existing customer  password   
@api_view(['POST'])
def update_customer_password(request):   
    """ 
    Update customer Password
    -----
        {
            id:1,
            password:123456
        } 
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            customer = customers.objects.get(id=request.data['id'])
            customer.password = make_password(request.data['password'])
            customer.save()
            success={
                'message':'success',
                'status_code':200,
            }
            return Response(success)

    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)            



#get all existing customers
@api_view(['POST'])  
def get_all_customers(request):  
    """
    See all customers 
    -----
        {
            page:1
            items: 5
        }
    """
    try: 
        customerss = customers.objects.all()
        page = request.GET.get('page', request.data['page'])
        paginator = Paginator(customerss, request.data['items'])
        details=[]
        for customer in paginator.page(page):
            values={
                'id':customer.id,
                'fname': customer.fname,
                'lname': customer.lname,
                'email': customer.email,
                'password': customer.password,
                'status': customer.status,
                'msisdn': customer.msisdn,
                'role':customer.role,
                'created_at': customer.created_at,
                'updated_at': customer.updated_at
            }

            details.append(values)

        data={
            'data':details,
            'message':'success',
            'status_code':200
            }
        return Response(data)
    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error) 



#get one particelar customers details
@api_view(['POST'])  
def get_particular_customer_details(request):

    """
    Get particular customer details
    -----
        {
            customer_id:1,
        }
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':

            customer_id = request.data['customer_id']
            customer = customers.objects.get(id=customer_id)
            details={
                'id':customer.id,
                'fname': customer.fname,
                'lname': customer.lname,
                'email': customer.email,
                'password': customer.password,
                'status': customer.status,
                'role':customer.role,
                'msisdn': customer.msisdn,
                'created_at': customer.created_at,
                'updated_at': customer.updated_at
            }

            data={'data':details,'message':'success','status_code':200}

            return Response(data)
    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error) 


@api_view(['POST'])
def delete_customer(request):
    """
    remove customer
    -----
        {
            id:1,
        }
    
    """
    try:
        if request.method == 'GET':
            success={'message':'method not allowed','status_code':401}
            return Response(success)

        elif request.method == 'POST':
            _id=request.data['id']
            delete=customers.objects.filter(id=_id).delete()
            data={
                "message":"customer deleted",
                "status_code":200
            }
            return Response(data)
    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
            'data':{}
        }
        return Response(error)  


# Login for a particular person
@api_view(['POST'])
def get_person_email_login(request):
    """
    Login for a particular person
    -----
        {
            email:roshie@gmail.com,
            password:roshie,
        }
    """

    try:
        user_id = request.data['email']
        user_input_pass = request.data['password']
        customer = customers.objects.get(email=user_id)
        if password_handler.verify(user_input_pass, customer.password):
            success = {
                'data': {
                    'id':customer.id,
                    'fname': customer.fname,
                    'lname': customer.lname,
                    'email': customer.email,
                    'password': customer.password,
                    'status': customer.status,
                    'role':customer.role,
                    'msisdn': customer.msisdn,
                    'created_at': customer.created_at,
                    'updated_at': customer.updated_at
                },
                'status_code': 200,
            }

            print(success)
            return Response(success)

        else:
            success = {
                'message': 'Error',
                'status_code': 500
            }

            return Response(success)

    except:
        user_id = request.data['email']
        user_input_pass = request.data['password']
        teller = tellers.objects.get(email=user_id)

        if password_handler.verify(user_input_pass, teller.password):
            success = {
                'data': {
                    'id':teller.id,
                    'fname': teller.fname,
                    'lname': teller.lname,
                    'email': teller.email,
                    'password': teller.password,
                    'status': teller.status,
                    'role':'TELLER',
                    'counter_id': teller.counter_id,
                    'created_at': teller.created_at,
                    'updated_at': teller.updated_at
                },
                'status_code': 200,
            }

            return Response(success)

        else:
            success = {
                'message': 'Error',
                'status_code': 500
            }
            return Response(success)




