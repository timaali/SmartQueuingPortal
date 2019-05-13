import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../api.service';
import { CustomerService } from '../customer.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  @ViewChild('input') myInput: any;
  log = {
    email: '',
    password: ''
  }
  data: any

  constructor(private api: ApiService, private customer: CustomerService, private router: Router ) { }

  ngOnInit() {
    if (this.customer.isLogged()) {
      return this.router.navigateByUrl('/dashboard');
    }
  }

  tryLogin() {
    const data ={
      email:this.log.email,
      password:this.log.password,
    }
    this.api.login(data).subscribe(response => {
      this.data = response
      if (this.data.status_code == 200) {
        this.customer.setToken(this.data.data);
        if(this.data.data.role === 'SUPER'){
          return this.router.navigateByUrl('/dashboard');
        }else if(this.data.data.role === 'CUSTOMER'){
          return this.router.navigateByUrl('/selectService');
        }else if(this.data.data.role === 'TELLER'){
          return this.router.navigateByUrl('/tickets/'+this.data.data.id);
        }
      }
    },r => {
      alert(r.data.status_code);
    });
  }

}
