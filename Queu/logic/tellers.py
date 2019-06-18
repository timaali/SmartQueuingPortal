from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import tellers, service, counters
from django.core.serializers import serialize
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as password_handler
import datetime
from django.core.paginator import Paginator

@api_view(['POST'])
def create_teller(request):
    """
    Create teller
    -----
        {
           
            fname:leon,
            lname:lishenga,
            email:leon@yahoo.com,
            password:roshie,
            counter_id: 1
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            teller = tellers(
                fname=request.data['fname'],
                lname=request.data['lname'], 
                email=request.data['email'],  
                password=make_password(request.data['password']), 
                counter_id=request.data['counter_id'], 
                status='1', 
                created_at = datetime.datetime.today(),
                updated_at= datetime.datetime.today()
            )
            teller.save()
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



#update existing teller    
@api_view(['POST'])
def update_teller(request):    
    """
    Update teller details
    -----
        {
            id:1,
            fname:leon,
            lname:lishenga,
            email:leon@yahoo.com,
            password:roshie,
            counter_id: 1
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            teller = tellers.objects.get(id=request.data['id'])
            teller.fname = request.data['fname']
            teller.lname=request.data['lname']
            teller.email=request.data['email']
            teller.counter_id=request.data['counter_id']
            teller.password = request.data['password']
            teller.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)  


#update existing teller  password   
@api_view(['POST'])
def update_teller_password(request):   
    """ 
    Update teller Password
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
            teller = tellers.objects.get(id=request.data['id'])
            teller.password = make_password(request.data['password'])
            teller.save()
            success={
                'message':'success',
                'status_code':200,
            }
            return Response(success)

    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)            



#get all existing tellers
@api_view(['POST'])  
def get_all_tellers(request):  
    """
    See all tellers 
    -----
        {
            page:1
            items: 5
        }
    """
    tellerss = tellers.objects.all()
    page = request.GET.get('page', request.data['page'])
    paginator = Paginator(tellerss, request.data['items'])
    details=[]
    data=[]
    for teller in paginator.page(page):
        values={
            'id':teller.id,
            'fname': teller.fname,
            'lname': teller.lname,
            'email': teller.email,
            'password': teller.password,
            'status': teller.status,
            'counter_id': teller.counter_id,
            'created_at': teller.created_at,
            'updated_at': teller.updated_at
        }

        details.append(values)

    for cats in details:
        counter = counters.objects.get(id=cats['counter_id'])
        services = service.objects.get(id=counter.service_id)
        val={
            'teller_id':cats['id'],
            'fname': cats['fname'],
            'lname': cats['lname'],
            'email': cats['email'],
            'counter_number': counter.number,
            'service_name': services.name,
            'created_at': cats['created_at'],
            'updated_at': cats['updated_at']
        }

        data.append(val)

    data={
        'data':data,
        'message':'success',
        'status_code':200
        }
    return Response(data)



#get one particelar tellers details
@api_view(['POST'])  
def get_particular_teller_details(request):

    """
    Get particular teller details
    -----
        {
            teller_id:1,
        }
    """
    if request.method == 'GET':
        success={'message':'method not allowed','status_code':401}
        return Response(success)

    elif request.method == 'POST':

        teller_id = request.data['teller_id']
        teller = tellers.objects.get(id=teller_id)
        details={
            'id':teller.id,
            'fname': teller.fname,
            'lname': teller.lname,
            'email': teller.email,
            'password': teller.password,
            'counter_id': teller.counter_id,
            'status': teller.status,
            'created_at': teller.created_at,
            'updated_at': teller.updated_at
        }

        data=[]

        for cats in details:
            counter = counters.objects.get(id=cats['counter_id'])
            services = service.objects.get(id=counter.service_id)
            val={
                'teller_id':cats['id'],
                'fname': cats['fname'],
                'lname': cats['lname'],
                'email': cats['email'],
                'counter_number': counter.number,
                'service_name': services.name,
                'created_at': cats['created_at'],
                'updated_at': cats['updated_at']
            }

            data.append(val)

        data={'data':data,'message':'success','status_code':200}

        return Response(data)


@api_view(['POST'])

def delete_teller(request):
    """
    remove teller
    -----
        {
            id:1,
        }
    
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            _id=request.data['id']
            delete=tellers.objects.filter(id=_id).delete()
            data={
                "message":"teller deleted",
                "status_code":200
            }
            return Response(data)

    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)   




