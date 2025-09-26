// import { NgModule } from '@angular/core';RouterModule

import { Routes } from '@angular/router';

import { CargarPedido } from '../cargar-pedido/cargar-pedido';
import { EstadoPedido } from '../estado-pedido/estado-pedido';
import { GestionClientes } from '../gestion-clientes/gestion-clientes';
import { StockProductos } from '../stock-productos/stock-productos';
import { ValidarCuentas } from '../validar-cuentas/validar-cuentas';

export const routes: Routes= [
    {path:'cargarpedido-empl', component:CargarPedido},
    {path:'estadopedido-empl', component:EstadoPedido},
    {path:'gestionclientes-empl', component:GestionClientes},
    {path:'stockproductos-empl', component:StockProductos},
    {path:'validarcuentas-empl', component:ValidarCuentas},
]

// no se que hace esto asique lo comento
// @NgModule({
//     imports: [RouterModule.forRoot(routes)],
//     exports: [RouterModule]
//   })
//   export class AppRoutingModule { }