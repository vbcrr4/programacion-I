import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-navbar',
  imports: [RouterLink, CommonModule],
  standalone: true,
  templateUrl: './navbar.html',
  styleUrls: ['./navbar.css']
})
export class Navbar {

  constructor(private authService: AuthService, private router: Router) { }

  isLoggedIn(): boolean {
    return this.authService.isLoggedIn();
  }

  isAdmin(): boolean {
    return this.authService.getUserRole() === 'Admin';
  }

  isClient(): boolean {
    return this.authService.getUserRole() === 'Client';
  }

  isEmpleado(): boolean {
    return this.authService.getUserRole() === 'Empleado';
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }
}
