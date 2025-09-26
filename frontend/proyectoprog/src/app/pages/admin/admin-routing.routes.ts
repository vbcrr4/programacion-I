 import { NgModule } from '@angular/core';
import { Routes,RouterModule } from '@angular/router';
//  import { GestionMenu } from '../gestion-menu/gestion-menu';
// import { NuevoProducto } from '../nuevo-producto/nuevo-producto';
// import { Pedidos } from '../pedidos/pedidos';
// import { Promociones } from '../promociones/promociones';
// import { Usuarios } from '../usuarios/usuarios';

// No se cual es la diferencia entre lo anterior y lo que sigue

export const routes: Routes = [

    { path: 'gestion-menu-admin', loadChildren: () => import('./gestion-menu/gestion-menu').then(m => m.GestionMenu) },
    { path: 'nuevo-producto-admin', loadChildren: () => import('./nuevo-producto/nuevo-producto').then(m => m.NuevoProducto) },
    { path: 'pedidos-admin', loadChildren: () => import('./pedidos/pedidos').then(m => m.Pedidos) },
    { path: 'promociones-admin', loadChildren: () => import('./promociones/promociones').then(m => m.Promociones) },
    {path: 'usuarios-admin', loadChildren: () => import('./usuarios/usuarios').then(m=>m.Usuarios)},
    { path: '', redirectTo: 'auth' },

    { path: '**', loadComponent: () => import('../error-page/error-page').then(c => c.ErrorPage) }
  ];
  
   @NgModule({
     imports: [RouterModule.forChild(routes)],
     exports: [RouterModule]
   })
   export class AppRoutingModule { }