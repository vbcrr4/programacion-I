import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ActionBttn } from './action-bttn';

describe('ActionBttn', () => {
  let component: ActionBttn;
  let fixture: ComponentFixture<ActionBttn>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ActionBttn]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ActionBttn);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
