import { Component } from '@angular/core';

import { RouterLink } from '@angular/router';
import { BackButton } from '../../../components/back-button/back-button';

@Component({
  selector: 'app-validar-cuentas',
  standalone: true,
  imports: [ RouterLink,BackButton],
  templateUrl: './validar-cuentas.html',
  styleUrls: ['./validar-cuentas.css']
})
export class ValidarCuentas {

}
