import { Component } from '@angular/core';
import { AppRoutingModule } from "../../admin/admin-routing.routes";
import { RouterLink } from '@angular/router';
@Component({
  selector: 'app-gestion-clientes',

  imports: [AppRoutingModule,RouterLink],
  templateUrl: './gestion-clientes.html',
  styleUrls: ['./gestion-clientes.css']
})
export class GestionClientes {

}
