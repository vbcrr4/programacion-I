import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { BackButton } from '../../../components/back-button/back-button';

@Component({
  selector: 'app-stock-productos',
  standalone : true,
  imports: [CommonModule,RouterLink,BackButton],
  templateUrl: './stock-productos.html',
  styleUrls: ['./stock-productos.css']
})
export class StockProductos {

}
