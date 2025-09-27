import { Pedidos } from './pages/admin/pedidos/pedidos';
import { Routes } from '@angular/router';

export const routes: Routes = [
{path:'login', loadComponent: () => import('./pages/auth/login/login').then(m => m.Login)},
{path:'register', loadComponent: () => import('./pages/auth/register/register').then(m => m.Register)},
{path:'admin-menu', loadComponent: () => import('./pages/admin/admin-menu/admin-menu').then(m => m.AdminMenu)},
{path:'menu', loadComponent: () => import('./pages/cliente/menu/menu').then(m => m.Menu)},
{path:'empleado-panel', loadComponent: () => import('./pages/empleado/empleado-panel/empleado-panel').then(m => m.EmpleadoPanel)},
{path:'estado-pedido', loadComponent: () => import('./pages/empleado/estado-pedido/estado-pedido').then(m => m.EstadoPedido)},
{path:'error', loadComponent: ()=>import('./pages/error-page/error-page').then(m=>m.ErrorPage)},
{path:'', redirectTo: 'login', pathMatch: 'full'},
{path:'**',redirectTo: 'error'},
];
