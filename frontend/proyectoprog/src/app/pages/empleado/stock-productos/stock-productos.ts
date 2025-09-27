import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-stock-productos',
  standalone : true,
  imports: [CommonModule,RouterLink],
  templateUrl: './stock-productos.html',
  styleUrls: ['./stock-productos.css']
})
export class StockProductos {

}
