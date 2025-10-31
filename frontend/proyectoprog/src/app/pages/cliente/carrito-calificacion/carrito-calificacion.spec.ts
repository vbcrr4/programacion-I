import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CarritoCalificacion } from './carrito-calificacion';

describe('CarritoCalificacion', () => {
  let component: CarritoCalificacion;
  let fixture: ComponentFixture<CarritoCalificacion>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CarritoCalificacion]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CarritoCalificacion);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
