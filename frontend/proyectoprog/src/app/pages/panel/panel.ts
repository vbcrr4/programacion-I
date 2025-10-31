import { Component,Input,input } from '@angular/core';
import { Navbar } from "../../components/navbar/navbar";
import { CardContenedora } from "../../components/card-contenedora/card-contenedora";
import { Card } from "../../components/card/card";
import { ActionBttn } from '../../components/action-bttn/action-bttn';
import { TextArea } from "../../components/textarea/textarea";
import { CalifiEstrellas } from '../../components/calfiestrellas/calfiestrellas';
import { UniversalCard } from '../../components/universal-card/universal-card';
import { InputField } from '../../components/input/input';

@Component({
  selector: 'app-panel',
  imports: [Navbar, CardContenedora, Card, ActionBttn, TextArea,UniversalCard,InputField],
  templateUrl: './panel.html',
  styleUrl: './panel.css'
})
export class Panel {
  //esto es temporal para simular el rol del usuario
  rol: 'admin' | 'empleado' = 'admin';
  tabseleccionada: string = "Gestion de menu";

  cambiarRol() {
    this.rol = this.rol === 'admin' ? 'empleado' : 'admin';
  }

  usuarios = [
    { nombre: 'Juan Pérez', email: 'juanperez@gmail.com', rol: 'Cliente' },
    { nombre: 'María Gómez', email: 'maria.gomez@gmail.com', rol: 'Empleado' },
    { nombre: 'Lucas Díaz', email: 'lucasdiaz@gmail.com', rol: 'Cliente' },
    { nombre: 'Sofía Fernández', email: 'sofiaf@gmail.com', rol: 'Administrador' },
  ];
}

