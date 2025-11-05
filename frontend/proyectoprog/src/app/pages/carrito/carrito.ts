import { Component, OnInit } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { UniversalCard } from "../../components/universal-card/universal-card";
import { Card } from "../../components/card/card";
import { ActionBttn } from '../../components/action-bttn/action-bttn';
import { TextArea } from "../../components/textarea/textarea";
import { CalifiEstrellas } from '../../components/calfiestrellas/calfiestrellas';
import { OrderService } from '../../services/order.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-carrito',
  standalone: true,
  imports: [Navbar, UniversalCard, ActionBttn, TextArea, Card, CommonModule, CalifiEstrellas],
  templateUrl: './carrito.html',
  styleUrl: './carrito.css'
})
export class Carrito implements OnInit {
  orders: any[] = [];
  del_status: string = '';
  del_price: string = '$5.000'; // Assuming a fixed price for now
  del_address: string = '';
  tabseleccionada = "pedido"

  constructor(private orderService: OrderService) { }

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
}
