import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarritoEnvio } from './carrito-envio';

describe('CarritoEnvio', () => {
  let component: CarritoEnvio;
  let fixture: ComponentFixture<CarritoEnvio>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CarritoEnvio]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CarritoEnvio);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
