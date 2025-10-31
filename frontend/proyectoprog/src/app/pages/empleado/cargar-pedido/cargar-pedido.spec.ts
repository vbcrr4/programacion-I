import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CargarPedido } from './cargar-pedido';

describe('CargarPedido', () => {
  let component: CargarPedido;
  let fixture: ComponentFixture<CargarPedido>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CargarPedido]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CargarPedido);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
