import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EmpleadoPanel } from './empleado-panel';

describe('EmpleadoPanel', () => {
  let component: EmpleadoPanel;
  let fixture: ComponentFixture<EmpleadoPanel>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EmpleadoPanel]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EmpleadoPanel);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
