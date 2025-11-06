import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  private apiUrl = 'http://127.0.0.1:7000/orders';

  constructor(private http: HttpClient) { }

  getOrders(): Observable<any> {
    return this.http.get<any>(this.apiUrl);
  }

  createOrder(orderData: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, orderData);
  }

  updateOrder(id: number, data: any): Observable<any> {
    return this.http.patch<any>(`${this.apiUrl}/${id}`, data);
  }

  addProductToOrder(productId: number, quantity: number): Observable<any> {
    return this.http.post<any>(this.apiUrl, { product_id: productId, quantity: quantity });
  }
}
