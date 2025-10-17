import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BackButton } from '../../../components/back-button/back-button';
import { Navbar } from "../../../components/navbar/navbar";


@Component({
  selector: 'app-carrito-calificacion',
  imports: [RouterLink,BackButton,Navbar],
  templateUrl: './carrito-calificacion.html',
  styleUrl: './carrito-calificacion.css'
})
export class CarritoCalificacion {

}
