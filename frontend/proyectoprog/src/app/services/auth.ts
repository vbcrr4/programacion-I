import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class Auth {
  
  private http = inject(HttpClient);

  url = 'http://localhost:7000';

  login():Observable<any>{
    let dataLogin = { 
      "password":"admin",
      "email":"admin" 
}
    return this.http.post(this.url+'/auth/login',dataLogin);
  }

}