import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CerraduraKleeneComponent } from './cerradura-kleene.component';

describe('CerraduraKleeneComponent', () => {
  let component: CerraduraKleeneComponent;
  let fixture: ComponentFixture<CerraduraKleeneComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CerraduraKleeneComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CerraduraKleeneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
