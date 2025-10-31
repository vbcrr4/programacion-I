import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { BackButton } from '../../../components/back-button/back-button';

@Component({
  selector: 'app-estado-pedido',
  standalone: true,
  imports: [RouterLink, CommonModule, BackButton],
  templateUrl: './estado-pedido.html',
  styleUrls: ['./estado-pedido.css']
})
export class EstadoPedido {}
