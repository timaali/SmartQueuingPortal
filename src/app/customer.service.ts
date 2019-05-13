import { Injectable } from '@angular/core';

const TOKEN = 'TOKEN';

@Injectable({
  providedIn: 'root'
})
export class CustomerService {

  constructor() { }

  setToken(token: any): void {
    localStorage.setItem(TOKEN, JSON.stringify(token));
  }

  isLogged() {
    return localStorage.getItem(TOKEN) != null;
  }

  checkRole(){
    return localStorage.getItem(TOKEN)
  }
}
