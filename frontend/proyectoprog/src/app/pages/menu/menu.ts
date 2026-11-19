import { Component, OnInit } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { UniversalCard } from "../../components/universal-card/universal-card";
import { ProductService } from '../../services/product.service';
import { OrderService } from '../../services/order.service';
import { CommonModule } from '@angular/common';
import { SearchbarComponent } from '../../components/searchbar/searchbar';
import { ButtonField } from '../../components/button/button';

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [Navbar, UniversalCard, CommonModule, SearchbarComponent, ButtonField],
  templateUrl: './menu.html',
  styleUrls: ['./menu.css']
})
export class Menu implements OnInit {
  products: any[] = [];
  currentPage: number = 1;
  totalPages: number = 1;
  perPage: number = 5;
  searchTerms: { name: string, category: string } = { name: '', category: '' };

  constructor(private productService: ProductService, private orderService: OrderService) {}

  ngOnInit(): void {
    this.loadProducts();
  }

  loadProducts(): void {
    this.productService.getProducts(this.currentPage, this.perPage, this.searchTerms.name, this.searchTerms.category).subscribe({
      next: (response) => {
        this.products = response.products;
        this.totalPages = response.pages;
        this.currentPage = response.page;
      },
      error: (err) => {
        console.error('Error loading products', err);
      }
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

  addToCart(productId: number): void {
    this.orderService.addProductToOrder(productId, 1).subscribe({
      next: (response) => {
        console.log('Product added to cart', response);
        alert('Producto agregado al carrito');
      },
      error: (err) => {
        console.error('Error adding product to cart', err);
        alert('Error al agregar el producto al carrito');
      }
    });
  }
}
