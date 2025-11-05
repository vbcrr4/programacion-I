import { Component, OnInit, ChangeDetectorRef, NgZone } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { CardContenedora } from "../../components/card-contenedora/card-contenedora";
import { Card } from "../../components/card/card";
import { ActionBttn } from '../../components/action-bttn/action-bttn';
import { TextArea } from "../../components/textarea/textarea";
import { CalifiEstrellas } from '../../components/calfiestrellas/calfiestrellas';
import { UniversalCard } from '../../components/universal-card/universal-card';
import { InputField } from '../../components/input/input';
import { ButtonField } from '../../components/button/button';
import { AuthService } from '../../services/auth.service';
import { ProductService } from '../../services/product.service';
import { OrderService } from '../../services/order.service';
import { UserService } from '../../services/user.service';
import { PromotionService } from '../../services/promotion.service';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-panel',
  imports: [Navbar, CardContenedora, Card, ActionBttn, TextArea,UniversalCard,InputField, ButtonField, CommonModule, ReactiveFormsModule],
  templateUrl: './panel.html',
  styleUrl: './panel.css'
})
export class Panel implements OnInit {
  rol: string | null = null;
  tabseleccionada: string = "Gestion de menu";

  products: any[] = [];
  orders: any[] = [];
  users: any[] = [];

  promotionForm: FormGroup;

  constructor(
    private authService: AuthService,
    private productService: ProductService,
    private orderService: OrderService,
    private userService: UserService,
    private promotionService: PromotionService,
    private fb: FormBuilder,
    private cdr: ChangeDetectorRef,
    private zone: NgZone
  ) {
    this.promotionForm = this.fb.group({
      from: ['', [Validators.required, Validators.email]],
      to: ['', Validators.required],
      message: ['', Validators.required],
      discountCode: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.rol = this.authService.getUserRole();
    this.loadProducts();
    this.loadOrders();
    this.loadUsers();
  }

  selectTab(tabName: string) {
    this.tabseleccionada = tabName;
  }

  getBadgeClass(status: string): string {
    if (!status) {
      return 'bg-secondary';
    }
    const cleanStatus = status.trim().toLowerCase();
    switch (cleanStatus) {
      case 'entregado':
      case 'ready':
        return 'bg-success';
      case 'en preparación':
      case 'preparing':
        return 'bg-warning text-dark';
      case 'cancelado':
      case 'canceled':
        return 'bg-danger';
      case 'pendiente':
      case 'pending':
        return 'bg-info text-dark';
      default:
        return 'bg-secondary';
    }
  }

  loadProducts(): void {
    this.productService.getProducts().subscribe({
      next: (response) => {
        this.zone.run(() => {
          this.products = response.products || [];
        });
      },
      error: (err: any) => { console.error('Error loading products', err); }
    });
  }

  loadOrders(): void {
    this.orderService.getOrders().subscribe({
      next: (response) => {
        this.zone.run(() => {
          this.orders = response.orders || [];
        });
      },
      error: (err: any) => { console.error('Error loading orders', err); }
    });
  }

  loadUsers(): void {
    this.userService.getUsers().subscribe({
      next: (response) => {
        this.zone.run(() => {
          this.users = response.users || [];
        });
      },
      error: (err: any) => { console.error('Error loading users', err); }
    });
  }

  deleteProduct(id: number): void {
    if (confirm('Are you sure you want to delete this product?')) {
      this.productService.deleteProduct(id).subscribe({
        next: () => {
          this.loadProducts();
        },
        error: (err: any) => {
          console.error('Error deleting product', err);
        }
      });
    }
  }

  sendPromotion(): void {
    if (this.promotionForm.valid) {
      this.promotionService.sendPromotion(this.promotionForm.value).subscribe({
        next: () => {
          alert('Promotion sent successfully!');
          this.promotionForm.reset();
        },
        error: (err: any) => {
          console.error('Error sending promotion', err);
          alert('Error sending promotion.');
        }
      });
    }
  }
}

