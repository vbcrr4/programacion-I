import { Component } from '@angular/core';
import { Navbar } from "../../../components/navbar/navbar";

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [Navbar],
  templateUrl: './menu.html',
  styleUrls: ['./menu.css']
})
export class Menu {

}
