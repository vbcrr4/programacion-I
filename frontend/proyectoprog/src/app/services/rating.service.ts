import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RatingService {
  private apiUrl = 'http://127.0.0.1:7000/ratings';

  constructor(private http: HttpClient) { }

  createRating(productId: number, rating: number, comment: string): Observable<any> {
    return this.http.post<any>(this.apiUrl, { product_id: productId, rating: rating, comment: comment });
  }
}
