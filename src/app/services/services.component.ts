import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-services',
  templateUrl: './services.component.html',
  styleUrls: ['./services.component.scss']
})
export class ServicesComponent implements OnInit {

  services: Object;
  success: any;
  status: any;

  constructor( private apiservice: ApiService ) { }

  ngOnInit() {
    this.apiservice.getServices().subscribe(data => {
      this.services = data;
    })
  }

  delete(service_id: any){
    const data={
      service_id: service_id
    }
    this.apiservice.deleteservice(data).subscribe(response=>{
      this.status = response
      if(this.status.status_code == 200){
        this.success='Service Deleted'
        this.ngOnInit()
      }else{
        this.success='Service not deleted'
      }
    })
  }

}
