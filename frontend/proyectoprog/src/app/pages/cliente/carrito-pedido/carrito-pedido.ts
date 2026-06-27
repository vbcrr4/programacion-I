import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BackButton } from "../../../components/back-button/back-button";
import { Navbar } from "../../../components/navbar/navbar";

@Component({
  selector: 'app-carrito-pedido',
  standalone: true,
  imports: [RouterLink, BackButton,Navbar],
  templateUrl: './carrito-pedido.html',
  styleUrl: './carrito-pedido.css'
})
export class CarritoPedido {

}
