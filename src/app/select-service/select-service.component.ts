import { ApiService } from './../api.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-select-service',
  templateUrl: './select-service.component.html',
  styleUrls: ['./select-service.component.scss']
})
export class SelectServiceComponent implements OnInit {

  services: any;
  userData: any;
  success: any;

  constructor(private apiservice: ApiService) { }

  ngOnInit() {
    this.apiservice.getServices().subscribe(data => {
      this.services = data;
    })
    this.userData = JSON.parse(localStorage.getItem('TOKEN'))
  }

}
