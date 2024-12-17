import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SintacticoComponent } from './sintactico.component';

describe('SintacticoComponent', () => {
  let component: SintacticoComponent;
  let fixture: ComponentFixture<SintacticoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SintacticoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SintacticoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
