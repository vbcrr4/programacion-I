import { Component } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { Card } from "../../components/card/card";
import { ButtonField } from "../../components/button/button";
import { UniversalCard } from "../../components/universal-card/universal-card";

@Component({
  selector: 'app-perfil',
  standalone: true,
  imports: [Navbar, Card, UniversalCard, ButtonField],
  templateUrl: './perfil.html',
  styleUrl: './perfil.css'
})
export class Perfil {
  profileImage = "assets/user-profile.jpg"
  cellphone = "261-773-5309"
  email = "test@gmail.com"
  address = "Mendoza, Argentina"
  role = "admin"
  state = "active"
  created_at = "02/02/2002"
}
