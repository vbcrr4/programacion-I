import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BackButton } from '../../../components/back-button/back-button';

@Component({
  selector: 'app-promociones',
  imports: [RouterLink,BackButton],
  templateUrl: './promociones.html',
  styleUrl: './promociones.css'
})
export class Promociones {

}
