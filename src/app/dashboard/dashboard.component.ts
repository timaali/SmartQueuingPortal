import { CustomerService } from './../customer.service';
import { Component, OnInit } from '@angular/core';
import { ViewEncapsulation } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['../app.component.scss','./dashboard.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class DashboardComponent implements OnInit {

  customers: Object;
  status: any;
  success: any;
  userData: any

  constructor( private apiservice: ApiService, private customer: CustomerService ) { }

  ngOnInit() {
    this.apiservice.getCustomers().subscribe(data => {
      this.customers = data;
    })
    this.userData = JSON.parse(localStorage.getItem('TOKEN'))
  }

  deleteuser(id: any){
    const data ={
      id: id
    }
    this.apiservice.deleteuser(data).subscribe(response=>{
      this.status = response
      if(this.status.status_code == 200){
        this.success='Customer Deleted'
        this.ngOnInit()
      }else{
        this.success='Customer not deleted'
      }
    })
  }

}
