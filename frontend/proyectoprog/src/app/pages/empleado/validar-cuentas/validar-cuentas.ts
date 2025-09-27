import { Component } from '@angular/core';
import { AppRoutingModule } from "../../admin/admin-routing.routes";
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-validar-cuentas',
  standalone: true,
  imports: [AppRoutingModule, RouterLink],
  templateUrl: './validar-cuentas.html',
  styleUrls: ['./validar-cuentas.css']
})
export class ValidarCuentas {

}
