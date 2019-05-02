import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  api: String = 'http://127.0.0.1:8000'
  data: Object;

  constructor( private http: HttpClient ) { }

  getCustomers(){
    const data={
      page:'1',
      items:'10',
    }
    return this.http.post(this.api+'/customer/getallcustomers/', data)
  }

  getTellers(){
    const data={
      page:'1',
      items:'10',
    }
    return this.http.post(this.api+'/tellers/getalltellers/', data)
  }

  getServices(){
    const data={
      page:'1',
      items:'10',
    }
    return this.http.post(this.api+'/services/getallservices/', data)
  }

  getTickets(teller_id: any){
    const data={
      teller_id: teller_id,
      page:'1',
      items:'10',
    }
    return this.http.post(this.api+'/tellers/getparticulartellertickets/', data)
  }

  bookTicket(data: any){
    return this.http.post(this.api+'/tickets/createticket/', data)
  }

  ticketBeingServed(service_id: any){
    const data={
      service_id: service_id,
    }
    return this.http.post(this.api+'/tickets/ticketbeingserved/', data)
  }

  createCustomer(data: any){
    return this.http.post(this.api+'/customer/createcustomer/', data)
  }

  createService(data: any){
    return this.http.post(this.api+'/services/createservice/', data)
  }

  createTeller(data: any){
    return this.http.post(this.api+'/tellers/createteller/', data)
  }

  updateCustomer(data: any){
    return this.http.post(this.api+'/customer/updatecustomer/', data)
  }

  updateService(data: any){
    return this.http.post(this.api+'/services/updateservice/', data)
  }

  updateTeller(data: any){
    return this.http.post(this.api+'/tellers/updateteller/', data)
  }

  cancelTicket(ticket: any){
    return this.http.post(this.api+'/tickets/cancelticket/', ticket)
  }

  deleteuser(id: any){
    return this.http.post(this.api+'/customer/deletecustomer/', id)
  }

  deleteservice(id: any){
    return this.http.post(this.api+'/services/deleteservice/', id)
  }

  deleteteller(id: any){
    return this.http.post(this.api+'/tellers/deleteteller/', id)
  }

}
