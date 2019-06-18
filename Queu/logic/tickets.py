from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from models import tickets, customers, tellers, service, logs, counters
from django.core.serializers import serialize
from django.contrib.auth.hashers import make_password
from passlib.hash import django_pbkdf2_sha256 as password_handler
from django.db.models import Count
import datetime
from django.core.paginator import Paginator

@api_view(['POST'])
def create_ticket(request):
    """
    Create ticket
    -----
        {
           
            customer_msisdn:0791172530,
            teller_id:1,
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            customer = customers.objects.get(msisdn = request.data['customer_msisdn'])
            all = tickets.objects.filter(teller_id = request.data['teller_id']).count()
            ticketing = tickets(
                customer_id=customer.id,
                teller_id= request.data['teller_id'],
                ticket= all + 1,  
                status=1, 
                created_at = datetime.datetime.today(),
                updated_at= datetime.datetime.today()
            )
            ticketing.save()
            ticket_no = tickets.objects.get(customer_id=customer.id)
            success={
                'message':'success',
                'ticket_no':ticket_no.ticket,
                'status_code':200
            }
            return Response(success)
            
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)        



#Cancel existing ticket    
@api_view(['POST'])
def cancel_ticket(request):    
    """
    Cancel ticket
    -----
        {
            ticket_no:1,
            teller_id: 1
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            no=request.data['ticket_no']
            delete=tickets.objects.filter(teller_id=request.data['teller_id']).get(ticket=no).delete()
            data={
                "message":"ticket deleted",
                "status_code":200
            }
            return Response(data)
            
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error)            



#get all existing tickets
@api_view(['POST'])  
def get_all_tickets(request):  
    """
    See all tickets 
    -----
        {
            page:1
            items: 5
        }
    """
    ticketss = tickets.objects.all()
    all = tickets.objects.all().Count()
    page = request.GET.get('page', request.data['page'])
    paginator = Paginator(ticketss, request.data['items'])
    details=[]
    data=[]
    datas=[]
    for ticket in paginator.page(page):
        values={
            'id':ticket.id,
            'customer_id': ticket.customer_id,
            'teller_id': ticket.teller_id,
            'ticket_no': ticket.ticket,
            'status': ticket.status,
            'created_at': ticket.created_at,
            'updated_at': ticket.updated_at
        }

        details.append(values)

    for cats in details:
        customer = customers.objects.get(id=cats['customer_id'])
        teller = tellers.objects.get(id=cats['teller_id'])
        val={
            'ticket_id':cats['id'],
            'customer_fname': customer.fname,
            'teller_fname': teller.fname,
            'customer_lname': customer.lname,
            'teller_lname': teller.lname,
            'counter_id': teller.counter_id,
            'ticket_no': cats['ticket_no'],
            'created_at': cats['created_at'],
            'updated_at': cats['updated_at']
        }

        data.append(val)

    for ca in data:
        counter = counters.objects.get(id=ca['counter_id'])
        service = services.objects.get(id=counter.service_id)
        vals={
            'ticket_id':ca['ticket_id'],
            'customer_fname': ca['customer_fname'],
            'teller_fname': ca['teller_fname'],
            'customer_lname': ca['customer_lname'],
            'teller_lname': ca['teller_lname'],
            'service_name': service.name,
            'ticket_no': ca['ticket_no'],
            'created_at': ca['created_at'],
            'updated_at': ca['updated_at']
        }

        datas.append(vals)

    data={
        'data':datas,
        'total': all,
        'message':'success',
        'status_code':200
        }
    return Response(data)



#get one particular tickets details
@api_view(['POST'])  
def get_particular_ticket_details(request):

    """
    Get particular ticket details
    -----
        {
            ticket_no:1,
        }
    """
    if request.method == 'GET':
        success={'message':'method not allowed','status_code':401}
        return Response(success)

    elif request.method == 'POST':

        ticket_no = request.data['ticket_no']
        ticket = tickets.objects.get(id=ticket_no)
        details={
            'id':ticket.id,
            'customer_id': ticket.customer_id,
            'teller_id': ticket.teller_id,
            'ticket_no': ticket.ticket,
            'status': ticket.status,
            'created_at': ticket.created_at,
            'updated_at': ticket.updated_at
        }

        data = []
        datas = []

        for cats in details:
            customer = customers.objects.get(id=cats['customer_id'])
            teller = tellers.objects.get(id=cats['teller_id'])
            val={
                'ticket_id':cats['id'],
                'customer_fname': customer.fname,
                'teller_fname': teller.fname,
                'customer_lname': customer.lname,
                'teller_lname': teller.lname,
                'counter_id': teller.counter_id,
                'ticket_no': cats['ticket_no'],
                'created_at': cats['created_at'],
                'updated_at': cats['updated_at']
            }

            data.append(val)

        for ca in data:
            counter = counters.objects.get(id=ca['counter_id'])
            services = service.objects.get(id=counter.service_id)
            vals={
                'ticket_id':ca['ticket_id'],
                'customer_fname': ca['customer_fname'],
                'teller_fname': ca['teller_fname'],
                'customer_lname': ca['customer_lname'],
                'teller_lname': ca['teller_lname'],
                'service_name': services.name,
                'ticket_no': ca['ticket_no'],
                'created_at': ca['created_at'],
                'updated_at': ca['updated_at']
            }

            datas.append(vals)

        data={
            'data':datas,
            'message':'success',
            'status_code':200
            }
        return Response(data)


#get particular teller's tickets 
@api_view(['POST'])  
def get_particular_tellers_tickets(request):

    """
    Get particular teller's tickets 
    -----
        {
            page: 1
            items: 10
            teller_id: 1
        }
    """
    if request.method == 'GET':
        success={'message':'method not allowed','status_code':401}
        return Response(success)

    elif request.method == 'POST':

        teller_id = request.data['teller_id']
        all = tickets.objects.filter(teller_id=teller_id).count()
        ticketss = tickets.objects.filter(teller_id=teller_id)
        page = request.GET.get('page', request.data['page'])
        paginator = Paginator(ticketss, request.data['items'])
        details=[]
        data=[]
        datas=[]
        for ticket in paginator.page(page):
            values={
                'id':ticket.id,
                'customer_id': ticket.customer_id,
                'teller_id': ticket.teller_id,
                'ticket_no': ticket.ticket,
                'status': ticket.status,
                'created_at': ticket.created_at,
                'updated_at': ticket.updated_at
            }

            details.append(values)

        for cats in details:
            customer = customers.objects.get(id=cats['customer_id'])
            teller = tellers.objects.get(id=cats['teller_id'])
            val={
                'ticket_id':cats['id'],
                'customer_fname': customer.fname,
                'teller_fname': teller.fname,
                'customer_lname': customer.lname,
                'teller_lname': teller.lname,
                'counter_id': teller.counter_id,
                'ticket_no': cats['ticket_no'],
                'created_at': cats['created_at'],
                'updated_at': cats['updated_at']
            }

            data.append(val)

        for ca in data:
            counter = counters.objects.get(id=ca['counter_id'])
            services = service.objects.get(id=counter.service_id)
            vals={
                'ticket_id':ca['ticket_id'],
                'customer_fname': ca['customer_fname'],
                'teller_fname': ca['teller_fname'],
                'customer_lname': ca['customer_lname'],
                'teller_lname': ca['teller_lname'],
                'service_name': services.name,
                'ticket_no': ca['ticket_no'],
                'created_at': ca['created_at'],
                'updated_at': ca['updated_at']
            }

            datas.append(vals)

        data={
            'data':datas,
            'total': all,
            'message':'success',
            'status_code':200
            }
        return Response(data)


#Serve existing ticket    
@api_view(['POST'])
def serve_ticket(request):    
    """
    Serve ticket
    -----
        {
            ticket_no:1,
            teller_id : 1
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            log = logs(
                ticket_no=request.data['ticket_no'], 
                teller_id=request.data['teller_id'],
                created_at = datetime.datetime.today(),
                updated_at= datetime.datetime.today()
            )
            log.save()
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

#ticket_being_served    
@api_view(['POST'])
def ticket_being_served(request):
    """
    Ticket being served by teller
    -----
        {
            teller_id:1
        }
    """
    try:
        if request.method == 'GET':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'POST':
            current = logs.objects.filter(teller_id = request.data['teller_id']).latest('created_at')
            success={
                'message':'success',
                'data': current.ticket_no,
                'status_code':200
            }
            return Response(success)
            
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error) 

#ticket_being_served    
@api_view(['GET'])
def no_to_send_message(request):
    try:
        if request.method == 'POST':
            snippets='success'
            return Response(snippets, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'GET':
            current = logs.objects.latest('created_at')
            person_five_ticket = current.ticket_no + 5
            person_one_ticket = current.ticket_no + 1
            ticket_five = tickets.objects.get(ticket = person_five_ticket)
            ticket_one = tickets.objects.get(ticket = person_one_ticket)
            customer_five = customers.objects.get(id = ticket_five.customer_id)
            customer_one = customers.objects.get(id = ticket_one.customer_id)
            success={
                'message':'success',
                'data_five': customer_five.msisdn,
                'data_one': customer_one.msisdn,
                'status_code':200
            }
            return Response(success)
            
    except BaseException as e:

        error={
            'status_code':500,
            'message':'error:'+ str(e),
        }
        return Response(error) 