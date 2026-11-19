import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BackButton } from '../../../components/back-button/back-button';
import { UserService } from '../../../services/user.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, FormControl } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-usuarios',
  standalone: true,
  imports: [RouterLink, BackButton, ReactiveFormsModule, CommonModule],
  templateUrl: './usuarios.html',
  styleUrl: './usuarios.css'
})
export class Usuarios implements OnInit {
  users: any[] = [];
  currentPage: number = 1;
  totalPages: number = 1;
  perPage: number = 10;
  searchForm: FormGroup;

  constructor(private userService: UserService, private fb: FormBuilder) {
    this.searchForm = this.fb.group({
      address: [''],
      role: [''],
      nrOrders: [null]
    });
  }

  ngOnInit(): void {
    this.loadUsers();
  }

  loadUsers(): void {
    const { address, role, nrOrders } = this.searchForm.value;
    this.userService.getUsers(this.currentPage, this.perPage, address, role, nrOrders).subscribe({
      next: (response) => {
        this.users = response.users;
        this.totalPages = response.pages;
        this.currentPage = response.page;
      },
      error: (err: any) => {
        console.error('Error loading users', err);
      }
    });
  }

  onSearch(): void {
    this.currentPage = 1;
    this.loadUsers();
  }

  goToPage(page: number): void {
    if (page >= 1 && page <= this.totalPages) {
      this.currentPage = page;
      this.loadUsers();
    }
  }

  nextPage(): void {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
      this.loadUsers();
    }
  }

  prevPage(): void {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.loadUsers();
    }
  }

  getPagesArray(): number[] {
    return Array.from({ length: this.totalPages }, (_, i) => i + 1);
  }

  deleteUser(userId: number): void {
    if (confirm('¿Estás seguro de que quieres eliminar este usuario?')) {
      this.userService.deleteUser(userId).subscribe({
        next: () => {
          alert('Usuario eliminado con éxito.');
          this.loadUsers(); // Reload users after deletion
        },
        error: (err: any) => {
          console.error('Error eliminando usuario', err);
          alert('Error al eliminar el usuario.');
        }
      });
    }
  }
}
