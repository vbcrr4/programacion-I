import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Calfiestrellas } from './calfiestrellas';

describe('Calfiestrellas', () => {
  let component: Calfiestrellas;
  let fixture: ComponentFixture<Calfiestrellas>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Calfiestrellas]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Calfiestrellas);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
