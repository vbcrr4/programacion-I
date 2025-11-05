import { Component, OnInit } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { Card } from "../../components/card/card";
import { ButtonField } from "../../components/button/button";
import { UniversalCard } from "../../components/universal-card/universal-card";
import { UserService } from '../../services/user.service';
import { AuthService } from '../../services/auth.service';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { InputField } from '../../components/input/input';

@Component({
  selector: 'app-perfil',
  standalone: true,
  imports: [Navbar, Card, UniversalCard, ButtonField, ReactiveFormsModule, CommonModule, InputField],
  templateUrl: './perfil.html',
  styleUrl: './perfil.css'
})
export class Perfil implements OnInit {
  profileImage = "assets/user-profile.jpg";
  user: any;
  profileForm: FormGroup;
  editMode: boolean = false;

  constructor(
    private userService: UserService,
    private authService: AuthService,
    private fb: FormBuilder,
    private router: Router
  ) {
    this.profileForm = this.fb.group({
      name: ['', Validators.required],
      cellphone: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      address: [''],
      role: [''],
      is_active: [false]
    });
  }

  ngOnInit(): void {
    this.loadUserProfile();
  }

  loadUserProfile(): void {
    const userId = this.authService.getUserId(); // Assuming you have a getUserId method in AuthService
    if (userId) {
      this.userService.getUser(userId).subscribe({
        next: (data) => {
          this.user = data;
          this.profileForm.patchValue(data);
        },
        error: (err) => {
          console.error('Error loading user profile', err);
          this.authService.logout();
          this.router.navigate(['/login']);
        }
      });
    }
  }

  toggleEditMode(): void {
    this.editMode = !this.editMode;
  }

  onSubmit(): void {
    if (this.profileForm.valid && this.user) {
      this.userService.updateUser(this.user.id, this.profileForm.value).subscribe({
        next: (data) => {
          this.user = data;
          this.editMode = false;
          alert('Perfil actualizado con éxito!');
        },
        error: (err) => {
          console.error('Error updating profile', err);
          alert('Error al actualizar el perfil.');
        }
      });
    }
  }

  deleteAccount(): void {
    if (confirm('¿Estás seguro de que quieres desactivar tu cuenta?')) {
      if (this.user) {
        this.userService.deleteUser(this.user.id).subscribe({
          next: () => {
            alert('Cuenta desactivada con éxito.');
            this.authService.logout();
            this.router.navigate(['/login']);
          },
          error: (err) => {
            console.error('Error desactivando cuenta', err);
            alert('Error al desactivar la cuenta.');
          }
        });
      }
    }
  }
}
