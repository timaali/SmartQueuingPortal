import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit {
  @ViewChild('input') myInput: any;
  creator = {
    msisdn: '',
    password: '',
    fname: '',
    lname: '',
    email: '',
    service_id: '',
    name: '',
    number: ''
  }
  content: any;
  counters: Object;
  number: any;
  success: any;
  status: any;
  counter_id: any;
  service_id: any

  constructor(private activatedroute: ActivatedRoute, private apiservice: ApiService) { }

  ngOnInit() {
    this.number = this.activatedroute.snapshot.paramMap.get('component')
    switch (this.number) {
      case '1':
        this.content = 1;
        break;
      case '2':
        this.content = 2;
        break;
      case '3':
        this.content = 3;
        this.counter_id = this.activatedroute.snapshot.paramMap.get('counter_id')
        this.apiservice.getParticularCounter(this.counter_id).subscribe(data => {
          this.counters = data;
        })
        break;
      case '4':
        this.content = 4;
        break;
      default:
        this.content = 1;
    }
  }

  create() {
    switch (this.number) {
      case '1':
        const data = {
          fname: this.creator.fname,
          lname: this.creator.lname,
          email: this.creator.email,
          msisdn: this.creator.msisdn,
          password: this.creator.password,
          role: 'CUSTOMER'
        }
        this.apiservice.createCustomer(data).subscribe(response => {
          this.status = response
          if (this.status.status_code == 200) {
            this.success = 'Customer successfully created'
          } else {
            this.success = 'Customer not created'
          }
        })
        break;
      case '2':
        const datas = {
          name: this.creator.name,
        }
        this.apiservice.createService(datas).subscribe(response => {
          this.status = response
          if (this.status.status_code == 200) {
            this.success = 'Service successfully created'
          } else {
            this.success = 'Service not created'
          }
        })
        break;
      case '3':
        const dat = {
          fname: this.creator.fname,
          lname: this.creator.lname,
          email: this.creator.email,
          counter_id: this.counter_id,
          password: this.creator.password,
          role: 'TELLER'
        }
        this.apiservice.createTeller(dat).subscribe(response => {
          this.status = response
          if (this.status.status_code == 200) {
            this.success = 'Teller successfully created'
          } else {
            this.success = 'Teller not created'
          }
        })
        break;

      case '4':
        const dat = {
          number: this.creator.number,
          service_id: this.activatedroute.snapshot.paramMap.get('counter_id')
        }
        this.apiservice.createCounter(dat).subscribe(response => {
          this.status = response
          if (this.status.status_code == 200) {
            this.success = 'Counter successfully created'
          } else {
            this.success = 'Counter not created'
          }
        })
        break;
      default:
        this.content = 1;
    }
  }
}
