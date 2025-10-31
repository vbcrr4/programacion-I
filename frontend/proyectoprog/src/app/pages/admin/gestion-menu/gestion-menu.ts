import { Component } from '@angular/core';
import { RouterLink } from "@angular/router";
import { BackButton } from '../../../components/back-button/back-button';

@Component({
  selector: 'app-gestion-menu',
  imports: [RouterLink,BackButton],
  templateUrl: './gestion-menu.html',
  styleUrl: './gestion-menu.css'
})
export class GestionMenu {

}
