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
  


  // IMPORTS DE ADMIN
  { path: 'admin-menu', loadComponent: () => import('./pages/admin/admin-menu/admin-menu').then(m => m.AdminMenu), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin'] } },
  {path:'gestion-menu-admin', loadComponent: ()=> import('./pages/admin/gestion-menu/gestion-menu').then(m=> m.GestionMenu), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin'] }},
  {path: 'nuevo-producto-admin', loadComponent: () => import('./pages/admin/nuevo-producto/nuevo-producto').then(m=>m.NuevoProducto), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin'] }},
  {path: 'pedidos-admin', loadComponent: () => import('./pages/admin/pedidos/pedidos').then(m=>m.Pedidos), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin', 'Empleado'] }},
  {path: 'promociones-admin', loadComponent: () => import('./pages/admin/promociones/promociones').then(m=>m.Promociones), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin'] }},
  {path: 'usuarios-admin', loadComponent: () => import('./pages/admin/usuarios/usuarios').then(m=>m.Usuarios), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin'] }},
  
  // IMPORTS DE CLIENTE
  { path: 'menu', loadComponent: () => import('./pages/menu/menu').then(m => m.Menu) },
  // Carrito
  { path: 'carrito', loadComponent: () => import('./pages/carrito/carrito').then(m => m.Carrito), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Client'] } },
  {path: 'carrito-calificacion-cliente',
     loadComponent: () => import('./pages/cliente/carrito-calificacion/carrito-calificacion').then(m=>m.CarritoCalificacion), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Client'] }},
  {path: 'carrito-envio-cliente', 
    loadComponent: () => import('./pages/cliente/carrito-envio/carrito-envio').then(m=>m.CarritoEnvio), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Client'] }},
    {path: 'carrito-pedido-cliente', loadComponent: () => import('./pages/cliente/carrito-pedido/carrito-pedido').then(m=>m.CarritoPedido), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Client'] }},
  
  // IMPORTS DE EMPLEADO
  { path: 'empleado-panel', loadComponent: () => import('./pages/empleado/empleado-panel/empleado-panel').then(m => m.EmpleadoPanel), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin', 'Empleado'] } },
  { path: 'estado-pedido', loadComponent: () => import('./pages/empleado/estado-pedido/estado-pedido').then(m => m.EstadoPedido), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin', 'Empleado'] } },
  { path: 'stock-productos', loadComponent: () => import('./pages/empleado/stock-productos/stock-productos').then(m => m.StockProductos), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin', 'Empleado'] } },
  { path: 'validar-cuentas', loadComponent: () => import('./pages/empleado/validar-cuentas/validar-cuentas').then(m => m.ValidarCuentas), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin'] } },
  { path: 'gestion-clientes', loadComponent: () => import('./pages/empleado/gestion-clientes/gestion-clientes').then(m => m.GestionClientes), canActivate: [AuthGuard, RoleGuard], data: { expectedRoles: ['Admin'] } },

  //  Error y redirecciones
  { path: 'error', loadComponent: () => import('./pages/error-page/error-page').then(m => m.ErrorPage) },
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: '**', redirectTo: 'error' }
];
