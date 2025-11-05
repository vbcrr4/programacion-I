import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://127.0.0.1:7000/products';

  constructor(private http: HttpClient) { }

  getProducts(page?: number, perPage?: number, name?: string, category?: string): Observable<any> {
    let params = new HttpParams();
    if (page) params = params.append('page', page.toString());
    if (perPage) params = params.append('per_page', perPage.toString());
    if (name) params = params.append('name', name);
    if (category) params = params.append('category', category);

    return this.http.get<any>(this.apiUrl, { params });
  }

  updateProduct(id: number, data: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, data);
  }

  deleteProduct(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`);
  }

  createProduct(data: any): Observable<any> {
    return this.http.post<any>(this.apiUrl, data);
  }
}
