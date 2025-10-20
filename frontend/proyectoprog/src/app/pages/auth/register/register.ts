import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { UniversalCard } from '../../../components/universal-card/universal-card';
import { InputField } from '../../../components/input/input';
import { ButtonField } from '../../../components/button/button';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [RouterLink, UniversalCard, InputField, ButtonField],
  templateUrl: './register.html',
  styleUrl: './register.css'
})
export class Register {
}
