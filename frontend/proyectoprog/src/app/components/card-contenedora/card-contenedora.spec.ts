import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardContenedora } from './card-contenedora';

describe('CardContenedora', () => {
  let component: CardContenedora;
  let fixture: ComponentFixture<CardContenedora>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CardContenedora]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CardContenedora);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
