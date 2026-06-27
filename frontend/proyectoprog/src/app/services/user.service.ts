import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://127.0.0.1:7000/users';

  constructor(private http: HttpClient) { }

  getUsers(page?: number, perPage?: number, address?: string, role?: string, nrOrders?: number, name?: string, email?: string, is_active?: boolean): Observable<any> {
    let params = new HttpParams();
    if (page) params = params.append('page', page.toString());
    if (perPage) params = params.append('per_page', perPage.toString());
    if (address) params = params.append('address', address);
    if (role) params = params.append('role', role);
    if (nrOrders) params = params.append('nrOrders', nrOrders.toString());
    if (name) params = params.append('name', name);
    if (email) params = params.append('email', email);
    if (is_active !== undefined) params = params.append('is_active', is_active ? '1' : '0');

    return this.http.get<any>(this.apiUrl, { params });
  }

  getUser(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/${id}`);
  }

  updateUser(id: number, data: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/${id}`, data);
  }

  deleteUser(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/${id}`);
  }
}
