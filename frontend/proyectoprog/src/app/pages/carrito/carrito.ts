import { Component, OnInit } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { UniversalCard } from "../../components/universal-card/universal-card";
import { Card } from "../../components/card/card";
import { ActionBttn } from '../../components/action-bttn/action-bttn';
import { TextArea } from "../../components/textarea/textarea";
import { OrderService } from '../../services/order.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-carrito',
  standalone: true,
  imports: [Navbar, UniversalCard, ActionBttn, TextArea, Card, CommonModule],
  templateUrl: './carrito.html',
  styleUrl: './carrito.css'
})
export class Carrito implements OnInit {
  orders: any[] = [];
  status = "Listo"
  del_status = "En camino"
  del_price = "$5.000"
  del_address = "Av. Boulogne Sur Mer 683, M5500 Mendoza"
  tabseleccionada = "pedido"

  constructor(private orderService: OrderService) { }

  ngOnInit(): void {
    this.loadOrders();
  }

  loadOrders(): void {
    this.orderService.getOrders().subscribe({
      next: (response) => {
        this.orders = response.orders;
      },
      error: (err) => {
        console.error('Error loading orders', err);
      }
    });
  }
}
