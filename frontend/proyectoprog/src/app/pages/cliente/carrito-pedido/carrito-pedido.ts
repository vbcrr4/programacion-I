import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BackButton } from "../../../components/back-button/back-button";

@Component({
  selector: 'app-carrito-pedido',
  imports: [RouterLink, BackButton],
  templateUrl: './carrito-pedido.html',
  styleUrl: './carrito-pedido.css'
})
export class CarritoPedido {

}
