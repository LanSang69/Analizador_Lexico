import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OpcionalComponent } from './opcional.component';

describe('OpcionalComponent', () => {
  let component: OpcionalComponent;
  let fixture: ComponentFixture<OpcionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [OpcionalComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(OpcionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
