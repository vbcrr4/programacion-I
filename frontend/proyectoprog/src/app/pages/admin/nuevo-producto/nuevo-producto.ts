import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BackButton } from '../../../components/back-button/back-button';
@Component({
  selector: 'app-nuevo-producto',
  imports: [RouterLink,BackButton],
  templateUrl: './nuevo-producto.html',
  styleUrl: './nuevo-producto.css'
})
export class NuevoProducto {

}
