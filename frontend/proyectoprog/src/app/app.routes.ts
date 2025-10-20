// import { NgModule } from '@angular/core';
import { Routes } from '@angular/router';
// import { Navbar } from './components/navbar/navbar';

export const routes: Routes = [
  //  Auth
  { path: 'login', loadComponent: () => import('./pages/auth/login/login').then(m => m.Login) },
  { path: 'register', loadComponent: () => import('./pages/auth/register/register').then(m => m.Register) },
  // Perfil
  {path: 'perfil', loadComponent: () => import('./pages/perfil/perfil').then(m => m.Perfil) },
  { path: 'panel', loadComponent: () => import('./pages/panel/panel').then(m => m.Panel) },
  { path: 'panel', loadComponent: () => import('./pages/panel/panel').then(m => m.Panel) },


  // IMPORTS DE ADMIN
  { path: 'admin-menu', loadComponent: () => import('./pages/admin/admin-menu/admin-menu').then(m => m.AdminMenu) },
  {path:'gestion-menu-admin', loadComponent: ()=> import('./pages/admin/gestion-menu/gestion-menu').then(m=> m.GestionMenu)},
  {path: 'nuevo-producto-admin', loadComponent: () => import('./pages/admin/nuevo-producto/nuevo-producto').then(m=>m.NuevoProducto)},
  {path: 'pedidos-admin', loadComponent: () => import('./pages/admin/pedidos/pedidos').then(m=>m.Pedidos)},
  {path: 'promociones-admin', loadComponent: () => import('./pages/admin/promociones/promociones').then(m=>m.Promociones)},
  {path: 'usuarios-admin', loadComponent: () => import('./pages/admin/usuarios/usuarios').then(m=>m.Usuarios)},
  
  // IMPORTS DE CLIENTE
  { path: 'menu', loadComponent: () => import('./pages/cliente/menu/menu').then(m => m.Menu) },
  // Carrito
  { path: 'carrito', loadComponent: () => import('./pages/carrito/carrito').then(m => m.Carrito) },
  {path: 'carrito-calificacion-cliente',
     loadComponent: () => import('./pages/cliente/carrito-calificacion/carrito-calificacion').then(m=>m.CarritoCalificacion)},
  {path: 'carrito-envio-cliente', 
    loadComponent: () => import('./pages/cliente/carrito-envio/carrito-envio').then(m=>m.CarritoEnvio)},
    {path: 'carrito-pedido-cliente', loadComponent: () => import('./pages/cliente/carrito-pedido/carrito-pedido').then(m=>m.CarritoPedido)},
  
  // IMPORTS DE EMPLEADO
  { path: 'empleado-panel', loadComponent: () => import('./pages/empleado/empleado-panel/empleado-panel').then(m => m.EmpleadoPanel) },
  { path: 'estado-pedido', loadComponent: () => import('./pages/empleado/estado-pedido/estado-pedido').then(m => m.EstadoPedido) },
  { path: 'stock-productos', loadComponent: () => import('./pages/empleado/stock-productos/stock-productos').then(m => m.StockProductos) },
  { path: 'validar-cuentas', loadComponent: () => import('./pages/empleado/validar-cuentas/validar-cuentas').then(m => m.ValidarCuentas) },
  { path: 'gestion-clientes', loadComponent: () => import('./pages/empleado/gestion-clientes/gestion-clientes').then(m => m.GestionClientes) },

  //  Error y redirecciones
  { path: 'error', loadComponent: () => import('./pages/error-page/error-page').then(m => m.ErrorPage) },
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: '**', redirectTo: 'error' }
];
