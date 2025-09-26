// import { NgModule } from '@angular/core';RouterModule
import { Routes } from '@angular/router';

import { CarritoPedido } from '../carrito-pedido/carrito-pedido';
import { CarritoEnvio } from '../carrito-envio/carrito-envio';
import { CarritoCalificacion } from '../carrito-calificacion/carrito-calificacion';

export const routes: Routes = [
  {path:'carrito-pedido', component:CarritoPedido},
  {path:'carrito-envio', component:CarritoEnvio},
  {path:'carrito-calificacion', component:CarritoCalificacion}
  
]


// @NgModule({
//     imports: [RouterModule.forRoot(routes)],
//     exports: [RouterModule]
//   })
//   export class AppRoutingModule { }