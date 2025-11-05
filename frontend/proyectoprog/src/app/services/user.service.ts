import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private apiUrl = 'http://127.0.0.1:7000'; // Base URL for your backend

  constructor(private http: HttpClient) { }

  getUser(userId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/users/${userId}`);
  }

  updateUser(userId: number, userData: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/users/${userId}`, userData);
  }

  deleteUser(userId: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/users/${userId}`);
  }

  getUsers(page: number, per_page: number, address?: string, role?: string, nrOrders?: number): Observable<any> {
    let params = new HttpParams();
    params = params.append('page', page.toString());
    params = params.append('per_page', per_page.toString());
    if (address) {
      params = params.append('address', address);
    }
    if (role) {
      params = params.append('role', role);
    }
    if (nrOrders) {
      params = params.append('nrOrders', nrOrders.toString());
    }
    return this.http.get(`${this.apiUrl}/users`, { params });
  }

  createUser(userData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/users`, userData);
  }
}
