import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CerraduraPositivaComponent } from './cerradura-positiva.component';

describe('CerraduraPositivaComponent', () => {
  let component: CerraduraPositivaComponent;
  let fixture: ComponentFixture<CerraduraPositivaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CerraduraPositivaComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CerraduraPositivaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
