import { Component, OnInit } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { UniversalCard } from "../../components/universal-card/universal-card";
import { InputField } from '../../components/input/input';
import { ProductService } from '../../services/product.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, FormControl } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [Navbar, UniversalCard, InputField, ReactiveFormsModule, CommonModule],
  templateUrl: './menu.html',
  styleUrls: ['./menu.css']
})
export class Menu implements OnInit {
  products: any[] = [];
  currentPage: number = 1;
  totalPages: number = 1;
  perPage: number = 5;
  searchForm: FormGroup;

  constructor(private productService: ProductService, private fb: FormBuilder) {
    this.searchForm = this.fb.group({
      name: [''],
      category: ['']
    });
  }

  ngOnInit(): void {
    this.loadProducts();
  }

  loadProducts(): void {
    const { name, category } = this.searchForm.value;
    this.productService.getProducts(this.currentPage, this.perPage, name, category).subscribe({
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

  onSearch(): void {
    this.currentPage = 1;
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
}
