import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-tickets',
  templateUrl: './tickets.component.html',
  styleUrls: ['./tickets.component.scss']
})
export class TicketsComponent implements OnInit {

  teller_id: any;
  tickets: Object;
  success: any;
  status: any;

  constructor( private activatedroute: ActivatedRoute, private apiservice: ApiService  ) { }

  ngOnInit() {
    this.teller_id = this.activatedroute.snapshot.paramMap.get('ticket_id')
    this.apiservice.getTickets(this.teller_id).subscribe(response =>{
      this.tickets = response;
    })
  }

  cancel(ticket_no: any){
    const data={
      ticket_no: ticket_no,
      teller_id: this.teller_id
    }
    this.apiservice.cancelTicket(data).subscribe(response=>{
      this.status = response
      if(this.status.status_code == 200){
        this.success='Ticket Cancelled'
        this.ngOnInit()
      }else{
        this.success='Ticket not cancelled'
      }
    })
  }

}
