import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BackButton } from '../../../components/back-button/back-button';
import { Navbar } from "../../../components/navbar/navbar";


@Component({
  selector: 'app-carrito-envio',
  imports: [RouterLink,BackButton,Navbar],
  templateUrl: './carrito-envio.html',
  styleUrl: './carrito-envio.css'
})
export class CarritoEnvio {

}
