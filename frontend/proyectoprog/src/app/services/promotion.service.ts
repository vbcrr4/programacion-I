import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PromotionService {
  // There is no endpoint for promotions in the backend yet.
  // This is a placeholder service.
  private apiUrl = 'http://127.0.0.1:7000/promotions';

  constructor(private http: HttpClient) { }

  sendPromotion(data: any): Observable<any> {
    console.log('Sending promotion', data);
    // Replace with actual HTTP POST request when the endpoint is available.
    return of({ success: true });
  }
}
