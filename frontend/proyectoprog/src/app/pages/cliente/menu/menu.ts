import { Component } from '@angular/core';
import { Navbar } from "../../../components/navbar/navbar";
import { SearchBar } from "../../../components/search-bar/search-bar";

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [Navbar, SearchBar],
  templateUrl: './menu.html',
  styleUrls: ['./menu.css']
})
export class Menu {

}
