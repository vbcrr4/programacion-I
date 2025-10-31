import { ComponentFixture, TestBed } from '@angular/core/testing';
import { EmpleadoPanel } from './empleado-panel';
import { RouterTestingModule } from '@angular/router/testing';
import { By } from '@angular/platform-browser';

describe('EmpleadoPanel', () => {
  let component: EmpleadoPanel;
  let fixture: ComponentFixture<EmpleadoPanel>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EmpleadoPanel, RouterTestingModule]
    }).compileComponents();

    fixture = TestBed.createComponent(EmpleadoPanel);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('debería crear el componente', () => {
    expect(component).toBeTruthy();
  });

  it('debería mostrar los números de pedidos y etiquetas correctas', () => {
    const stats = fixture.debugElement.queryAll(By.css('.action-btn .stat-number'));
    const labels = fixture.debugElement.queryAll(By.css('.action-btn .stat-label'));

    expect(stats[0].nativeElement.textContent).toContain('8');
    expect(stats[1].nativeElement.textContent).toContain('3');
    expect(labels[0].nativeElement.textContent).toContain('Pendientes');
    expect(labels[1].nativeElement.textContent).toContain('En preparación');
  });

  it('debería tener los botones con los routerLink correctos', () => {
    const links = fixture.debugElement.queryAll(By.css('.actions-grid a'));

    expect(links[0].attributes['ng-reflect-router-link']).toBe('/empleado/estado-pedido');
    expect(links[1].attributes['ng-reflect-router-link']).toBe('/empleado/stock-productos');
    expect(links[2].attributes['ng-reflect-router-link']).toBe('/empleado/validar-cuentas');
    expect(links[3].attributes['ng-reflect-router-link']).toBe('/empleado/gestion-clientes');
  });

  it('debería mostrar la sección de pedidos urgentes', () => {
    const urgentSection = fixture.debugElement.query(By.css('.urgent-section'));
    expect(urgentSection).toBeTruthy();

    const urgentOrder = urgentSection.query(By.css('.urgent-order .order-title'));
    expect(urgentOrder.nativeElement.textContent).toContain('Pedido #1240');
  });
});
