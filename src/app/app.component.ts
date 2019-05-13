import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CustomerService } from './customer.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit  {
  title = 'star-admin-angular';
  user: any;
  userData: any

  constructor( private customer: CustomerService, private router: Router ) { }
  ngOnInit() {
    if (this.customer.isLogged()) {
      this.userData = JSON.parse(localStorage.getItem('TOKEN'))
      if(this.userData.role === 'SUPER'){
        this.user = true;
        return this.router.navigateByUrl('/dashboard');
      }else if(this.userData.role === 'CUSTOMER'){
        this.user = false;
        return this.router.navigateByUrl('/selectService');
      }else if(this.userData.role === 'TELLER'){
        this.user = false;
        return this.router.navigateByUrl('/tickets/'+this.userData.id);
      }
    }else{
      this.user = false;
    }
  }
}
