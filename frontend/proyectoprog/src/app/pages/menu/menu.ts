import { Component } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { UniversalCard } from "../../components/universal-card/universal-card";
import { InputField } from '../../components/input/input';

@Component({
  selector: 'app-menu',
  standalone: true,
  imports: [Navbar, UniversalCard, InputField],
  templateUrl: './menu.html',
  styleUrls: ['./menu.css']
})
export class Menu {
}
