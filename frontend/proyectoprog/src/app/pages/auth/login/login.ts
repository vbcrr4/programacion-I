import { Component } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { UniversalCard } from '../../../components/universal-card/universal-card';
import { InputField } from '../../../components/input/input';
import { ActionBttn } from '../../../components/action-bttn/action-bttn';
import { AuthService } from '../../../services/auth.service';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterLink, UniversalCard, InputField, ActionBttn, ReactiveFormsModule],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class Login {
  loginForm: FormGroup;

  constructor(private fb: FormBuilder, private authService: AuthService, private router: Router) {
    this.loginForm = this.fb.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onSubmit(): void {
    if (this.loginForm.valid) {
      this.authService.login(this.loginForm.value).subscribe({
        next: () => {
          this.router.navigate(['/menu']);
        },
        error: (err) => {
          console.error('Login failed', err);
        }
      });
    }
  }
}
