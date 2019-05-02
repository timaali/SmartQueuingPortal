import { Component, OnInit, ViewChild } from '@angular/core';
import { ApiService } from '../api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-book',
  templateUrl: './book.component.html',
  styleUrls: ['./book.component.scss']
})
export class BookComponent implements OnInit {

  @ViewChild('input') myInput: any;
  book = {
    msisdn:'',
  }
  services : Object;
  YourTicket: any;
  teller_id: any
  ticketbeignserved: any

  constructor( private apiservice: ApiService, private activatedroute: ActivatedRoute  ) { }

  ngOnInit() {
    this.teller_id=this.activatedroute.snapshot.paramMap.get('teller_id')
    this.apiservice.ticketBeingServed(this.teller_id).subscribe(response => {
      this.ticketbeignserved = response
    })
  }

  Book(){
    const data = {
      customer_msisdn : this.book.msisdn,
      teller_id : this.teller_id
    }
    this.apiservice.bookTicket(data).subscribe(response => {
      this.YourTicket = response
    })
    this.book.msisdn = ''
  }

}
