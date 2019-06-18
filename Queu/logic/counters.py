from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import counters, service, tellers, logs
from django.core.serializers import serialize
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as password_handler
import datetime
from django.core.paginator import Paginator

@api_view(['POST'])
def create_counter(request):
    """
    Create Counter
    -----
        {
            number:leon,
            service_id: 1
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            counter = counters(
                number=request.data['number'],
                service_id=request.data['service_id'],
                created_at = datetime.datetime.today(),
                updated_at= datetime.datetime.today()
            )
            counter.save()
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



#update existing services    
@api_view(['POST'])
def update_counter(request):    
    """
    Update counter details
    -----
        {
            id:1,
            number:leon,
            service_id: 1
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            counter = counters.objects.get(id=request.data['id'])
            counter.number = request.data['number']
            counter.service_id = request.data['service_id']
            services.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)  

#get all existing counters
@api_view(['POST'])  
def get_all_counters(request):  
    """
    See all counters
    -----
        {
            page:1
            items: 5
        }
    """
    counter = counters.objects.all()
    page = request.GET.get('page', request.data['page'])
    paginator = Paginator(counter, request.data['items'])
    details=[]
    dat=[]
    for count in paginator.page(page):
        values={
            'id':count.id,
            'number': count.number,
            'service_id': count.service_id,
            'created_at': count.created_at,
            'updated_at': count.updated_at
        }

        details.append(values)

    for cats in details:
        services = service.objects.get(id=cats['service_id'])
        va={
            'id':cats['id'],
            'number': cats['number'],
            'service_name': services.name,
            'created_at': cats['created_at'],
            'updated_at': cats['updated_at']
        }

        dat.append(va)
    data={
        'data':dat,
        'message':'success',
        'status_code':200
        }
    return Response(data)


#get one particelar counters details
@api_view(['POST'])  
def get_particular_counters_details(request):

    """
    Get particular counters details
    -----
        {
            counter_id:1,
        }
    """
    if request.method == 'GET':
        success={'message':'method not allowed','status_code':401}
        return Response(success)

    elif request.method == 'POST':

        counter_id = request.data['counter_id']
        counter = counters.objects.get(id=counter_id)
        dat=[]
        details={
            'id':counter.id,
            'number': counter.number,
            'service_id': counter.service_id,
            'created_at': counter.created_at,
            'updated_at': counter.updated_at
        }

        for cats in details:
            services = service.objects.get(id=cats['service_id'])
            va={
                'id':cats['id'],
                'details': 'counter '+cats['number']+ services.name,
                'created_at': cats['created_at'],
                'updated_at': cats['updated_at']
            }

            dat.append(va)

        data={'data':dat,'message':'success','status_code':200}

        return Response(data)


#get one counters for a service details
@api_view(['POST'])  
def get_particular_counters_for_service_details(request):

    """
    Get service counters details
    -----
        {
            service_id:1,
        }
    """
    if request.method == 'GET':
        success={'message':'method not allowed','status_code':401}
        return Response(success)

    elif request.method == 'POST':

        service_id = request.data['service_id']
        counter = counters.objects.filter(service_id=service_id)
        details = []
        dat=[]
        for count in counter:
            values={
                'id':count.id,
                'number': count.number,
                'service_id': count.service_id,
                'created_at': count.created_at,
                'updated_at': count.updated_at
            }
            details.append(values)

        for cats in details:
            teller = tellers.objects.get(counter_id=cats['id'])
            services = service.objects.get(id=cats['service_id'])
            try:
                current = logs.objects.filter(teller_id = teller.id).latest('created_at')
                va={
                    'id':cats['id'],
                    'number': cats['number'],
                    'service_name': services.name,
                    'teller_name': teller.fname + teller.lname,
                    'ticketBeingServed': current.ticket_no,
                    'teller_id': teller.id,
                    'created_at': cats['created_at'],
                    'updated_at': cats['updated_at']
                }

                dat.append(va)
            except:
                va={
                    'id':cats['id'],
                    'number': cats['number'],
                    'service_name': services.name,
                    'teller_name': teller.fname + teller.lname,
                    'ticketBeingServed': 0,
                    'teller_id': teller.id,
                    'created_at': cats['created_at'],
                    'updated_at': cats['updated_at']
                }
                
                dat.append(va)
        data={'data':dat,'message':'success','status_code':200}

        return Response(data)


@api_view(['POST'])
def delete_counter(request):
    """
    remove counter
    -----
        {
            counter_id:1,
        }
    
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            _id=request.data['counter_id']
            delete=counters.objects.filter(id=_id).delete()
            data={
                "message":"Counter deleted",
                "status_code":200
            }
            return Response(data)

    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error) 




