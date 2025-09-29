import { Component } from '@angular/core';

import { RouterLink } from '@angular/router';
import { BackButton } from '../../../components/back-button/back-button';
@Component({
  selector: 'app-gestion-clientes',

  imports: [RouterLink,BackButton],
  templateUrl: './gestion-clientes.html',
  styleUrls: ['./gestion-clientes.css']
})
export class GestionClientes {

}
