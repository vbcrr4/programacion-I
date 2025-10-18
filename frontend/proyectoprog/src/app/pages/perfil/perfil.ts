import { Component } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { Card } from "../../components/card/card";
import { ActionBttn } from "../../components/action-bttn/action-bttn";
import { CardContenedora } from "../../components/card-contenedora/card-contenedora";

@Component({
  selector: 'app-perfil',
  imports: [Navbar, Card, CardContenedora, ActionBttn],
  standalone: true,
  templateUrl: './perfil.html',
  styleUrl: './perfil.css'
})
export class Perfil {
cellphone = "261-773-5309"
email = "test@gmail.com"
address = "Mendoza, Argentina"
role = "admin"
state = "active"
created_at = "02/02/2002"
}
