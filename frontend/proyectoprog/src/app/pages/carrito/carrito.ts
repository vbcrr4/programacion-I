import { Component, OnInit } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { UniversalCard } from "../../components/universal-card/universal-card";
import { Card } from "../../components/card/card";
import { ActionBttn } from '../../components/action-bttn/action-bttn';
import { ButtonField } from '../../components/button/button';
import { TextArea } from "../../components/textarea/textarea";
import { CalifiEstrellas } from '../../components/calfiestrellas/calfiestrellas';
import { OrderService } from '../../services/order.service';
import { RatingService } from '../../services/rating.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-carrito',
  standalone: true,
  imports: [Navbar, UniversalCard, ActionBttn, TextArea, Card, CommonModule, CalifiEstrellas, FormsModule, ButtonField],
  templateUrl: './carrito.html',
  styleUrl: './carrito.css'
})
export class Carrito implements OnInit {
  orders: any[] = [];
  del_status: string = '';
  del_price: number = 0;
  del_address: string = '';
  tabseleccionada = "pedido"
  ratings: { [productId: number]: number } = {};
  comments: { [productId: number]: string } = {};

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
          this.del_price = this.orders[0].total;

          // Initialize ratings and comments for each product in the last order
          this.orders[0].order_details.forEach((detail: any) => {
            this.ratings[detail.product.id] = 0;
            this.comments[detail.product.id] = '';
          });
        }
      },
      error: (err) => {
        console.error('Error loading orders', err);
      }
    });
  }

  submitRating(productId: number): void {
    const rating = this.ratings[productId] || 0;
    const comment = this.comments[productId] || '';
    if (rating === 0) {
      alert('Por favor, selecciona una calificación');
      return;
    }
    this.ratingService.createRating(productId, rating, comment).subscribe({
      next: (response) => {
        console.log('Rating submitted', response);
        alert('Calificación enviada para el producto.');
      },
      error: (err) => {
        console.error('Error submitting rating', err);
        alert('Error al enviar la calificación');
      }
    });
  }
}
