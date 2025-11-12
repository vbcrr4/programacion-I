import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OrderService {
  private apiUrl = 'http://127.0.0.1:7000/orders';

  constructor(private http: HttpClient) { }

  getOrders(page: number = 1, per_page: number = 10, status?: string, userId?: number): Observable<any> {
    let params = new HttpParams()
      .set('page', page.toString())
      .set('per_page', per_page.toString());

    if (status) {
      params = params.set('status', status);
    }
    if (userId) {
      params = params.set('user_id', userId.toString());
    }

    return this.http.get<any>(this.apiUrl, { params });
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
