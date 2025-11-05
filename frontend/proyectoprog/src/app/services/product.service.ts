import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://127.0.0.1:7000'; // Base URL for your backend

  constructor(private http: HttpClient) { }

  getProducts(page: number, per_page: number, name?: string, category?: string): Observable<any> {
    let params = new HttpParams();
    params = params.append('page', page.toString());
    params = params.append('per_page', per_page.toString());
    if (name) {
      params = params.append('name', name);
    }
    if (category) {
      params = params.append('category', category);
    }
    return this.http.get(`${this.apiUrl}/products`, { params });
  }
}
