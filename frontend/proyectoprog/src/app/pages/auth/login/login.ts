import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { UniversalCard } from '../../../components/universal-card/universal-card';
import { InputField } from '../../../components/input/input';
import { ActionBttn } from '../../../components/action-bttn/action-bttn';
import { AuthService } from '../../../services/auth.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { NgIf } from '@angular/common';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterLink, UniversalCard, InputField, ActionBttn, ReactiveFormsModule, NgIf],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class Login {
  loginForm: FormGroup;
  errorMessage: string = '';

  constructor(private fb: FormBuilder, private authService: AuthService, private router: Router) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.loginForm.valid) {
      this.errorMessage = '';
      this.authService.login(this.loginForm.value).subscribe({
        next: () => {
          this.router.navigate(['/menu']);
        },
        error: (err) => {
          if (err.status === 401) {
            this.errorMessage = 'Usuario o contraseña incorrecta';
          } else {
            this.errorMessage = 'Ocurrió un error. Por favor, intente nuevamente';
          }
          console.error('Login failed', err);
        }
      });
    }
  }
}
