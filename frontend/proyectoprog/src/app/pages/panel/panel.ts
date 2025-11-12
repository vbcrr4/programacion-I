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
import { SearchbarComponent } from '../../components/searchbar/searchbar';

@Component({
  selector: 'app-panel',
  imports: [Navbar, CardContenedora, Card, ActionBttn, TextArea,UniversalCard,InputField, ButtonField, CommonModule, ReactiveFormsModule, SearchbarComponent],
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

  currentPage: number = 1;
  totalPages: number = 1;
  perPage: number = 5;
  searchTerms: { name: string, category: string } = { name: '', category: '' };

  orderCurrentPage: number = 1;
  orderTotalPages: number = 1;
  orderPerPage: number = 5;
  orderSearchTerms: { name: string, category: string } = { name: '', category: '' };
  orderUserId: number | null = null;

  userCurrentPage: number = 1;
  userTotalPages: number = 1;
  userPerPage: number = 5;
  userSearchTerms: { name: string, category: string } = { name: '', category: '' };

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
    this.productService.getProducts(this.currentPage, this.perPage, this.searchTerms.name, this.searchTerms.category).subscribe({
      next: (response: any) => {
        this.zone.run(() => {
          this.products = response.products || [];
          this.totalPages = response.pages;
          this.currentPage = response.page;
        });
      },
      error: (err: any) => { console.error('Error loading products', err); }
    });
  }

  onSearch(searchTerms: any): void {
    this.currentPage = 1;
    this.searchTerms = searchTerms;
    this.loadProducts();
  }

  goToPage(page: number): void {
    if (page >= 1 && page <= this.totalPages) {
      this.currentPage = page;
      this.loadProducts();
    }
  }

  nextPage(): void {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
      this.loadProducts();
    }
  }

  prevPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.loadProducts();
    }
  }

  getPagesArray(): number[] {
    return Array.from({ length: this.totalPages }, (_, i) => i + 1);
  }

  loadOrders(): void {
    this.orderService.getOrders(this.orderCurrentPage, this.orderPerPage, this.orderSearchTerms.category, this.orderUserId ?? undefined).subscribe({
      next: (response: any) => {
        this.zone.run(() => {
          this.orders = response.orders || [];
          this.orderTotalPages = response.pages;
          this.orderCurrentPage = response.page;
        });
      },
      error: (err: any) => { console.error('Error loading orders', err); }
    });
  }

  onOrderSearch(searchTerms: any): void {
    this.orderCurrentPage = 1;
    this.orderSearchTerms = searchTerms;
    if (searchTerms.name) {
      this.userService.getUsers(1, 1, undefined, undefined, undefined, searchTerms.name).subscribe({
        next: (response) => {
          if (response.users && response.users.length > 0) {
            this.orderUserId = response.users[0].id;
          } else {
            this.orderUserId = -1; // Use a non-existent ID to return no orders
          }
          this.loadOrders();
        },
        error: (err) => {
          console.error('Error searching for user', err);
          this.orderUserId = null;
          this.loadOrders(); // Load orders without user filter
        }
      });
    } else {
      this.orderUserId = null;
      this.loadOrders();
    }
  }

  goToOrderPage(page: number): void {
    if (page >= 1 && page <= this.orderTotalPages) {
      this.orderCurrentPage = page;
      this.loadOrders();
    }
  }

  nextOrderPage(): void {
    if (this.orderCurrentPage < this.orderTotalPages) {
      this.orderCurrentPage++;
      this.loadOrders();
    }
  }

  prevOrderPage(): void {
    if (this.orderCurrentPage > 1) {
      this.orderCurrentPage--;
      this.loadOrders();
    }
  }

  getOrderPagesArray(): number[] {
    return Array.from({ length: this.orderTotalPages }, (_, i) => i + 1);
  }

  loadUsers(): void {
    this.userService.getUsers(this.userCurrentPage, this.userPerPage, undefined, this.userSearchTerms.category, undefined, this.userSearchTerms.name).subscribe({
      next: (response: any) => {
        this.zone.run(() => {
          this.users = response.users || [];
          this.userTotalPages = response.pages;
          this.userCurrentPage = response.page;
          this.unvalidatedUsers = this.users.filter(u => u.role === 'Client' && !u.is_active);
          this.clientUsers = this.users.filter(u => u.role === 'Client');
        });
      },
      error: (err: any) => { console.error('Error loading users', err); }
    });
  }

  onUserSearch(searchTerms: any): void {
    this.userCurrentPage = 1;
    this.userSearchTerms = searchTerms;
    this.loadUsers();
  }

  goToUserPage(page: number): void {
    if (page >= 1 && page <= this.userTotalPages) {
      this.userCurrentPage = page;
      this.loadUsers();
    }
  }

  nextUserPage(): void {
    if (this.userCurrentPage < this.userTotalPages) {
      this.userCurrentPage++;
      this.loadUsers();
    }
  }

  prevUserPage(): void {
    if (this.userCurrentPage > 1) {
      this.userCurrentPage--;
      this.loadUsers();
    }
  }

  getUserPagesArray(): number[] {
    return Array.from({ length: this.userTotalPages }, (_, i) => i + 1);
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
  
  // ... rest of the file

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
    this.orderService.updateOrder(orderId, { status }).subscribe({
      next: (updatedOrder: any) => {
        const index = this.orders.findIndex(o => o.id === orderId);
        if (index !== -1) {
          this.orders[index] = updatedOrder;
          this.cdr.detectChanges();
        }
        alert('Estado del pedido actualizado.');
      },
      error: (err: any) => {
        console.error(`Error updating order ${orderId}`, err);
        alert('Error al actualizar el pedido.');
      }
    });
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
      // Note: This is a simplified implementation. A real-world scenario would likely require
      // resolving clientName to a user ID and products to a structured list of product IDs.
      this.orderService.createOrder(this.newOrderForm.value).subscribe({
        next: () => {
          alert('Pedido creado con éxito.');
          this.newOrderForm.reset();
          this.selectTab('Pedidos'); // Switch to orders tab to see the new order
          this.loadOrders();
        },
        error: (err: any) => {
          console.error('Error creating order', err);
          alert('Error al crear el pedido.');
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

