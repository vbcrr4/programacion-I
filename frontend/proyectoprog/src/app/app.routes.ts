import { Routes } from '@angular/router';
import { AuthGuard } from './guards/auth.guard';
import { RoleGuard } from './guards/role.guard';

export const routes: Routes = [

  //  Auth
  { path: 'login', loadComponent: () => import('./pages/auth/login/login').then(m => m.Login) },
  { path: 'register', loadComponent: () => import('./pages/auth/register/register').then(m => m.Register) },
  // Perfil
  {path: 'perfil', loadComponent: () => import('./pages/perfil/perfil').then(m => m.Perfil), canActivate: [AuthGuard] },
  {path: 'panel', loadComponent: () => import('./pages/panel/panel').then(m => m.Panel), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin', 'Empleado'] } },
  


  
  // IMPORTS DE CLIENTE
  { path: 'menu', loadComponent: () => import('./pages/menu/menu').then(m => m.Menu) },
  // Carrito
  { path: 'carrito', loadComponent: () => import('./pages/carrito/carrito').then(m => m.Carrito), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Client'] } },
  {path: 'carrito-calificacion-cliente',
     loadComponent: () => import('./pages/cliente/carrito-calificacion/carrito-calificacion').then(m=>m.CarritoCalificacion), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Client'] }},
  {path: 'carrito-envio-cliente', 
    loadComponent: () => import('./pages/cliente/carrito-envio/carrito-envio').then(m=>m.CarritoEnvio), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Client'] }},
    {path: 'carrito-pedido-cliente', loadComponent: () => import('./pages/cliente/carrito-pedido/carrito-pedido').then(m=>m.CarritoPedido), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Client'] }},
  

  //  Error y redirecciones
  { path: 'error', loadComponent: () => import('./pages/error-page/error-page').then(m => m.ErrorPage) },
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: '**', redirectTo: 'error' }
];
