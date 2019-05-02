import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-tellers',
  templateUrl: './tellers.component.html',
  styleUrls: ['./tellers.component.scss']
})
export class TellersComponent implements OnInit {

  tellers: Object;
  status: any;
  success: any;

  constructor( private apiservice: ApiService ) { }

  ngOnInit() {
    this.apiservice.getTellers().subscribe(data => {
      this.tellers = data;
    })
  }

  delete(teller_id: any){
    const data={
      id: teller_id
    }
    this.apiservice.deleteteller(data).subscribe(response=>{
      this.status = response
      if(this.status.status_code == 200){
        this.success='Teller Deleted'
        this.ngOnInit()
      }else{
        this.success='Teller not deleted'
      }
    })
  }

}
