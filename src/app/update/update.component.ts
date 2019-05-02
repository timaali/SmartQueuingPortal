import { Component, OnInit, ViewChild } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UpdateComponent implements OnInit {
  @ViewChild('input') myInput: any;
  updator = {
    msisdn:'',
    password: '',
    fname: '',
    lname: '',
    email: '',
    service_id: '',
    name: ''
  }
  content: any;
  services: Object;
  number: any;
  success: any;
  id: any;
  status: any;

  constructor( private activatedroute: ActivatedRoute, private apiservice: ApiService ) { }

  ngOnInit() {
    this.number = this.activatedroute.snapshot.paramMap.get('update')
    this.id = this.activatedroute.snapshot.paramMap.get('id')
    switch(this.number) {
      case '1':
        this.content = 1;
        break;
      case '2':
        this.content = 2;
        break;
      case '3':
        this.content = 3;
        this.apiservice.getServices().subscribe(data => {
          this.services = data;
        })
        break;
      default:
        this.content = 1;
    }
  }

  update(){
    switch(this.number) {
      case '1':
        const data ={
          fname:this.updator.fname,
          lname:this.updator.lname,
          email:this.updator.email,
          msisdn:this.updator.msisdn,
          password:this.updator.password,
          id: this.id
        }
        this.apiservice.updateCustomer(data).subscribe(response =>{
          this.status = response
          if(this.status.status_code == 200){
            this.success='Customer successfully updated'
            this.updator = {
              msisdn:'',
              password: '',
              fname: '',
              lname: '',
              email: '',
              service_id: '',
              name: ''
            }
          }else{
            this.success='Customer not updated'
            this.updator = {
              msisdn:'',
              password: '',
              fname: '',
              lname: '',
              email: '',
              service_id: '',
              name: ''
            }
          }
        })
        break;
      case '2':
        const datas ={
          name:this.updator.name,
          id: this.id
        }
        this.apiservice.updateService(datas).subscribe(response =>{
          this.status = response
          if(this.status.status_code == 200){
            this.success='Service successfully updated'
            this.updator = {
              msisdn:'',
              password: '',
              fname: '',
              lname: '',
              email: '',
              service_id: '',
              name: ''
            }
          }else{
            this.success='Service not updated'
            this.updator = {
              msisdn:'',
              password: '',
              fname: '',
              lname: '',
              email: '',
              service_id: '',
              name: ''
            }
          }
        })
        break;
      case '3':
        const dat ={
          fname:this.updator.fname,
          lname:this.updator.lname,
          email:this.updator.email,
          service_id:this.updator.service_id,
          password:this.updator.password,
          id:this.id
        }
        this.apiservice.updateTeller(dat).subscribe(response =>{
          this.status = response
          if(this.status.status_code == 200){
            this.success='Teller successfully updated'
            this.updator = {
              msisdn:'',
              password: '',
              fname: '',
              lname: '',
              email: '',
              service_id: '',
              name: ''
            }
          }else{
            this.success='Teller not updated'
            this.updator = {
              msisdn:'',
              password: '',
              fname: '',
              lname: '',
              email: '',
              service_id: '',
              name: ''
            }
          }
        })
        break;
      default:
        this.content = 1;
    }
  }
}
