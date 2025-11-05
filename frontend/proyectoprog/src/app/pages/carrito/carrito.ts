import { Component, OnInit } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { UniversalCard } from "../../components/universal-card/universal-card";
import { Card } from "../../components/card/card";
import { ActionBttn } from '../../components/action-bttn/action-bttn';
import { TextArea } from "../../components/textarea/textarea";
import { CalifiEstrellas } from '../../components/calfiestrellas/calfiestrellas';
import { OrderService } from '../../services/order.service';
import { RatingService } from '../../services/rating.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-carrito',
  standalone: true,
  imports: [Navbar, UniversalCard, ActionBttn, TextArea, Card, CommonModule, CalifiEstrellas, FormsModule],
  templateUrl: './carrito.html',
  styleUrl: './carrito.css'
})
export class Carrito implements OnInit {
  orders: any[] = [];
  del_status: string = '';
  del_price: string = '$5.000'; // Assuming a fixed price for now
  del_address: string = '';
  tabseleccionada = "pedido"
  rating: number = 0;
  comment: string = '';

  constructor(private orderService: OrderService, private ratingService: RatingService) { }

  ngOnInit(): void {
    this.loadOrders();
  }

  loadOrders(): void {
    this.orderService.getOrders().subscribe({
      next: (response) => {
        this.orders = response.orders;
        if (this.orders.length > 0) {
          this.del_status = this.orders[0].status;
          this.del_address = this.orders[0].user?.address;
        }
      },
      error: (err) => {
        console.error('Error loading orders', err);
      }
    });
  }

  submitRating(productId: number): void {
    this.ratingService.createRating(productId, this.rating, this.comment).subscribe({
      next: (response) => {
        console.log('Rating submitted', response);
        alert('Calificación enviada');
      },
      error: (err) => {
        console.error('Error submitting rating', err);
        alert('Error al enviar la calificación');
      }
    });
  }

  onRatingChanged(rating: number): void {
    this.rating = rating;
  }
}
