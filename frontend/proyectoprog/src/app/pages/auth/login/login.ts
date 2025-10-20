import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { UniversalCard } from '../../../components/universal-card/universal-card';
import { InputField } from '../../../components/input/input';
import { ButtonField } from '../../../components/button/button';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [RouterLink, UniversalCard, InputField, ButtonField],
  templateUrl: './login.html',
  styleUrls: ['./login.css']
})
export class Login {
}
