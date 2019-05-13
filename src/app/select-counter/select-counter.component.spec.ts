import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SelectCounterComponent } from './select-counter.component';

describe('SelectCounterComponent', () => {
  let component: SelectCounterComponent;
  let fixture: ComponentFixture<SelectCounterComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SelectCounterComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SelectCounterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
