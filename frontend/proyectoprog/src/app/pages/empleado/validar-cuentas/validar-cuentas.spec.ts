import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ValidarCuentas } from './validar-cuentas';

describe('ValidarCuentas', () => {
  let component: ValidarCuentas;
  let fixture: ComponentFixture<ValidarCuentas>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ValidarCuentas]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ValidarCuentas);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
