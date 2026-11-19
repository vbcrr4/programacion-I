import { Component } from '@angular/core';
import { Navbar } from "../../../components/navbar/navbar";
import { ActionBttn } from "../../../components/action-bttn/action-bttn";
import { BackButton } from "../../../components/back-button/back-button";
@Component({
  selector: 'app-admin-menu',
  imports: [ Navbar, ActionBttn, BackButton],
  standalone:true,
  templateUrl: './admin-menu.html',
  styleUrl: './admin-menu.css'
})
export class AdminMenu {

}
