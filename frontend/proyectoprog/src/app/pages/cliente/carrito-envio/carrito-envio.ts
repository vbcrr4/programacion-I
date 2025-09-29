import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BackButton } from '../../../components/back-button/back-button';

@Component({
  selector: 'app-carrito-envio',
  imports: [RouterLink,BackButton],
  templateUrl: './carrito-envio.html',
  styleUrl: './carrito-envio.css'
})
export class CarritoEnvio {

}
