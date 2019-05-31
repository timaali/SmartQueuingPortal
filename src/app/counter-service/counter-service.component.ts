import { ApiService } from './../api.service';
import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-counter-service',
  templateUrl: './counter-service.component.html',
  styleUrls: ['./counter-service.component.scss']
})
export class CounterServiceComponent implements OnInit {

  service_id : any
  status: any
  counters: any
  userData: any

  constructor(private activatedroute: ActivatedRoute, private apiservice: ApiService) { }

  ngOnInit() {
    this.service_id = this.activatedroute.snapshot.paramMap.get('serviceId')
    const data ={
      service_id:this.service_id,
    }
    this.apiservice.getCounters(data).subscribe(response =>{
      this.status = response
      if(this.status.status_code == 200){
        this.counters = this.status.data
        this.userData = JSON.parse(localStorage.getItem('TOKEN'))
      }
    })
  }

}
