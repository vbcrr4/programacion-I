import { Routes } from '@angular/router';
import { Pedidos } from './pages/admin/pedidos/pedidos';

export const routes: Routes = [
  //  Auth
  { path: 'login', loadComponent: () => import('./pages/auth/login/login').then(m => m.Login) },
  { path: 'register', loadComponent: () => import('./pages/auth/register/register').then(m => m.Register) },

  //  Admin
  { path: 'admin-menu', loadComponent: () => import('./pages/admin/admin-menu/admin-menu').then(m => m.AdminMenu) },
  { path: 'pedidos', loadComponent: () => import('./pages/admin/pedidos/pedidos').then(m => m.Pedidos) },

  // Cliente
  { path: 'menu', loadComponent: () => import('./pages/cliente/menu/menu').then(m => m.Menu) },

  //  Empleado
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
