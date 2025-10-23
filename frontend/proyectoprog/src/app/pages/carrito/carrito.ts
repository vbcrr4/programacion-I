import { Component } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { UniversalCard } from "../../components/universal-card/universal-card";
import { Card } from "../../components/card/card";
import { ActionBttn } from '../../components/action-bttn/action-bttn';
import { TextArea } from "../../components/textarea/textarea";
import { CalifiEstrellas } from '../../components/calfiestrellas/calfiestrellas';


@Component({
  selector: 'app-carrito',
  standalone: true,
  imports: [Navbar, UniversalCard, Card, ActionBttn, TextArea, CalifiEstrellas],
  templateUrl: './carrito.html',
  styleUrl: './carrito.css'
})
export class Carrito {
  status = "Listo"
  del_status = "En camino"
  del_price = "$5.000"
  del_address = "Av. Boulogne Sur Mer 683, M5500 Mendoza"
  tabseleccionada = "pedido"

}
