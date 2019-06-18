from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import service
from django.core.serializers import serialize
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as password_handler
import datetime
from django.core.paginator import Paginator

@api_view(['POST'])
def create_service(request):
    """
    Create Service
    -----
        {
            name:leon,
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            services = service(
                name=request.data['name'],
                created_at = datetime.datetime.today(),
                updated_at= datetime.datetime.today()
            )
            services.save()
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
def update_service(request):    
    """
    Update service details
    -----
        {
            id:1,
            name:leon,
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            services = service.objects.get(id=request.data['id'])
            services.name = request.data['name']
            services.save()
            success={'message':'success','status_code':200}
            return Response(success)

    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)  

#get all existing service
@api_view(['POST'])  
def get_all_services(request):  
    """
    See all services
    -----
        {
            page:1
            items: 5
        }
    """
    servicess = service.objects.all()
    page = request.GET.get('page', request.data['page'])
    paginator = Paginator(servicess, request.data['items'])
    details=[]
    for services in paginator.page(page):
        values={
            'id':services.id,
            'name': services.name,
            'created_at': services.created_at,
            'updated_at': services.updated_at
        }

        details.append(values)

    data={
        'data':details,
        'message':'success',
        'status_code':200
        }
    return Response(data)


#get one particelar service details
@api_view(['POST'])  
def get_particular_service_details(request):

    """
    Get particular service details
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
        services = service.objects.get(id=service_id)
        details={
            'id':services.id,
            'name': services.name,
            'created_at': services.created_at,
            'updated_at': services.updated_at
        }

        data={'data':details,'message':'success','status_code':200}

        return Response(data)


@api_view(['POST'])
def delete_service(request):
    """
    remove services
    -----
        {
            service_id:1,
        }
    
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            _id=request.data['service_id']
            delete=service.objects.filter(id=_id).delete()
            data={
                "message":"services deleted",
                "status_code":200
            }
            return Response(data)

    except BaseException as e:
        
        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error) 




