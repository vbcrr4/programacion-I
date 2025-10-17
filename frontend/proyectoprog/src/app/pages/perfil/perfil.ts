import { Component } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";

@Component({
  selector: 'app-perfil',
  imports: [Navbar],
  standalone: true,
  templateUrl: './perfil.html',
  styleUrl: './perfil.css'
})
export class Perfil {

}
