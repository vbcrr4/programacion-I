import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarritoPedido } from './carrito-pedido';

describe('CarritoPedido', () => {
  let component: CarritoPedido;
  let fixture: ComponentFixture<CarritoPedido>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CarritoPedido]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CarritoPedido);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
