import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearBasicoComponent } from './crear-basico.component';

describe('CrearBasicoComponent', () => {
  let component: CrearBasicoComponent;
  let fixture: ComponentFixture<CrearBasicoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CrearBasicoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CrearBasicoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
