import { Component } from '@angular/core';
import { Navbar } from "../../../components/navbar/navbar";
import { SearchBar } from "../../../components/search-bar/search-bar";
import { Card } from '../../../components/card/card';
import { CardContenedora } from "../../../components/card-contenedora/card-contenedora";


@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [Navbar, SearchBar, Card, CardContenedora],
  templateUrl: './menu.html',
  styleUrls: ['./menu.css']
})
export class Menu {

}
