from Queu import customers, tellers, tickets, service, counters
from django.conf.urls import url

urlpatterns = [
    
    #Customers routes
    url(r'^customer/createcustomer/', customers.create_customer),
    url(r'^customer/updatecustomer/', customers.update_customer),
    url(r'^customer/deletecustomer/', customers.delete_customer),
    url(r'^customer/getallcustomers/', customers.get_all_customers),
    url(r'^customer/resetcustomerpassword/',customers.update_customer_password),
    url(r'^customer/getparticularcustomer/', customers.get_particular_customer_details),
    url(r'^login', customers.get_person_email_login),


    #Services routes
    url(r'^services/createservice/', service.create_service),
    url(r'^services/updateservice/', service.update_service),
    url(r'^services/deleteservice/', service.delete_service),
    url(r'^services/getallservices/', service.get_all_services),
    url(r'^services/getparticularservice/', service.get_particular_service_details),


    #Counters routes
    url(r'^counter/createcounter/', counters.create_counter),
    url(r'^counter/updatecounter/', counters.update_counter),
    url(r'^counter/deletecounter/', counters.delete_counter),
    url(r'^counter/getallcounter/', counters.get_all_counters),
    url(r'^counter/getparticularcounter/', counters.get_particular_counters_details),
    url(r'^counter/getCountersForService', counters.get_particular_counters_for_service_details),


    #Tellers routes
    url(r'^tellers/createteller/', tellers.create_teller),
    url(r'^tellers/updateteller/', tellers.update_teller),
    url(r'^tellers/deleteteller/', tellers.delete_teller),
    url(r'^tellers/getalltellers/', tellers.get_all_tellers),
    url(r'^tellers/resettellerpassword/',tellers.update_teller_password),
    url(r'^tellers/getparticularteller/', tellers.get_particular_teller_details),
    url(r'^tellers/getparticulartellertickets/', tickets.get_particular_tellers_tickets),

    #Tickets routes
    url(r'^tickets/createticket/', tickets.create_ticket),
    url(r'^tickets/cancelticket/', tickets.cancel_ticket),
    url(r'^tickets/getalltickets/', tickets.get_all_tickets),
    url(r'^tickets/serveticket/',tickets.serve_ticket),
    url(r'^tickets/ticketbeingserved/',tickets.ticket_being_served),
    url(r'^tickets/phoneNumbertosendMessage/',tickets.no_to_send_message),
    url(r'^tickets/getparticularticket/', tickets.get_particular_ticket_details),
    url(r'^counters/getCountersService', counters.get_particular_counters_for_service),

]