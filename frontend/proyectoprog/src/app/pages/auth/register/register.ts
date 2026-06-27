import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { UniversalCard } from '../../../components/universal-card/universal-card';
import { InputField } from '../../../components/input/input';
import { ActionBttn } from '../../../components/action-bttn/action-bttn';
import { AuthService } from '../../../services/auth.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [RouterLink, UniversalCard, InputField, ActionBttn, ReactiveFormsModule, CommonModule],
  templateUrl: './register.html',
  styleUrl: './register.css'
})
export class Register {
  registerForm: FormGroup;
  errorMessage: string = '';

  constructor(private fb: FormBuilder, private authService: AuthService, private router: Router) {
    this.registerForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(6)]],
      cellphone: ['', Validators.required],
      address: ['', Validators.required]
    });
  }



  onSubmit(): void {
    console.log('onSubmit called');
    console.log('form valid:', this.registerForm.valid);
    console.log('form value:', this.registerForm.value);
    if (this.registerForm.valid) {
      this.errorMessage = '';
      this.authService.register(this.registerForm.value).subscribe({
        next: () => {
          this.router.navigate(['/login']);
        },
        error: (err) => {
          this.errorMessage = 'Ocurrió un error inesperado. Por favor, intente nuevamente';
          console.error('Registration failed', err);
        }
      });
    }
  }
}
