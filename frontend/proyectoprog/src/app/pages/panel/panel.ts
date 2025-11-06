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
  unvalidatedUsers: any[] = [];
  clientUsers: any[] = [];

  promotionForm: FormGroup;
  newOrderForm: FormGroup;

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

    this.newOrderForm = this.fb.group({
      clientName: ['', Validators.required],
      products: ['', Validators.required],
      total: [0, [Validators.required, Validators.min(0.01)]]
    });
  }

  ngOnInit(): void {
    this.rol = this.authService.getUserRole();
    if (this.rol === 'Empleado') {
      this.tabseleccionada = 'Pedidos';
    }
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
      next: (response: any) => {
        this.zone.run(() => {
          this.products = response.products || [];
        });
      },
      error: (err: any) => { console.error('Error loading products', err); }
    });
  }

  loadOrders(): void {
    this.orderService.getOrders().subscribe({
      next: (response: any) => {
        this.zone.run(() => {
          this.orders = response.orders || [];
        });
      },
      error: (err: any) => { console.error('Error loading orders', err); }
    });
  }

  loadUsers(): void {
    this.userService.getUsers().subscribe({
      next: (response: any) => {
        this.zone.run(() => {
          this.users = response.users || [];
          this.unvalidatedUsers = this.users.filter(u => u.role === 'Client' && !u.is_active);
          this.clientUsers = this.users.filter(u => u.role === 'Client');
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

  deleteUser(id: number): void {
    if (confirm('Are you sure you want to delete this user?')) {
      this.userService.deleteUser(id).subscribe({
        next: () => {
          this.loadUsers();
        },
        error: (err: any) => {
          console.error('Error deleting user', err);
        }
      });
    }
  }

  updateOrderStatus(orderId: number, status: string): void {
    console.log(`Updating order ${orderId} to status ${status}`);
    // TODO: Implement this.orderService.updateOrder(orderId, { status: status }) when available in the service.
    const order = this.orders.find(o => o.id === orderId);
    if (order) {
      order.status = status;
      this.cdr.detectChanges(); // Refresh view after local change
    }
    alert(`El estado del pedido #${orderId} se cambió a "${status}" (simulación).`);
  }

  validateUser(userId: number): void {
    this.userService.updateUser(userId, { is_active: true }).subscribe({
      next: () => {
        alert(`Usuario ${userId} ha sido validado.`);
        this.loadUsers(); // Reload users to reflect change
      },
      error: (err: any) => {
        console.error(`Error validating user ${userId}`, err);
        alert('Error al validar el usuario.');
      }
    });
  }

  blockUser(userId: number): void {
    if (confirm(`¿Estás seguro de que quieres bloquear al usuario ${userId}?`)) {
      this.userService.updateUser(userId, { is_active: false }).subscribe({
        next: () => {
          alert(`Usuario ${userId} ha sido bloqueado.`);
          this.loadUsers();
        },
        error: (err: any) => {
          console.error(`Error blocking user ${userId}`, err);
          alert('Error al bloquear al usuario.');
        }
      });
    }
  }

  createOrder(): void {
    if (this.newOrderForm.valid) {
      console.log('Creating order with:', this.newOrderForm.value);
      // TODO: Implement this.orderService.createOrder(...) when available in the service.
      alert('Pedido creado (simulación).');
      this.newOrderForm.reset();
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

