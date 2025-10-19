import { Component } from '@angular/core';
import { Navbar } from "../../../components/navbar/navbar";
import { Card } from '../../../components/card/card';
import { CardContenedora } from "../../../components/card-contenedora/card-contenedora";
import { TextArea } from '../../../components/textarea/textarea';


@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [Navbar, Card, CardContenedora,TextArea],
  templateUrl: './menu.html',
  styleUrls: ['./menu.css']
})
export class Menu {

}
